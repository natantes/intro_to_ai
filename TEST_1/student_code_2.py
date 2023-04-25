QUEENS = 10

def num_attack(board):

    row_attack = 0
    queen_pos = []

    for y in range(10):
        queen = 0
        for x in range(10):
            if board[y][x] == 1:
                queen = queen + 1
                queen_pos.append((y, x))

        if queen > 1:
            while queen > 1:
                row_attack = row_attack + queen - 1
                queen = queen - 1

    d_attack = 0

    for q1 in queen_pos:
        for q2 in queen_pos:
            if q2[0] > q1[0] and q2[1] > q1[1] and ((q2[0] - q1[0]) == (q2[1] - q1[1])):
                d_attack = d_attack + 1
            if q2[0] < q1[0] and q2[1] > q1[1] and ((q1[0] - q2[0]) == (q2[1] - q1[1])):
                d_attack = d_attack + 1

    attack = row_attack + d_attack

    return attack

def gradient_search_2(board):

    if num_attack(board) == 0:
        return True

    else:
        # record the max deduction of column x
        deduction = []
        # record the y_pos that results in the max deduction of column x
        y_pos = []
        # record the previous number of attacks
        prev_attack = num_attack(board)

        for x in range(10):
            deduction_at_x = []

            # find original queen location and remove it at column x
            for y in range(10):
                if board[y][x] == 1:
                    original_y = y
                    board[original_y][x] = 0

            # move the original queen
            for y in range(10):

                # start with the first entry
                board[y][x] = 1
                deduction_at_x.append(prev_attack - num_attack(board))
                # return to all 0s
                board[y][x] = 0

            board[original_y][x] = 1

            deduction.append(max(deduction_at_x))
            y_pos.append(deduction_at_x.index(max(deduction_at_x)))

        if max(deduction) == 0:
            return False
        else:
            moved_x = deduction.index(max(deduction))
            moved_y = y_pos[moved_x]
            for y in range(10):
                board[y][moved_x] = 0
            board[moved_y][moved_x] = 1
            return(gradient_search_2(board))


# print(gradient_search([[0,0,0,0,0,0,0,0,0,0], [1,0,0,0,0,0,0,0,0,0], [0,1,0,0,1,0,0,0,0,0], [0,0,1,0,0,1,0,0,1,0],
#                  [0,0,0,0,0,0,0,1,0,0], [0,0,0,1,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0],
#                  [0,0,0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,1]]))


