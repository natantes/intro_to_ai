import common

class variables:
	counter=0

def deepcopy(dictionary):
	return {key: set(dictionary[key]) for key, value in dictionary.items()}

def check_domains(domain):
	return all(len(domain[coord]) != 0 for coord in domain)

def board_solved(board):
	for y, row in enumerate(board):
		for x, n in enumerate(row):
			temp, board[y][x] = board[y][x], 0
			if n == 0 or not common.can_yx_be_z(board, y, x, n):
				return False
			board[y][x] = temp
	return True

def update_domains(board, y, x, z, domains):
	del domains[(y, x)]
	for i in range(9):
		if (y, i) in domains:
			domains[(y, i)] = set(n for n in range(1, 10) if common.can_yx_be_z(board, y, i, n))
		if (i, x) in domains:
			domains[(i, x)] = set(n for n in range(1, 10) if common.can_yx_be_z(board, i, x, n))
		if ((y // 3) * 3 + (i // 3), (x // 3) * 3 + i % 3) in domains:
			domains[((y // 3) * 3 + (i // 3), (x // 3) * 3 + i % 3)] = set(n for n in range(1, 10) if common.can_yx_be_z(board, (y // 3) * 3 + (i // 3), (x // 3) * 3 + i % 3, n))

	return domains

def solver(board, y, x, domain={}, forward_checking=False):
	if not (0 <= y < 9 and 0 <= x < 9):
		return board_solved(board)
	next_y, next_x = y + ((x + 1) // 9), (x + 1) % 9
	if board[y][x] == 0:
		variables.counter += 1
		for n in range(1, 10):
			if common.can_yx_be_z(board, y, x, n):
				board[y][x] = n
				if forward_checking:
					new_domain = update_domains(board, y, x, n, deepcopy(domain))
					if check_domains(new_domain):
						if solver(board, next_y, next_x, new_domain, forward_checking=forward_checking):
							return True
				else:
					if solver(board, next_y, next_x): return True
				board[y][x] = 0
	else:
		if solver(board, next_y, next_x, domain, forward_checking=forward_checking): return True
	return False

def sudoku_backtracking(sudoku):
	variables.counter = 0
	solver(sudoku, 0, 0)
	return variables.counter + 1

def sudoku_forwardchecking(sudoku):
	variables.counter, starting_domain = 0, {}
	
	for y, row in enumerate(sudoku):
		for x, n in enumerate(row):
			if sudoku[y][x] == 0:
				starting_domain[(y, x)] = set() 
				for z in range(1,10):
					if common.can_yx_be_z(sudoku, y, x, z):
						starting_domain[(y, x)].add(z)
		
	solver(sudoku, 0, 0, starting_domain, forward_checking=True)
	return variables.counter + 1