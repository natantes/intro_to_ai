import common

HEIGHT, WIDTH = common.constants.MAP_HEIGHT, common.constants.MAP_WIDTH
starting = [-1, -1]

def df_search(map):
	found = False
	visited = set()
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

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

def bf_search(map):
	found = False;
	path, queue = [], []
	visited = set()
	queue.append(tuple(starting))
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	for y in range(HEIGHT):
		for x in range(WIDTH):
			if map[y][x] == 2:
				starting[0], starting[1] = y, x

	while queue:
		l = len(queue)

		for _ in range(l):
			y, x = queue.pop(0)

			if 0 <= y < HEIGHT and 0 <= x < WIDTH:

				if map[y][x] == 3:
					visited.add((y, x))
					found = True
					break
				
				elif map[y][x] == 0 or map[y][x] == 2:
					map[y][x] = 4

					visited.add((y, x))

					queue.append((y, x + 1))
					queue.append((y + 1, x))
					queue.append((y, x - 1))
					queue.append((y - 1, x))
					
					visited.remove((y, x))

		if found:
			break
		
	for y, x in visited:
		map[y][x] = 5

	return found
