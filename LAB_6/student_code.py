import common

def truncate(n, p):
    return int(n * 10**p) / 10**p

actions = [
    (common.constants.SOFF, 1, 0, 1, [0.7, 0.15, 0.15], [1]),
    (common.constants.WOFF, 0, -1, 1, [0.7, 0.15, 0.15], [2]),
    (common.constants.NOFF, -1, 0, 1, [0.7, 0.15, 0.15], [3]),
    (common.constants.EOFF, 0, 1, 1, [0.7, 0.15, 0.15], [4])]
special_actions = [
    (common.constants.SON, 1, 0, 2, [0.8, 0.10, 0.10], [5]),
    (common.constants.WON, 0, -1, 2, [0.8, 0.10, 0.10], [6]),
    (common.constants.NON, -1, 0, 2, [0.8, 0.10, 0.10], [7]),
    (common.constants.EON, 0, 1, 2, [0.8, 0.10, 0.10], [8]),
]

def calculator(current_actions, battery_drop_cost, discount, current_values, y, x):
    analyzer = []

    for i in range(4):
        current_action, left_action, right_action = current_actions[i], current_actions[(i - 1) % 4], current_actions[(i + 1) % 4]
        choices = [current_action, left_action, right_action]
        policy, _, _, _, prob, _ = current_actions[i]

        expected_value = 0

        for p, action in zip(prob, choices):
            _, dy, dx, mulitplier, _, _ = action
            next_x, next_y = x + dx, y + dy

            if 0 <= next_x < 6 and 0 <= next_y < 6:
                expected_value += p * (-battery_drop_cost * mulitplier + discount * current_values[next_y][next_x])
            else:
                expected_value += p * (-battery_drop_cost * mulitplier + discount * current_values[y][x])

        analyzer.append([truncate(expected_value, 6), policy])

    return analyzer

def best_move(battery_drop_cost, discount, current_values, y, x):
    analyzer = calculator(actions, battery_drop_cost, discount, current_values, y, x) + calculator(special_actions, battery_drop_cost, discount, current_values, y, x)

    analyzer.sort(key=lambda x: (-x[0], x[1]))
    
    return analyzer[0][0], analyzer[0][1]

def find_delta(values, new_values):
    delta = float("-inf")
    for y in range(6):
        for x in range(6):
            delta = max(delta, abs(new_values[y][x] - values[y][x]))
    return delta

def drone_flight_planner(map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
    current_values = list(values)

    for y in range(6):
        for x in range(6):
            if map[y][x] == common.constants.RIVAL:
                current_values[y][x] = -dronerepair_cost
            elif map[y][x] == common.constants.CUSTOMER:
                current_values[y][x] = delivery_fee

    def bellman_update(current_values):
        new_values = [[0 for _ in range(6)] for _ in range(6)]

        for y in range(6):
            for x in range(6):

                if map[y][x] == common.constants.RIVAL:
                    new_values[y][x] = -dronerepair_cost
                elif map[y][x] == common.constants.CUSTOMER:
                    new_values[y][x] = delivery_fee
                else:
                    expected_value, best_policy = best_move(battery_drop_cost, discount, current_values, y, x)

                    new_values[y][x] = expected_value
                    policies[y][x] = best_policy

        return new_values

    epsilon = 1e-5
    while True:
        new_values = bellman_update(current_values)
        delta = find_delta(current_values, new_values)
        current_values = list(new_values)

        if delta < epsilon:
            break

    for y in range(6):
        for x in range(6):
            values[y][x] = current_values[y][x]
            if map[y][x] == common.constants.PIZZA:
                result = values[y][x]

    return result