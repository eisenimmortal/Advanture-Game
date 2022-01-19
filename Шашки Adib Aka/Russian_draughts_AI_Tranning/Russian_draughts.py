
from Board import Board

import heapq as hq
import itertools as it
import numpy as np

from Players import Player, Move
from Figures import Empty, Simple, King
from NeuroNet import NeuroNet

class Draughts_Game:
	def __init__(self, board, neuro_net, winner_color="white"):
		self.board = board
		self.neuro_net = neuro_net
		self.players = it.cycle([board.player1, board.player2])
		self.now_playing = next(self.players)
		self.winner_color = winner_color
		self.moves_to_draw = 0
#		self.all_figs1 = board.player1.all_figures()
#		self.all_figs2 = self.player2.all_figures()
#		self.all_figs = self.all_figs1 + self.all_figs2
		
		self.is_game_over = False
		self.is_draw = False
	
	
	def play_predicated(self):
		self.check_to_draw()
		if self.is_draw:
			self.is_game_over = True
			return
		beating_fig = self.board.beating_figure
		# if we have beating figure
		if not (beating_fig is None):
			move = self.now_playing.choose_the_move(self.board, self.neuro_net)
			if move:
				self.board.handle_move(move)
			
			# if now_beating player no moves left
			else:
				self.board.clear_move()
				self.now_playing.is_moved = False
				self.now_playing = next(self.players)
		
		# if we haven't beating figure
		# and now_playing player have made his move
		elif self.now_playing.is_moved:
			self.board.clear_move()
			self.now_playing.is_moved = False
			self.now_playing = next(self.players)
		
		# if we haven't beating figure
		# and now_playing player have not made his move yet
		elif not self.now_playing.is_moved:
			move = self.now_playing.choose_the_move(self.board, self.neuro_net)
			# if now_playing player have move
			if move:
				self.board.handle_move(move)
			
			# if now_playing player can not move
			else:
				self.game_over()
				
				
		
	def game_over(self):
		loser = self.now_playing
		self.now_playing = next(self.players)
		winner = self.now_playing
		self.winner_color = winner.color
		print("\nGame over")
		print(winner.color, " wins")
		print(loser.color, " lose")
		self.is_game_over = True
	
	def check_to_draw(self):
		if (1<=len(self.board.player1.all_figures())<=3
		and 1<=len(self.board.player2.all_figures())<=3):
			self.moves_to_draw+=1
			if self.moves_to_draw > 60:
				self.is_draw = True
				self.is_game_over = True
			return
		self.is_draw = False
		self.moves_to_draw = 0
			

		


def init_board(player1_init_pos, player2_init_pos):
	whites = player1 = Player(player1_init_pos, "white", 1)
	blacks = player2 = Player(player2_init_pos, "black", -1)
	#blacks.simple_to_king(player2.simples[4])
	#whites.simple_to_king(whites.simples[0])
	new_board = Board(player1, player2)
	return new_board

def play_game(game):
	moves_count = 0
	while not game.is_game_over:
		if game.is_draw:
			print("DRAW")
			break
		game.play_predicated()
		#board.printout()
#		moves_count += 1
#		if (moves_count%1)==0:
#			print(moves_count)
#			game.board.printout()
		#print(moves_count)
		#print()
#	print(len(game.board.moves_queue))
#	print(sum(1 for i in game.board.moves_queue if i.beated_fig is None))


WHITES_INIT_POS = ((0,0), (2,0), (4,0), (6,0), (1,1), (3,1), (5,1), (7,1), (0,2), (2,2), (4,2), (6,2))
BLACKS_INIT_POS = ((1,7), (3,7), (5,7), (7,7), (0,6), (2,6), (4,6), (6,6), (1,5), (3,5), (5,5), (7,5))#, (7,7), (5,7), , , (6,6), (4,6))#(4,4), (2,2), (2,4), (4,2), (4,6)
#whites_init_pos = ((1,5),)
#blacks_init_pos = ((2,6),(6,4),(5,3),(3,5))


###### LOADING WEIGHTS #########

'''
with open(f'F:\Install\Программирование\Python\Projects\Checkers\Draughts_neuro_weights_whites_v0.3.txt', 'r+t') as file1:
	print(f'coursor at {file1.tell()}')
	loaded_arr_whites = np.loadtxt(file1)
'''

'''
with open(f'F:\Install\Программирование\Python\Projects\Checkers\Draughts_neuro_weights_blacks_v0.3.txt', 'r+t') as file2:
	print(f'coursor at {file2.tell()}')
	loaded_arr_blacks = np.loadtxt(file2)
#print(loaded_arr.shape)
'''

neuro_net = NeuroNet()
#neuro_net = NeuroNet(loaded_arr_whites, loaded_arr_blacks)

print((np.count_nonzero(neuro_net.weights["white"])))
#print((np.count_nonzero(neuro_net.weights["black"])))

winners_counter = {"white":0, "black":0}
moves_log_to_compare = ""

for epoch in range(1):
	board_to_play = init_board(WHITES_INIT_POS, BLACKS_INIT_POS)
	game = Draughts_Game(board_to_play, neuro_net)
	play_game(game)
	winners_counter[game.winner_color] +=1
	
#	input("game over")
#	print("is_draw", game.is_draw)
	if game.is_draw:
		print("DRAW")
		board_to_learn = init_board(WHITES_INIT_POS, BLACKS_INIT_POS)
		neuro_net.draw_learn(board_to_learn, board_to_play.moves_queue, game.winner_color)
		continue
	board_to_learn = init_board(WHITES_INIT_POS, BLACKS_INIT_POS)
	neuro_net.learn(board_to_learn, board_to_play.moves_queue, game.winner_color)
	#print((np.count_nonzero(neuro_net.weights)))
#	save_moves_log = input("Do you wanna save or compare moves log S/C/N")
#	if save_moves_log in "Ss":
#		moves_log_to_compare = board_to_play.moves_logger
#	elif save_moves_log in "CcСс":
#		print(board_to_play.moves_logger == moves_log_to_compare)
	#print(neuro_net.weights[neuro_net.weights!=0])

print(winners_counter)

##### SAVE WEGHTS ######

with open(f'F:\Install\Программирование\Python\Projects\Checkers\Draughts_neuro_weights_whites_v0.3.txt', 'wt') as file3:
#	print(f'coursor at {file3.tell()}')
	np.savetxt(file3, neuro_net.weights["white"])

'''
with open(f'F:\Install\Программирование\Python\Projects\Checkers\Draughts_neuro_weights_blacks_v0.3.txt', 'wt') as file4:
#	print(f'coursor at {file4.tell()}')
	np.savetxt(file4, neuro_net.weights["black"])
'''

#print(len(board.moves_logger))
#print(board.moves_logger)
#print(len(board.moves_queue))
#print(board.moves_queue)
#print("for whites")
#print(board.get_binar_input_for_NN(whites.direction).reshape(-1,4,8))
#print("for blackd")
#print(board.get_binar_input_for_NN(blacks.direction).reshape(-1,4,8))

#blacks_for_learn.simple_to_king(blacks_for_learn.simples[4])


####################################

'''

0 1 0 1 0 1 0 e
1 0 1 0 1 0 e 0
0 1 0 1 0 b 0 1
e 0 1 0 e 0 1 0
0 b 0 e 0 1 0 1
1 0 W 0 1 0 1 0
0 e 0 e 0 1 0 1
e 0 1 0 e 0 1 0

def upleft_beat_row_moves(position, i):
	row=upleft_beat_row(position, i)
	return [(4666+i*65-k*520) for k in range(2,8) if row&(1<<k)]
		#return [int(f'{k+2}{i}{k}{i+2}',8) for k in range(6) if row[k]=="1"]
	
'''
#------------

'''
is_blacks_turn = 0

turns=[empty, white_turn, black_turn]
turn = turns[is_blacks_turn]

is_blacks_turn ^=1

'''

