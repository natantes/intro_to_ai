import common

# Constants
HEIGHT, WIDTH = common.constants.MAP_HEIGHT, common.constants.MAP_WIDTH
starting = [-1, -1]

# DFS
def df_search_1(map):
	found = False
	visited = set()

	for y in range(HEIGHT):
		for x in range(WIDTH):
			if map[y][x] == 2:
				starting[0], starting[1] = y, x

	def dfs(y, x):
		if 0 <= y < HEIGHT and 0 <= x < WIDTH:
			if map[y][x] == 3:
				visited.add((y, x))
				return True
			
			elif map[y][x] == 0 or map[y][x] == 2:
				map[y][x] = 4

				local_found = False
				visited.add((y, x))

				local_found = dfs(y, x + 1) or dfs(y + 1, x) or dfs(y, x - 1) or dfs(y - 1, x)

				if local_found: 
					return True
				
				visited.remove((y, x))

		return False

	found = dfs(starting[0], starting[1])

	for y, x in visited:
		map[y][x] = 5

	return found


# BFS
def bf_search_1(map):
	found = False
	path, queue, final_path = [], [], []
	queue.append([[starting[0]], [starting[1]], path])

	for y in range(HEIGHT):
		for x in range(WIDTH):
			if map[y][x] == 2:
				starting[0], starting[1] = y, x

	while queue:
		l = len(queue)

		for _ in range(l):
			y, x, path = queue.pop(0)
			y = y[0]
			x = x[0]

			if 0 <= y < HEIGHT and 0 <= x < WIDTH:
				path.append((y, x))

				if map[y][x] == 3:
					final_path = path
					found = True
					break
				
				elif map[y][x] == 0 or map[y][x] == 2:
					map[y][x] = 4


					queue.append([[y], [x + 1], list(path)])
					queue.append([[y + 1], [x], list(path)])
					queue.append([[y], [x - 1], list(path)])
					queue.append([[y - 1], [x], list(path)])					

		if found:
			break
	
	for y, x in final_path:
		map[y][x] = 5

	return found