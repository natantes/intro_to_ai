
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
number_locations = {}

for i, num in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 0]):
    current_row, current_col = i // 3, i % 3
    number_locations[num] = [current_row, current_col]

def calc_hscore(current_board):
    hscore = 0
    for i, num in enumerate(current_board):
        if num == 0: continue
        current_row, current_col = i // 3, i % 3
        hscore += abs(current_row - number_locations[num][0]) + abs(current_col - number_locations[num][1])
    
    return hscore

def add_states(current_depth, current_path, current_board):
    current_row, current_col, states = 0, 0, []
    for i, num in enumerate(current_board):
        if num == 0:
            current_row, current_col = i // 3, i % 3
            break
    
    for i, (dy, dx) in enumerate(directions):
        if 0 <= current_row + dy < 3  and 0 <= current_col + dx < 3:
            new_depth = current_depth + 1
            new_path = list(current_path + [i])

            old_index = (current_row)*3 + current_col
            new_index = (current_row + dy)*3 + current_col + dx

            current_board[old_index] = current_board[new_index]
            current_board[new_index] = 0

            new_board = list(current_board)
            new_f_score = calc_hscore(new_board) + new_depth

            new_num = int(''.join(map(str, new_board)))

            current_board[new_index] = current_board[old_index] 
            current_board[old_index] = 0

            states.append([new_f_score, new_num, new_depth, new_path, new_board])
    
    return states

#astar search
def astar(board):
    nodes_expanded = 0
    visited = set()
    queue = [[0, int(''.join(map(str, board))), 0, [], board]]
    while queue:
        queue.sort(key=lambda x: (x[0], -x[1]))
        nodes_expanded += 1
        current = queue.pop(0)
        current_fn, current_num, current_depth, current_path, current_board = current
        visited.add(tuple(current_board))
        if current_board == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return [current_depth, nodes_expanded, current_path]

        new_queue = []
        for fn, num, depth, path, bd in queue:
            if current_board == bd or tuple(bd) in visited:
                continue
            new_queue.append([fn, num, depth, path, bd])

        new_states = add_states(current_depth, current_path, current_board)
        for new_state in new_states:
            _, _, _, _, bd = new_state
            if tuple(bd) not in visited:
                new_queue.append(new_state)
        queue = list(new_queue)