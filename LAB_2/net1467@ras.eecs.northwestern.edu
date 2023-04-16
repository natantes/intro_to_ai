QUEENS = 10
directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

def get_pairs(board, queen, pairs):
	for dy, dx in directions:
		current_y, current_x = queen
		current_y += dy
		current_x += dx
		while 0 <= current_x < len(board[0]) and 0 <= current_y < len(board):
			if board[current_y][current_x] == 1:
				pairs.add((queen[0], queen[1], current_y, current_x))
			current_x += dx
			current_y += dy
	
	return pairs

def full_board_counter(board):
	pairs = set()
	for y in range(QUEENS):
		for x in range(QUEENS):
			if board[y][x] == 1:
				for p_1, p_2, p_3, p_4 in get_pairs(board, [y, x], set()):
					if (p_1, p_2, p_3, p_4) not in pairs and (p_3, p_4, p_1, p_2) not in pairs:
						pairs.add((p_1, p_2, p_3, p_4))
	
	return len(pairs)

def choose_queen(board):
	queens = []
	old_count = full_board_counter(board)
	for y in range(QUEENS):
		for x in range(QUEENS):
			if board[y][x] == 1:
				next_choice = potential_difference(board, (y, x), old_count)
				if not next_choice:
					continue
				new_best, new_choice = next_choice
				queens.append([new_best, x, [y, x], new_choice])
	
	queens.sort(key=lambda x: (x[0], -x[1]), reverse=True)
	return queens[0] if queens else None

def potential_difference(board, queen, old_count):
	board[queen[0]][queen[1]] = 0
	column = queen[1]
	choices = []

	for y in range(QUEENS):
		board[y][column] = 1
		choices.append([full_board_counter(board), y, [y, column]])
		board[y][column] = 0

	choices.sort(key=lambda x: (x[0], x[1]))
	new_best_count = choices[0][0]
	board[queen[0]][queen[1]] = 1
	if new_best_count == old_count:
		return 
	return [old_count - new_best_count, [choices[0][2][0], choices[0][2][1]]]


def gradient_search(board):
	while True:
		queen = choose_queen(board)
		if not queen:
			return full_board_counter(board) == 0
		_, _, old_pos, new_pos = queen
		board[old_pos[0]][old_pos[1]] = 0
		board[new_pos[0]][new_pos[1]] = 1