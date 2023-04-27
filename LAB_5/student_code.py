import common
import copy

class variables:
	counter=0

def board_solved(board):
	for y, row in enumerate(board):
		for x, n in enumerate(row):
			temp = board[y][x]
			board[y][x] = 0
			if n == 0 or not common.can_yx_be_z(board, y, x, n):
				return False
			board[y][x] = temp
	return True

def sudoku_backtracking(sudoku):
	variables.counter = 0
	def b(board, y, x):
		if board_solved(board):
			return True
		if 0 <= y < 9 and 0 <= x < 9 or x == -1 and y == 0:
			next_y, next_x = y + ((x + 1) // 9), (x + 1) % 9
			if board[next_y][next_x] == 0:
				variables.counter += 1
				for n in range(1, 10):
					if common.can_yx_be_z(board, next_y, next_x, n):
						board[next_y][next_x] = n
						if b(board, next_y, next_x): return True
						board[next_y][next_x] = 0
			else:
				if b(board, next_y, next_x): return True
		return False

	b(sudoku, 0, -1)
	return variables.counter + 1

def check_domains(domain):
	for coord in domain:
		if len(domain[coord]) == 0:
			return False
	return True

# def update_domains(sudoku):
# 	domain = {}
# 	for i in range(9):
# 		for j in range(9):
# 			if sudoku[i][j] == 0:
# 				temp = []
# 				for z in range(1,10):
# 					if common.can_yx_be_z(sudoku, i, j, z):
# 						temp.append(z)		
# 				domain[(i,j)] = temp
# 	return domain

def sudoku_forwardchecking(sudoku):
	variables.counter = 0

	starting_domain = {}

	def update_domains(board, y, x, z, domains):
		for i in range(9):
			if (y, i) in domains and z in domains[(y, i)]:
				domains[(y, i)].remove(z)
			if (i, x) in domains and z in domains[(i, x)]:
				domains[(i, x)].remove(z)
			if ((y // 3) * 3 + (i // 3), (x // 3) * 3 + i % 3) in domains and z in domains[((y // 3) * 3 + (i // 3), (x // 3) * 3 + i % 3)]:
				domains[((y // 3) * 3 + (i // 3), (x // 3) * 3 + i % 3)].remove(z)
		return domains

	def f(board, y, x, domain):
		if board_solved(board):
			return True
		if 0 <= y < 9 and 0 <= x < 9:
			# for row in board:
			# 	print(row)
			# print(domain)
			# print("======================")
			next_y, next_x = y + ((x + 1) // 9), (x + 1) % 9
			if board[y][x] == 0:
				variables.counter += 1
				for n in range(1, 10):  
					if common.can_yx_be_z(board, y, x, n):
						board[y][x] = n
						new = update_domains(board, y, x, n, copy.deepcopy(domain))
						# new = update_domains(board)
						if check_domains(new):
							if f(board, next_y, next_x, copy.deepcopy(new)):
								return True
						board[y][x] = 0
			else:
				if f(board, next_y, next_x, copy.deepcopy(domain)): return True
		return False
	
	for y, row in enumerate(sudoku):
		for x, n in enumerate(row):
			if sudoku[y][x] == 0:
				starting_domain[(y, x)] = set() 
				for z in range(1,10):
					if common.can_yx_be_z(sudoku, y, x, z):
						starting_domain[(y, x)].add(z)
		
	f(sudoku, 0, 0, starting_domain)
	return variables.counter + 1
