
from Figures import Empty, Simple, King
import itertools as it
import heapq as hq
import numpy as np

#best way to represent and analyze different boards:
#	positions of white, black draughts and checker-kings must be presented as binar number

#	it must be 5 binar arrays, which will descript one board-position:
#		empty cells
#		white checkers
#		black checkers
#		white kings
#		black kings

#Solve must be presented as array of 1024 bin elems
#or number in range(1024) - it will be
#turn

# IMPORTANT:
# string representation of positions
# is revers of binar representations
# of positions:
#	String:
#	top for black
#	bottom for white

'''
str = input ("string")
shift = int(input ("shift"))
str2 = ""
for chrs in str:
	asccode = ord (chrs)
	ascdecode = asccode - shift
	str2 += chr(ascdecode)
print (str2)
'''

##########################

def flatten(lst):
	result = []
	for i in lst:
		if isinstance(i, list):
			result.extend(flatten(i))
		else:
			result.append(i)
	return result

def extended(lst, iterable):
	new_lst = lst[:]
	new_lst.extend(iterable)
	return new_lst

def all_of(player):
	all_simples = [(item.color[0], item.x, item.y) for item in player.simples]
	all_kings = [(item.color[0].upper(), item.x, item.y) for item in player.kings]
	all_simples.extend(all_kings)
	return all_simples

def get_coords_of_move(x1,x2,y1,y2):
	return (x1*512 + y1*64 + x2*8 + y2)

############################

board_range = range(8)

#######################

class Move:
	letters = "abcdefgh"
	octs = "01234567"
	notes = "12345678"
	
	def __init__(self, coords:tuple, amount_of_moves:int, fig_type:str, fig_color:str, fig_direction:int, beated_fig=None):
		self.coords = coords
		self.amount_of_moves = amount_of_moves
		self.fig_type = fig_type
		self.fig_color = fig_color
		self.fig_direction = fig_direction
		self.beated_fig = beated_fig
	
	def oct(self):
		if (isinstance(self.source, tuple)
		and isinstance(self.target, tuple)):
			if (all(isinstance(i, int) for i in self.source)
			and all(isinstance(i, int) for i in self.target)):
				pass
		return "".join(str(i) for i in source)


class Convert_move:
	letters = "abcdefgh"
	octs = "01234567"
	notes = "12345678"
#	note_to_oct = dict(zip(letters, nums))
#	cells.update(dict(zip(range(8), letters)))
#	oct_to_note = (dict(zip(nums, letters)))
	
	def __init__(self, raw_data):
		self.raw_data = raw_data
		#self.oct = self.to_oct()
	
	def to_oct(self):
		if self.is_oct():
			return self.raw_data
		if self.is_dec():
			dec_to_note = self.to_note()
			notes_to_octs = "".maketrans(self.letters + self.notes, self.octs*2)
			result = dec_to_note.translate(notes_to_octs)
			return result
			#oct_repr = oct(self.raw_data)[2:]
#			return oct_repr.zfill(4)
		if self.is_note:
			notes_to_octs = "".maketrans(self.letters + self.notes, self.octs*2)
			result = self.raw_data.translate(notes_to_octs)
			return result
		print("Error")
	
	def to_dec(self):
		if self.is_dec():
			return self.raw_data
		if self.is_oct():
			x1,y1,x2,y2 = self.raw_data
			print((x1,y1,x2,y2))
			return (int(x1)//2 + int(y1)*4)*32 + int(x2)//2 + int(y2)*4
			#return int(self.raw_data,8)
		if self.is_note():
			oct_repr = self.to_oct()
			x1,y1,x2,y2 = oct_repr
			return (int(x1)//2 + int(y1)*4)*32 + int(x2)//2 + int(y2)*4
			#return int(oct_repr,8)
		print("Error")
	
	def to_note(self):
		if self.is_note():
			return self.raw_data
		if self.is_oct():
			octs_to_notes_1 = "".maketrans(self.octs, self.letters)
			octs_to_notes_2 = "".maketrans(self.octs, self.notes)
			chr0 = self.raw_data[0].translate(octs_to_notes_1)
			chr1 = self.raw_data[1].translate(octs_to_notes_2)
			chr2 = self.raw_data[2].translate(octs_to_notes_1)
			chr3 = self.raw_data[3].translate(octs_to_notes_2)
#			chr0 = self.letters[int(self.raw_data[0])]
#			chr1 = str(int(self.raw_data[1])+1)
#			chr2 = self.letters[int(self.raw_data[2])]
#			chr3 = str(int(self.raw_data[3])+1)
			result = chr0 + chr1 + chr2 + chr3
			return result
		if self.is_dec():
			num = self.raw_data
			source_num, target_num = divmod(num, 32)
			y1_0, x1_0 = divmod(source_num, 8)
			y1_1, x1_1 = divmod(x1_0, 4)
			x1 = y1_1 + x1_1 * 2
			y1 = y1_1 + y1_0 * 2
			
			y2_0, x2_0 = divmod(target_num, 8)
			y2_1, x2_1 = divmod(x2_0, 4)
			x2 = y2_1 + x2_1 * 2
			y2 = y2_1 + y2_0 * 2
			
			source = self.letters[x1]+str(y1+1)
			target = self.letters[x2]+str(y2+1)
			return source+target
		print("Error")
	
	def is_dec(self):
		if isinstance(self.raw_data, (int, np.int32)):
			if 0 <= self.raw_data < 1024:
				return True
		return False
	
	def is_note(self):
		note_str = self.raw_data
		if isinstance(note_str, str):
			if ":" in note_str:
				if (set("abcdefgh").issuperset(set(note_str[::3]))
				and set("12345678").issuperset(set(note_str[1::3]))
				and set(":").issuperset(set(note_str[2::3]))
				and (len(note_str)>4)):
					return True
			
			elif (set("abcdefgh").issuperset(set(note_str[::2]))
			and set("12345678").issuperset(set(note_str[1::2]))
			and (len(note_str)==4)):
				return True
		
		return False
			
	def is_oct(self):
		oct_str = self.raw_data
		if isinstance(oct_str, str):
			if oct_str[:2]=="0o":
				oct_str = oct_str[2:]
			if (len(oct_str)<5
			and set("01234567").issuperset(set(oct_str[2:]))):
				return True
		
		return False
	
	def __str__(self):
		return self.to_note()

'''
print("\n is oct a1b2")
print(Convert_move("a1b2").is_oct())
print("\n is dec a1b2")
print(Convert_move("a1b2").is_dec())
print("\n is note a1b2")
print(Convert_move("a1b2").is_note())

print("\nnote to oct:")
print(Convert_move("a1b2").to_oct())

print("\nnote to dec")
print(Convert_move("a1b2").to_dec())

print("\nnote to note")
print(Convert_move("a1b2").to_note())


print("\n is oct 0002")
print(Convert_move("0002").is_oct())
print("\n is dec 0002")
print(Convert_move("0002").is_dec())
print("\n is note 0002")
print(Convert_move("0002").is_note())


print("\noct to oct")
print(Convert_move("0002").to_oct())

print("\noct to dec")
print(Convert_move("0002").to_dec())

print("\noct to note")
print(Convert_move("0002").to_note())

print("\n is oct 157")
print(Convert_move(157).is_oct())
print("\n is dec 157")
print(Convert_move(157).is_dec())
print("\n is note 157")
print(Convert_move(157).is_note())

print("\ndec to oct")
print(Convert_move(157).to_oct())

print("\ndec to dec")
print(Convert_move(157).to_dec())

print("\ndec to note")
print(Convert_move(157).to_note())
'''

###############################


class Player():
	def __init__(self, positions_of_simples:tuple, color:str, move_direction:int, kings = None, beating_fig = None, moved = False, must_to_beat=False):
		self.simples = [Simple(coords[0], coords[1], color, move_direction, self) for coords in positions_of_simples]
		self.color = color
		self.direction = move_direction
		
		if kings is None:
			kings = []
		self.kings = kings
		
		self.beating_fig = beating_fig
		self.is_moved = moved
		self.must_to_beat = must_to_beat
		#self.empty = [0,0,0, 0b01010101, 0b10101010, 0,0,0]
	
	def get_possible_moves(self, board):
		if self.beating_fig is None:
			return flatten(self.all_possible_beat_moves(board)) or flatten(self.all_possible_simple_moves(board))
		return flatten(self.beating_fig.get_beat_moves(board))
		
	def all_possible_beat_moves(self, board):
		beat_moves_of_simples = [simpl.get_beat_moves(board) for simpl in self.simples]
		beat_moves_of_kings = [king.get_beat_moves(board) for king in self.kings]
		return [beat_moves_of_simples, beat_moves_of_kings]
		
	def all_possible_simple_moves(self, board):
		simple_moves_of_simples = [draught.get_simple_moves(board) for draught in self.simples]
		simple_moves_of_kings = [king.get_simple_moves(board) for king in self.kings]
		return [simple_moves_of_simples, simple_moves_of_kings]
	
	def choose_the_move(self, board, neuro_net):
		input_vector = board.get_binar_input_for_NN(self.direction)
		posbl_moves = np.array(self.get_possible_moves(board))
		num_of_posbl_moves = posbl_moves.shape[0]
		#if no one posbl move
		if num_of_posbl_moves == 0:
			return None
		
		#weights of all moves (include impossible)
		dence1 = input_vector.dot(neuro_net.weights[self.color])
		#dence1 shape is (1024,1)
		
		#weights of possible moves (impossible is excluded)
		dence2 = dence1[posbl_moves]
		
		#if dence2 have negative elems
		#probabs will be calculate with
		#shift from min elem of dence2
		
		#actually this is choosing_mode selector:
		#type here "white_" to automatic
		if self.color != "white":
			max_elem = hq.nlargest(1, dence2)[-1]
			min_elem = hq.nsmallest(1, dence2)[-1] - 1
			#max_relu = np.array(np.logical_or(min_elem >= dence2,  dence2 >= max_elem), int)
			#print(max_relu)
			#probabs = np.array(dence2==max_elem, int)
			#probabs = 10**(dence2)
			probabs = dence2 - min_elem
			probabs_sum = sum(probabs)
			if probabs_sum:
				probabs_normed = probabs / probabs_sum
			else:
				probabs_normed = np.full((num_of_posbl_moves,),(1/num_of_posbl_moves))
			
			#board.printout()
			#print([Convert_move(move).to_note() for move in posbl_moves])
			#print(dence2)
			
			my_choice = np.random.choice(posbl_moves, p=probabs_normed)
			
			#print(self.color, Convert_move(my_choice).to_note())
		
		else:
			min_shift = np.min(dence2)
			temp_vect = dence2 - min_shift
			sum_temp_vect = np.sum(temp_vect)
			if sum_temp_vect:
				probabs = temp_vect/sum_temp_vect
			else:
				probabs = np.full((num_of_posbl_moves,),(1/num_of_posbl_moves))

			board.printout()
			print([Convert_move(move).to_note() for move in posbl_moves])
			print(dence2)
			
			wanna_show = True
			while wanna_show:
				is_want = input("What do you want to see? int/'b' (back move)/'sw'(show weights)")
				if "sw" in is_want:
					is_want = int(is_want[2:])
					weights_to_show = (dence1[posbl_moves[is_want]]).reshape(32,-1)
					print(weights_to_show)
				elif "b" in is_want:
					board.one_move_back() 
				elif is_want=="":
					move_indx = 0
				else:
					move_indx = int(is_want)
				break
			
			#move_indx = int(input("input number of move"))
			
			my_choice = posbl_moves[move_indx]

		#my_choice = np.random.choice(posbl_moves, p=probabs)
#		print(self.color, Convert_move(my_choice).to_note())
		#print(probabs.shape)
		#print(type(probabs[0]))
#		print(dence2)
#		
		#probabs = np.arange(1,num_of_posbl_moves+1)/sum(np.arange(1,num_of_posbl_moves+1))

		return (my_choice, num_of_posbl_moves)
	
	def choosing_mode():
		...
	
	def all_figures(self):
		all_simples = [item for item in self.simples]
		all_kings = [item for item in self.kings]
		all_simples.extend(all_kings)
		return all_simples
	
	# move draught function
	def simple_to_king(self, simpl_obj):
		new_king = King(simpl_obj.x, simpl_obj.y, simpl_obj.color, simpl_obj.direction, self, simpl_obj.is_beating_fig, simpl_obj.is_beated)
		if simpl_obj.is_beating_fig:
			self.beating_fig = new_king
		self.kings.append(new_king)
		self.simples.remove(simpl_obj)
		return new_king

