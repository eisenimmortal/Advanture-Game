
import numpy as np

class NeuroNet():
	def __init__(self, white_weights=None, black_weights=None):
		if white_weights is None:
			white_weights = np.zeros((192,1024)) #64-simples, 64-kings, 32-emptys, 32-beated
			white_weights = np.random.random((192,1024)) #64-simples, 64-kings, 32-emptys, 32-beated
		self.white_weights = white_weights
		'''
		if black_weights is None:
			black_weights = np.zeros((192,1024))
		'''
		#self.black_weights = black_weights
		self.black_weights = np.flip(white_weights)
		self.weights ={"white": self.white_weights, "black": self.black_weights}
		
	def get_output(self, input_vector):
		out_vector = input_vector.dot(self.weights)
	

	def get_input_vector(self, board_to_learn, move):
		x1, y1, x2, y2 = move.coords
		source = x1//2 + y1*4
		target = x2//2 + y2*4
		vectorized_out_indx = source*32 + target
		
		# true_indx = int(511.5 - move.fig_direction*(511.5 - vectorized_out_indx))
		true_indx = vectorized_out_indx
		#fig = board_to_learn.figures[x1][y1]
		
		input_vector = np.array(board_to_learn.get_binar_input_for_NN(move.fig_direction), bool)
		#learn_koef = 1 / (32 * move.amount_of_moves)
		return input_vector
		
	
	def learn(self, board_to_learn, moves_queue, winner_color, learn_method="grad_regression", learn_mult=1):
		#get move from moves queue
		temp_color = moves_queue[0].fig_color
		#gamma = sum(1 for i in moves_queue if i.beated_fig is None)
		#reward = 80 - gamma
		#print(reward)
		#learn_koef = 1/32
		for i, move in enumerate(moves_queue):
			
			if temp_color != move.fig_color:
				board_to_learn.clear_move()
				temp_color = move.fig_color
			
			x1, y1, x2, y2 = move.coords
			source = x1//2 + y1*4
			target = x2//2 + y2*4
			
			# line order number of result move (номер хода в таблице выходов)
			vectorized_out_indx = source*32 + target
		
			# true_indx = int(511.5 - move.fig_direction*(511.5 - vectorized_out_indx))
			true_indx = vectorized_out_indx
			#fig = board_to_learn.figures[x1][y1]
		
			input_vector = np.array(board_to_learn.get_binar_input_for_NN(move.fig_direction), bool)
			#learn_koef = 1 / (32 * move.amount_of_moves)

			
			if winner_color==move.fig_color:
				#print("winner_color ", move.fig_color)
				#learn_direction = 1
				learn_koef = 1 * learn_mult #/ (32) # * move.amount_of_moves)
			else:
				#print("looser_color ", move.fig_color)
				#learn_direction = -1
				learn_koef = -1 * learn_mult #/ (32) # * move.amount_of_moves)
			
			#print(move.fig_color)
#			print(learn_koef * learn_direction)
			
			#self.weights[input_vector, vectorized_out_indx] = (self.weights[input_vector, vectorized_out_indx] + learn_direction)/2 ### += ((reward) * learn_direction / 32)
			self.weights[move.fig_color][input_vector, true_indx] += learn_koef
			
			board_to_learn.handle_move((vectorized_out_indx, move.amount_of_moves))
#			board_to_learn.printout()
#			print(move.fig_color, Convert_move(vectorized_out_indx).to_note())
			
		
		#slice self.weights[:][move]

	def reverse_learn(self, board):
		pass
		#reverse learn is very difficult due to
		#represent queue of beated figures
#		for i, move in enumerate(reversed(board.moves_queue)):
#			x1, y1, x2, y2 = move.coords
#			source = x1//2 + y1*4
#			target = x2//2 + y2*4
#			vectorized_out_indx = source*32 + target
#			indx_shift = board.indx_shift[move.fig_direction][move.fig_type]
#			if not move.beated_fig is None:
#				x, y = move.beated_fig.x, move.beated_fig.y
#				indx_for_set_beated = x//2 + y*4
#				indx_for_remove_fig = i*32 + indx_for_set_empty
#				self.bin_vector_repr_for_white[indx_for_remove_fig] = 0
#				self.bin_vector_of_emptys_for_white[indx_for_set_empty] = 1
#				self.bin_vector_of_beated_for_white[indx_for_set_empty] = 0

	def draw_learn(self, board_to_learn, moves_queue, winner_color, learn_method="grad_regression", learn_mult=1):
		#get move from moves queue
		temp_color = moves_queue[0].fig_color
		#gamma = sum(1 for i in moves_queue if i.beated_fig is None)
		#reward = 80 - gamma
		#print(reward)
		#learn_koef = 1/32
		for i, move in enumerate(moves_queue):
			if temp_color != move.fig_color:
				board_to_learn.clear_move()
				temp_color = move.fig_color
			
			x1, y1, x2, y2 = move.coords
			source = x1//2 + y1*4
			target = x2//2 + y2*4
			vectorized_out_indx = source*32 + target
		
			# true_indx = int(511.5 - move.fig_direction*(511.5 - vectorized_out_indx))
			true_indx = vectorized_out_indx
			#fig = board_to_learn.figures[x1][y1]
		
			input_vector = np.array(board_to_learn.get_binar_input_for_NN(move.fig_direction), bool)
			#learn_koef = 1 / (32 * move.amount_of_moves)
			
			if winner_color==move.fig_color:
				#print("winner_color ", move.fig_color)
				#learn_direction = 1
				learn_koef = -0.1 * learn_mult #/ (32) # * move.amount_of_moves)
			else:
				#print("looser_color ", move.fig_color)
				#learn_direction = -1
				learn_koef = -0.1 * learn_mult #/ (32) # * move.amount_of_moves)
			
			#print(move.fig_color)
#			print(learn_koef * learn_direction)
			
			#self.weights[input_vector, vectorized_out_indx] = (self.weights[input_vector, vectorized_out_indx] + learn_direction)/2 ### += ((reward) * learn_direction / 32)
			self.weights[move.fig_color][input_vector, true_indx] += learn_koef
			
			board_to_learn.handle_move((vectorized_out_indx, move.amount_of_moves))
#			board_to_learn.printout()
#			print(move.fig_color, Convert_move(vectorized_out_indx).to_note())
			
		
		#slice self.weights[:][move]
		
