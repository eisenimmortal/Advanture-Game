
#Python 3.8.10

#This file contents classes of Figures of Russian Draughts:
#Empty cell, Simple draught, King draught

import itertools as it

#class Figure:
#	def __init__(self, x:int, y:int, color:str, direction: int, *args, is_beating_fig=False, is_beated=False):
#		self.x = x
#		self.y = y
#		self.color = color
#		self.direction = direction
#		self.is_beating_fig = is_beating_fig
#		self.is_beated = is_beated
#		#self.rep = self.color[0]
#		#self.is_touched = is_touched
#	
#	def get_coords_of_move_to(self, x2, y2):
#		return (self.x*512 + self.y*64 + x2*8 + y2)
#	
class Figure:
	def __init__(self, x:int, y:int):
		self.x = x
		self.y = y
		self.indx_shift = {1: {"simple": 0, "king":32}, -1:{"king":64, "simple": 96}}
	
	def get_flatted_indx(self):
		res = self.x // 2 + self.y * 4
		return res

class Empty:
	def __init__(self, x:int, y:int, color="empty"):
		self.x = x
		self.y = y
		self.color = color
	
	def repr(self):
		return "."#self.color[0]
		
	def get_flatted_indx(self):
		res = self.x // 2 + self.y * 4
		return res
		

class Simple():
	def __init__(self, x:int, y:int, color:str, direction: int, player, is_beating_fig=False, is_beated=False):
		self.x = x
		self.y = y
		self.color = color
		self.direction = direction
		self.player = player
		self.is_beating_fig = is_beating_fig
		self.is_beated = is_beated
		self.fig_type = "simple"
		#self.rep = self.color[0]
	
	def repr(self):
		return "t" if self.is_beated else self.color[0]
	
	def convert_2d_coords_into_1d_repr(self, coords_tpl):
		x2, y2 = coords_tpl
		coord_1d = (self.x//2 + self.y*4) * 32 + x2//2 + y2*4
		return coord_1d
		#coords = (self.x, self.y) + coords_tpl
		#return "".join(str(i) for i in coords)
		#return (str(self.x) + str(self.y) + str(x2) + str(y2))
		#return (self.x*512 + self.y*64 + x2*8 + y2)
	
	def get_simple_moves(self, board):
		x_to_left = self.x - self.direction
		x_to_right = self.x + self.direction
		y_to_forward = self.y + self.direction
		simple_moves=[]
		if (0<= x_to_left <=7) and board.is_empty(x_to_left, y_to_forward):
			simple_moves.append(self.convert_2d_coords_into_1d_repr((x_to_left, y_to_forward)))
		if (0<= x_to_right <=7) and board.is_empty(x_to_right, y_to_forward):
			simple_moves.append(self.convert_2d_coords_into_1d_repr((x_to_right, y_to_forward)))
		return simple_moves
	
	def get_beat_moves(self, board):
		#beat_funcs = (self.upright_beat_coords, self.upleft_beat_coords, self.downright_beat_coords, self.downleft_beat_coords)
		beat_coords = ((self.x+2, self.y+2), (self.x-2, self.y+2), (self.x+2, self.y-2), (self.x-2, self.y-2))
		#beat_coords_x = [self.x+2, self.x-2, self.x+2, self.x-2]
		#beat_coords_y = [self.y+2, self.y+2, self.y-2, self.y-2]
		#beated_coords = [(self.x+1, self.y+1), (self.x-1, self.y+1), (self.x+1, self.y-1), (self.x-1, self.y-1)]
		can_beat_to = (self.can_beat_to_upright, self.can_beat_to_upleft, self.can_beat_to_downright, self.can_beat_to_downleft)
		return [self.convert_2d_coords_into_1d_repr(beat_coords[i]) for i in range(4) if can_beat_to[i](board)]
		#return [beat_funcs[i]() for i in range(4) if can_beat_to[i](board)]
	
	def can_beat_to_upright(self, board):
		if (self.x > 5) or (self.y > 5):
			return False
		to_beat = board.figures[self.x + 1][self.y + 1]
		
		if to_beat.color == "empty":
			return False
		elif to_beat.color == self.color:
			return False
		elif to_beat.is_beated:
			return False
		elif board.is_empty(self.x + 2, self.y + 2):
			return True
		else:
			return False
	
	def can_beat_to_upleft(self, board):
		if (self.x < 2) or (self.y > 5):
			return False
		to_beat = board.figures[self.x - 1][self.y + 1]
		
		if to_beat.color == "empty":
			return False
		elif to_beat.color == self.color:
			return False
		elif to_beat.is_beated:
			return False
		elif board.is_empty(self.x - 2, self.y + 2):
			return True
		else:
			return False
	
	def can_beat_to_downright(self, board):
		if (self.x > 5) or (self.y < 2):
			return False
		to_beat = board.figures[self.x + 1][self.y - 1]
		
		if to_beat.color == "empty":
			return False
		elif to_beat.color == self.color:
			return False
		elif to_beat.is_beated:
			return False
		elif board.is_empty(self.x + 2, self.y - 2):
			return True
		else:
			return False
	
	def can_beat_to_downleft(self, board):
		if (self.x < 2) or (self.y < 2):
			return False
		to_beat = board.figures[self.x - 1][self.y - 1]
		
		if to_beat.color == "empty":
			return False
		elif to_beat.color == self.color:
			return False
		elif to_beat.is_beated:
			return False
		elif board.is_empty(self.x - 2, self.y - 2):
			return True
		else:
			return False


class King():
	def __init__(self, x:int, y:int, color:str, direction: int, player, is_beating_fig=False, is_beated=False):
		self.x = x
		self.y = y
		self.color = color
		self.direction = direction
		self.is_beating_fig = is_beating_fig
		self.is_beated = is_beated
		self.fig_type = "king"
		self.player = player
		#self.rep = self.color[0]
		#self.is_touched = is_touched
	
	def repr(self):
		return "T" if self.is_beated else self.color[0].upper()
		
	def convert_2d_coords_into_1d_repr(self, coords_tpl):
		x2, y2 = coords_tpl
		coords = (self.x//2 + self.y*4) * 32 + x2//2 + y2*4
		return coords
		#return (str(self.x) + str(self.y) + str(x2) + str(y2))
		#return (self.x*512 + self.y*64 + x2*8 + y2)
	
	def get_simple_moves(self, board):
		simple_moves_directions = (self.uprigt_moves, self.upleft_moves, self.downright_moves, self.downleft_moves)
		return [move_direction_fn(board) for move_direction_fn in simple_moves_directions]
		
	def uprigt_moves(self, board):
		cell_is_empty = lambda i: board.is_empty(self.x + i, self.y + i)
		tru_range = it.takewhile(cell_is_empty, range(1,8-max(self.x, self.y)))
		return [self.convert_2d_coords_into_1d_repr((self.x + i, self.y + i)) for i in tru_range]
	
	def upleft_moves(self, board):
		cell_is_empty = lambda i: board.is_empty(self.x - i, self.y + i)
		tru_range = it.takewhile(cell_is_empty, range(1, min(self.x+1, 8-self.y)))
		return [self.convert_2d_coords_into_1d_repr((self.x - i, self.y + i)) for i in tru_range]
	
	def downright_moves(self, board):
		cell_is_empty = lambda i: board.is_empty(self.x + i, self.y - i)
		tru_range = it.takewhile(cell_is_empty, range(1, min(8-self.x, self.y+1)))
		return [self.convert_2d_coords_into_1d_repr((self.x + i, self.y - i)) for i in tru_range]
	
	def downleft_moves(self, board):
		cell_is_empty = lambda i: board.is_empty(self.x - i, self.y - i)
		tru_range = it.takewhile(cell_is_empty, range(1, min(self.x+1, self.y+1)))
		return [self.convert_2d_coords_into_1d_repr((self.x - i, self.y - i)) for i in tru_range]
	
	def get_beat_moves(self, board):
		beat_directions = (self.beats_to_upright, self.beats_to_upleft, self.beats_to_downright, self.beats_to_downleft)
		return [beat_direction(board) for beat_direction in beat_directions if beat_direction(board)]
	
	def beats_to_upright(self, board):
		can_beat_to_upright, shift = self.have_beat_to_upright_from(self.x, self.y, board)
		#end of beat may be forced by continuing beat
		if can_beat_to_upright:
			return self.get_ends_of_upright_diag(shift, board)
		else:
			return []
	
	def beats_to_upleft(self, board):
		can_beat_to_upleft, shift = self.have_beat_to_upleft_from(self.x, self.y, board)
		#end of beat may be forced by continuing beat
		if can_beat_to_upleft:
			return self.get_ends_of_upleft_diag(shift, board)
		else:
			return []
	
	def beats_to_downright(self, board):
		can_beat_to_downright, shift = self.have_beat_to_downright_from(self.x, self.y, board)
		#end of beat may be forced by continuing beat
		if can_beat_to_downright:
			return self.get_ends_of_downright_diag(shift, board)
		else:
			return []
	
	def beats_to_downleft(self, board):
		can_beat_to_downleft, shift = self.have_beat_to_downleft_from(self.x, self.y, board)
		#end of beat may be forced by continuing beat
		if can_beat_to_downleft:
			return self.get_ends_of_downleft_diag(shift, board)
		else:
			return []
	
	def get_ends_of_upright_diag(self, i, board):
		end_of_upright_diag = 8 - max(self.x, self.y)
		
		ends_of_beat = []
		forced_ends_of_beat = []
		is_forsed_mode = False
		
		for j in range(i+1, end_of_upright_diag):
			if board.is_empty(self.x + j, self.y + j):
				have_continue_beat = self.have_beat_to_upleft_from(self.x+j, self.y+j, board)[0] or self.have_beat_to_downright_from(self.x+j, self.y+j, board)[0] or self.have_beat_to_upright_from(self.x+j, self.y+j, board)[0]
				if have_continue_beat:
					is_forsed_mode = True
					forced_ends_of_beat.append(self.convert_2d_coords_into_1d_repr((self.x+j, self.y+j)))
					continue
				if not is_forsed_mode:
					ends_of_beat.append(self.convert_2d_coords_into_1d_repr((self.x+j, self.y+j)))
			else:
				break
		
		#cell_is_empty = lambda j: board.is_empty(self.x + j, self.y + j)
		#tru_range = it.takewhile(cell_is_empty, range(1,8-max(self.x, self.y)))
		
		if is_forsed_mode:
			is_forsed_mode = False
			return forced_ends_of_beat
		else:
			return ends_of_beat
	
	def get_ends_of_upleft_diag(self, i, board):
		end_of_upleft_diag = min(self.x, 7-self.y)+1
		
		ends_of_beat = []
		forced_ends_of_beat = []
		is_forsed_mode = False
		
		for j in range(i+1, end_of_upleft_diag):
			if board.is_empty(self.x - j, self.y + j):
				have_continue_beat = self.have_beat_to_upright_from(self.x-j, self.y+j, board)[0] or self.have_beat_to_downleft_from(self.x-j, self.y+j, board)[0] or self.have_beat_to_upleft_from(self.x-j, self.y+j, board)[0]
				if have_continue_beat:
					is_forsed_mode = True
					forced_ends_of_beat.append(self.convert_2d_coords_into_1d_repr((self.x-j, self.y+j)))
					continue
				if not is_forsed_mode:
					ends_of_beat.append(self.convert_2d_coords_into_1d_repr((self.x-j, self.y+j)))
			else:
				break
		
		if is_forsed_mode:
			is_forsed_mode = False
			return forced_ends_of_beat
		else:
			return ends_of_beat
	
	def get_ends_of_downright_diag(self, i, board):
		end_of_downright_diag = min(7-self.x, self.y)+1
		
		ends_of_beat = []
		forced_ends_of_beat = []
		is_forsed_mode = False
		
		for j in range(i+1, end_of_downright_diag):
			if board.is_empty(self.x + j, self.y - j):
				have_continue_beat = self.have_beat_to_upright_from(self.x+j, self.y-j, board)[0] or self.have_beat_to_downleft_from(self.x+j, self.y-j, board)[0] or self.have_beat_to_downright_from(self.x+j, self.y-j, board)[0]
				if have_continue_beat:
					is_forsed_mode = True
					forced_ends_of_beat.append(self.convert_2d_coords_into_1d_repr((self.x+j, self.y-j)))
					continue
				if not is_forsed_mode:
					ends_of_beat.append(self.convert_2d_coords_into_1d_repr((self.x+j, self.y-j)))
			else:
				break
		
		if is_forsed_mode:
			is_forsed_mode = False
			return forced_ends_of_beat
		else:
			return ends_of_beat
	
	def get_ends_of_downleft_diag(self, i, board):
		end_of_downleft_diag = min(self.x, self.y)+1
		
		ends_of_beat = []
		forced_ends_of_beat = []
		is_forsed_mode = False
		
		for j in range(i+1, end_of_downleft_diag):
			if board.is_empty(self.x - j, self.y - j):
				have_continue_beat = self.have_beat_to_upleft_from(self.x-j, self.y-j, board)[0] or self.have_beat_to_downright_from(self.x-j, self.y-j, board)[0] or self.have_beat_to_downleft_from(self.x-j, self.y-j, board)[0]
				if have_continue_beat:
					is_forsed_mode = True
					forced_ends_of_beat.append(self.convert_2d_coords_into_1d_repr((self.x-j, self.y-j)))
					continue
				if not is_forsed_mode:
					ends_of_beat.append(self.convert_2d_coords_into_1d_repr((self.x-j, self.y-j)))
			else:
				break
		
		if is_forsed_mode:
			is_forsed_mode = False
			return forced_ends_of_beat
		else:
			return ends_of_beat
	
	def have_beat_to_upright_from(self, x1, y1, board):
		falsey_tpl = (False, None)
		if (x1 > 5) or (y1 > 5):
			return falsey_tpl
		upright_limit = 7-max(x1, y1)
		
		for i in range(1, upright_limit):
			to_beat = board.figures[x1 + i][y1 + i]
			
			if to_beat.color == "empty":
				continue
		
			elif to_beat.color == self.color:
				return falsey_tpl
			
			elif to_beat.is_beated:
				return falsey_tpl
			
			elif board.is_empty(x1 + (i+1), y1 + (i+1)):
				#founded figure to beat
				#if we'll return only 'i' 
				return (True, i)
			else:
				return falsey_tpl
		return falsey_tpl
	
	def have_beat_to_upleft_from(self, x1, y1, board):
		falsey_tpl = (False, None)
		if (x1 < 2) or (y1 > 5):
			return falsey_tpl
		upleft_limit = min(x1, 7-y1)
		
		for i in range(1, upleft_limit):
			to_beat = board.figures[x1 - i][y1 + i]
			
			if to_beat.color == "empty":
				continue
			elif to_beat.color == self.color:
				return falsey_tpl
			elif to_beat.is_beated:
				return falsey_tpl
			elif board.is_empty(x1 - (i+1), y1 + (i+1)):
				#founded figure to beat
				return (True, i)
			else:
				return falsey_tpl
		return falsey_tpl
	
	def have_beat_to_downright_from(self, x1, y1, board):
		falsey_tpl = (False, None)
		if (x1 > 5) or (y1 < 2):
			return falsey_tpl
		downright_limit = min(7-x1, y1)
		
		for i in range(1, downright_limit):
			to_beat = board.figures[x1 + i][y1 - i]
			
			if to_beat.color == "empty":
				continue
			elif to_beat.color == self.color:
				return falsey_tpl
			elif to_beat.is_beated:
				return falsey_tpl
			elif board.is_empty(x1 + (i+1), y1 - (i+1)):
				#founded figure to beat
				return (True, i)
			else:
				return falsey_tpl
		return falsey_tpl
		
		
	def have_beat_to_downleft_from(self, x1, y1, board):
		falsey_tpl = (False, None)
		if (x1 < 2) or (y1 < 2):
			return falsey_tpl
		downleft_limit = min(x1, y1)
		for i in range(1, downleft_limit):
			to_beat = board.figures[x1 - i][y1 - i]
			
			if to_beat.color == "empty":
				continue
			elif to_beat.color == self.color:
				return falsey_tpl
			elif to_beat.is_beated:
				return falsey_tpl
			elif board.is_empty(x1 - (i+1), y1 - (i+1)):
				#founded figure to beat
				return (True, i)
			else:
				return falsey_tpl
		return falsey_tpl

