import common

def df_search_2(map):

	found = False

	for i in range(common.constants.MAP_HEIGHT - 1):
		for j in range(common.constants.MAP_WIDTH - 1):
			if map[i][j] == 2:
				start = (i, j)
				stack = [start]

	path = {start: [start]}

	while len(stack) > 0:
		current = stack.pop()
		y, x = current[0], current[1]
		if map[y][x] == 3:
			for i in path[(y, x)]:
				map[i[0]][i[1]] = 5
			return True
		map[y][x] = 4

		if y > 0 and map[y-1][x] != 1 and map[y-1][x] != 4:
			stack.append((y-1, x))
			path[(y-1, x)] = path[current] + [(y-1, x)]

		if x > 0 and map[y][x-1] != 1 and map[y][x-1] != 4:
			stack.append((y, x-1))
			path[(y, x-1)] = path[current] + [(y, x-1)]

		if y < common.constants.MAP_HEIGHT - 1 and map[y+1][x] != 1 and map[y+1][x] != 4:
			stack.append((y+1, x))
			path[(y+1, x)] = path[current] + [(y+1, x)]

		if x < common.constants.MAP_WIDTH - 1 and map[y][x + 1] != 1 and map[y][x + 1] != 4:
			stack.append((y, x+1))
			path[(y, x+1)] = path[current] + [(y, x+1)]

	return found

def bf_search_2(map):

	found = False

	for i in range(common.constants.MAP_HEIGHT - 1):
		for j in range(common.constants.MAP_WIDTH - 1):
			if map[i][j] == 2:
				start = (i, j)
				queue = [start]

	path = {start: [start]}

	while len(queue) > 0:
		current = queue.pop(0)
		y, x = current[0], current[1]
		if map[y][x] == 3:
			for i in path[(y, x)]:
				map[i[0]][i[1]] = 5
			return True
		map[y][x] = 4

		if x < common.constants.MAP_WIDTH - 1 and map[y][x+1] != 1 and map[y][x+1] != 4:
			queue.append((y, x+1))
			path[(y, x+1)] = path[current] + [(y, x+1)]

		if y < common.constants.MAP_HEIGHT - 1 and map[y+1][x] != 1 and map[y+1][x] != 4:
			queue.append((y+1, x))
			path[(y+1, x)] = path[current] + [(y+1, x)]

		if x > 0 and map[y][x-1] != 1 and map[y][x-1] != 4:
			queue.append((y, x-1))
			path[(y, x-1)] = path[current] + [(y, x-1)]

		if y > 0 and map[y-1][x] != 1 and map[y-1][x] != 4:
			queue.append((y-1, x))
			path[(y-1, x)] = path[current] + [(y-1, x)]

	return found
