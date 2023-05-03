import common

def drone_flight_planner(map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
    actions = [
        (common.constants.SOFF, 1, 0, 1),
        (common.constants.WOFF, 0, -1, 1),
        (common.constants.NOFF, -1, 0, 1),
        (common.constants.EOFF, 0, 1, 1),
        (common.constants.SON, 1, 0, 2),
        (common.constants.WON, 0, -1, 2),
        (common.constants.NON, -1, 0, 2),
        (common.constants.EON, 0, 1, 2),
    ]

    def is_valid(x, y):
        return 0 <= x < 6 and 0 <= y < 6

    def transition(state, action, cost):
        x, y = state
        dx, dy, energy_cost = action

        next_x = x + dx
        next_y = y + dy

        if not is_valid(next_x, next_y):
            return (x, y, cost + battery_drop_cost * energy_cost)

        if map[next_y][next_x] == common.constants.RIVAL:
            return (x, y, cost - dronerepair_cost)

        if map[next_y][next_x] == common.constants.CUSTOMER:
            return (x, y, cost + delivery_fee)

        return (next_x, next_y, cost + battery_drop_cost * energy_cost)

    def bellman_update(x, y):
        if map[y][x] == common.constants.RIVAL or map[y][x] == common.constants.CUSTOMER:
            return values[y][x], policies[y][x]

        best_value = float('-inf')
        best_policy = common.constants.EXIT

        for action in actions:
            action_value = 0
            expected_value = 0

            for prob, dx, dy in [(0.7, *action[1:3]), (0.15, -action[2], action[1]), (0.15, action[2], -action[1])]:
                next_x, next_y, cost = transition((x, y), (dx, dy, action[3]), 0)
                action_value += prob * (cost + discount * values[next_y][next_x])

            if action_value > best_value:
                best_value = action_value
                best_policy = action[0]

        return best_value, best_policy

    epsilon = 1e-5
    while True:
        delta = 0

        for y in range(6):
            for x in range(6):
                new_value, new_policy = bellman_update(x, y)

                delta = max(delta, abs(values[y][x] - new_value))
                values[y][x] = new_value
                policies[y][x] = new_policy

        if delta < epsilon:
            break

    return values[0][0]

