
from Figures import Empty, Simple, King
from Players import Player, Move, Convert_move
import numpy as np

# This script implements Board class and its metgods

class Board():
	def __init__(self, player1, player2, play_direction=1, beating_figure=None):
		self.player1 = player1
		self.player2 = player2
		#self.all_figs = all_figs
		self.play_direction = play_direction
		self.move_agregator = ""
		self.moves_logger = []
		self.moves_queue = []
		self.beating_figure = beating_figure
		#self.beated_figs_to_clear = []
		self.fig_types = (self.player1.simples, self.player1.kings, self.player2.kings, self.player2.simples)
		#index shift - direction(!) and figure type
		self.indx_shift = {1: {"simple": 0, "king":32}, -1:{"king":64, "simple": 96}}
		self.figures = {x: {y: Empty(x,y) for y in range(8) if (x+y)%2==0} for x in range(8)}
		
		#vector(192x1) representation of board
		self.bin_vector_repr_for_white = np.zeros(128, int)
		self.bin_vector_of_emptys_for_white = np.ones(32, int)
		self.bin_vector_of_beated_for_white = np.zeros(32, int)
		#self.figures1 = {f"{'abcdefgh'[x]}{y}":"0" if (x+y)%2==0 else "." for x in range(8) for y in range(1,9)}
		self.dict_first_upd()
		self.bin_vector_repr_for_black = np.flip(self.bin_vector_repr_for_white)
		self.bin_vector_of_emptys_for_black = np.flip(self.bin_vector_of_emptys_for_white)
		self.bin_vector_of_beated_for_black = np.flip(self.bin_vector_of_beated_for_white)
		
	def dict_first_upd(self):
		fig_types = self.fig_types[::self.player1.direction]
		for i,fig_type in enumerate(fig_types):
			for figure in fig_type:
				self.figures[figure.x][figure.y] = figure
				indx1 = figure.y*4 + figure.x//2
				indx2 = i*32 + indx1
				self.bin_vector_repr_for_white[indx2] = 1
				self.bin_vector_of_emptys_for_white[indx1] = 0
	
	def change_turn(self):
		self.play_direction = -1 * self.play_direction
	
	def is_empty(self, x, y):
		return (self.figures[x][y].color == "empty")
	
	def get_binar_input_for_NN(self, direction):
		#if direction == 1:
		if True:
			return np.hstack((
			self.bin_vector_repr_for_white,
			self.bin_vector_of_emptys_for_white,
			self.bin_vector_of_beated_for_white))
		
		# return np.hstack((
		# self.bin_vector_repr_for_black,
		# self.bin_vector_of_emptys_for_black,
		# self.bin_vector_of_beated_for_black))
		
		#return binar_input[player.direction]
	
	
	def handle_move(self, move):
		coords, num_of_moves = move
		x1, y1, x2, y2 = [int(i) for i in (Convert_move(coords).to_oct())]
		#print(x1, y1, x2, y2)
		#print(self.figures[x1])
		fig = self.figures[x1][y1]
		self.play_direction = fig.direction
		
		move_str_repr = Convert_move(coords).to_note()
		#print(move_str_repr)
		
		self.move_agregator = self.move_agregator[:-2] + move_str_repr
		
		shift_x = x2 - x1
		step_x = shift_x//abs(shift_x)
		shift_y = y2 - y1
		step_y = shift_y//abs(shift_y)
		
		beated_fig = None
		beated_coords_note = ""
		
		#change places of figures of board due to move
		for i in range(1, abs(shift_x)):
			x = x1+i*step_x
			y = y1+i*step_y
			to_beat = self.figures[x][y]
			#check for beating
			if to_beat.color != "empty":
				
				fig.is_beating_fig = True
				fig.player.beating_fig = fig
				self.beating_figure = fig
				
				beated_fig = to_beat
				beated_fig.is_beated = True
				
				#self.beated_figs_to_clear.append(beated_fig)
				beated_indx = ((beated_fig.x)//2 + (beated_fig.y)*4)# + 0.5) * to_beat.direction - 0.5
				self.bin_vector_of_beated_for_white[beated_indx] = 1
				beated_coords_note = ":"+"abcdefgh"[x]+str(y+1)+":"
				break
		
		#moves log
		#move_int_repr = fig.convert_2d_coords_into_1d_repr((x2, y2))
		self.move_agregator = self.move_agregator[:-2] + beated_coords_note + move_str_repr[-2:]
		move_to_log = Move((x1, y1, x2, y2,), num_of_moves, fig.fig_type, fig.color, fig.direction, beated_fig)
		self.moves_queue.append(move_to_log)
		
		self.swap_place(fig, x1, y1, x2, y2)
		
	def swap_place(self, fig, x1, y1, x2, y2):
		'''
		This realisation of swaping is FINALLY READY for RUSIAN DRAUGHTS:
		DO NOT CHANGE OR UPDATE IT !!!
		
		we can't just swap figs by coords and forget it,
		due to TARGET coords have the side-effect:
		moving the SIMPLE-draught can turn it to KING-fig
		'''
		########## work with source cell and coords ##########
		
		# set Empty-fig to source cell (x1, y1)
		self.figures[x1][y1] = Empty(x1, y1)
		
		# set entry of empty-fig to emptys bin vector, using source coords
		indx_for_set_empty = x1//2 + y1*4
		self.bin_vector_of_emptys_for_white[indx_for_set_empty] = 1
		
		# remove entry of fig from bin vector using source coords
		indx_shift = self.indx_shift[fig.direction][fig.fig_type]
		indx_for_remove_fig =  indx_for_set_empty + indx_shift
		self.bin_vector_repr_for_white[indx_for_remove_fig] = 0
		
		
		########## work with target cell and coords ##########
		
		# set figs inner coords to target coords
		fig.x, fig.y = x2, y2
		
		# remove entry of empty-fig from bin vector using target coords
		indx_for_remove_empty = x2//2 + y2*4
		self.bin_vector_of_emptys_for_white[indx_for_remove_empty] = 0
		
		# if simple draught reach the opposite side it becomes king
		if (fig.fig_type == "simple") and (y2 == (3.5 + (3.5 * fig.direction))):
			fig = fig.player.simple_to_king(fig)
		
		# set fig to boards target cell
		self.figures[x2][y2] = fig
		
		# set entry of fig to bin vector using target coords
		indx_shift = self.indx_shift[fig.direction][fig.fig_type]
		indx_for_set_fig = indx_shift + indx_for_remove_empty
		self.bin_vector_repr_for_white[indx_for_set_fig] = 1
		
		fig.player.is_moved = True
		#self.printout()

	def swap_figs_onboard(self, x1, y1, x2, y2):
		source_fig = self.figures[x1][y1]
		target_fig = self.figures[x2][y2]
		
		self.figures[x1][y1] = target_fig
		
		########## VERY IMPORTANT CHECKING #########
		# if simple draught reach the opposite side it becomes king
		
		if (source_fig.fig_type == "simple") and (y2 == (3.5 + (3.5 * source_fig.direction))):
			source_fig = source_fig.player.simple_to_king(source_fig)
		
		# set fig to boards target cell
		self.figures[x2][y2] = source_fig
		
		target_fig.x, target_fig.y = x1, y1
		source_fig.x, source_fig.y = x2, y2

	def one_move_back(self):
		move = self.moves_queue.pop()
		x1, y1, x2, y2 = move.coords
		source = x1//2 + y1*4
		target = x2//2 + y2*4
		vectorized_out_indx = source*32 + target
		fig = self.figures[x2][y2]
		
	def clear_move(self):
		if self.beating_figure != None:
			self.beating_figure.player.beating_fig = None
			self.beating_figure.is_beating_fig = False
			self.beating_figure = None
			
			fig_types = self.fig_types[::self.player1.direction]
			for i, fig_type in enumerate(fig_types):
				for figure in tuple(fig_type):
					if figure.is_beated:
						x, y = figure.x, figure.y
						self.figures[x][y] = Empty(x, y)
						fig_type.remove(figure)
						indx_for_set_empty = x//2 + y*4
						indx_for_remove_fig = i*32 + indx_for_set_empty
						self.bin_vector_repr_for_white[indx_for_remove_fig] = 0
						self.bin_vector_of_emptys_for_white[indx_for_set_empty] = 1
						self.bin_vector_of_beated_for_white[indx_for_set_empty] = 0
		
		self.moves_logger.append(self.move_agregator)
		self.move_agregator = ""
		#self.printout()
	
	def printout(self):
		print()
		for y in range(7,-1,-1):
			for x in range(8):
				if (x+y)%2==0:
					print(self.figures[x][y].repr(), end=" ")
				else:
					print(" ", end=" ")
			print()

