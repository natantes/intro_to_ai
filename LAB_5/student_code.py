import common
import collections

class variables:
	counter=0

def can_yx_be_z(sudoku, y, x, z):	
	for i in range(9):
		if (sudoku[y][i]==z):
			return False
		if (sudoku[i][x]==z):
			return False
		if(sudoku[int(y/3)*3+int(i/3)][int(x/3)*3+i%3]==z): 
			return False
	return True

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
		if 0 <= y < 9 and 0 <= x < 9:
			variables.counter += 1
			next_y, next_x = y + ((x + 1) // 9), (x + 1) % 9
			if board[y][x] == 0:
				for n in range(1, 10):
					if common.can_yx_be_z(board, y, x, n):
						board[y][x] = n
						if b(board, next_y, next_x): return True
						board[y][x] = 0
			else:
				if b(board, next_y, next_x): return True
		return False

	b(sudoku, 0, 0)
	return variables.counter

def sudoku_forwardchecking(sudoku):
    variables.counter = 0
    domains = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]

    def update_domains(board, y, x, z, remove=True):
        affected_cells = []
        for i in range(9):
            if remove:
                if z in domains[y][i]:
                    domains[y][i].remove(z)
                    affected_cells.append((y, i))
                if z in domains[i][x]:
                    domains[i][x].remove(z)
                    affected_cells.append((i, x))
            else:
                domains[y][i].add(z)
                domains[i][x].add(z)
            block_y, block_x = int(y / 3) * 3, int(x / 3) * 3
            for j in range(3):
                for k in range(3):
                    if remove:
                        if z in domains[block_y + j][block_x + k]:
                            domains[block_y + j][block_x + k].remove(z)
                            affected_cells.append((block_y + j, block_x + k))
                    else:
                        domains[block_y + j][block_x + k].add(z)
        return affected_cells

    def f(board, y, x):
        if board_solved(board):
            return True
        if 0 <= y < 9 and 0 <= x < 9:
            variables.counter += 1
            next_y, next_x = y + ((x + 1) // 9), (x + 1) % 9
            if board[y][x] == 0:
                for n in domains[y][x]:
                    if can_yx_be_z(board, y, x, n):
                        board[y][x] = n
                        affected_cells = update_domains(board, y, x, n)
                        if not any(not domains[i][j] for i, j in affected_cells) and f(board, next_y, next_x):
                            return True
                        board[y][x] = 0
                        update_domains(board, y, x, n, remove=False)
            else:
                if f(board, next_y, next_x):
                    return True
        return False

    f(sudoku, 0, 0)
    return variables.counter