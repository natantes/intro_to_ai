import common

translate = [0, 1, 0, 1, -1, 2]

def max_board(board, a=float("-inf"), b=float("inf"), a_b_pruning=False):
	current_state = common.game_status(board)
	if current_state or all(board): return translate[current_state + 2]
	
	v = float("-inf")
	for index in range(9):
		if common.get_cell(board, index // 3, index % 3) == 0:
			common.set_cell(board, index // 3, index % 3, 1)
			if a_b_pruning:
				v = max(v, min_board(list(board), a, b, True))
				if v >= b: return v
				a = max(a, v)
			else:
				v = max(v, min_board(list(board)))
			common.set_cell(board, index // 3, index % 3, 0)
	return v


def min_board(board, a=float("-inf"), b=float("inf"), a_b_pruning=False):
	current_state = common.game_status(board)
	if current_state or all(board): return translate[current_state + 2]

	v = float("inf")
	for index in range(9):
		if common.get_cell(board, index // 3, index % 3) == 0:
			common.set_cell(board, index // 3, index % 3, 2)
			if a_b_pruning:
				v = min(v, max_board(list(board), a, b, True))
				if v <= a: return v
				b = min(b, v)
			else:
				v = min(v, max_board(list(board)))
			common.set_cell(board, index // 3, index % 3, 0)
	return v

def minmax_tictactoe(board, turn):
	return translate[max_board(board)] if turn == 1 else translate[min_board(board)]

def abprun_tictactoe(board, turn):
	return translate[max_board(board, a_b_pruning=True)] if turn == 1 else translate[min_board(board, a_b_pruning=True)]