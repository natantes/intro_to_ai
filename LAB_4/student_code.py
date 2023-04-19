import common

def max_board(board):
	current_state = common.game_status(board)
	if current_state:
		return current_state
	elif all(board):
		return common.constants.NONE
	v = float("-inf")
	for index in range(9):
		row, col = index // 3, index % 3
		if common.get_cell(board, row, col) == 0:
			common.set_cell(board, row, col, 1)
			v = max(v, min_board(list(board)))
			common.set_cell(board, row, col, 0)
	return v

def min_board(board):
	current_state = common.game_status(board)
	if current_state:
		return current_state
	elif all(board):
		return common.constants.NONE
	v = float("inf")
	for index in range(9):
		row, col = index // 3, index % 3
		if common.get_cell(board, row, col) == 0:
			common.set_cell(board, row, col, 2)
			v = min(v, max_board(list(board)))
			common.set_cell(board, row, col, 0)
	return v

	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

def minmax_tictactoe(board, turn):
	if turn == 1: return max_board(board)
	return min_board(board)

def abprun_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	return None
	# return common.constants.NONE
