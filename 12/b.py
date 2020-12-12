from functools import reduce

ship_x = "ship_x"
ship_y = "ship_y"
waypoint_x = "waypoint_x"
waypoint_y = "waypoint_y"


def turn_waypoint(state, direction, deg):
    if (deg == 90 and direction == "R") or (deg == 270 and direction == "L"):
        new_x = -state[waypoint_y]
        new_y = state[waypoint_x]
    if deg == 180:
        new_x = -state[waypoint_x]
        new_y = -state[waypoint_y]
    if (deg == 90 and direction == "L") or (deg == 270 and direction == "R"):
        new_x = state[waypoint_y]
        new_y = -state[waypoint_x]

    state[waypoint_x] = new_x
    state[waypoint_y] = new_y

    return state


def move_waypoint(state, direction, distance):
    if direction == "E":
        state[waypoint_x] += distance
    if direction == "S":
        state[waypoint_y] += distance
    if direction == "W":
        state[waypoint_x] -= distance
    if direction == "N":
        state[waypoint_y] -= distance

    return state


def move_to_waypoint_times(state, times):
    dx = state[waypoint_x] * times
    dy = state[waypoint_y] * times
    state[ship_x] += dx
    state[ship_y] += dy

    return state


def do_instruction(state, row):
    instruction = row[:1]
    value = int(row[1:])

    if instruction in ["R", "L"]:
        return turn_waypoint(state, instruction, value)
    elif instruction == "F":
        return move_to_waypoint_times(state, value)
    else:
        return move_waypoint(state, instruction, value)


with open("./12/real.in") as f:
    final_state = reduce(
        do_instruction,
        f.read().splitlines(),
        {
            ship_x: 0,
            ship_y: 0,
            waypoint_x: 10,
            waypoint_y: -1,
        },
    )

    assert 106860 == abs(final_state[ship_x]) + abs(final_state[ship_y])