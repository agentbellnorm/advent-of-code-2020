from functools import reduce

heading_to_compass = {
    90: "E",
    180: "S",
    270: "W",
    0: "N",
}


def turn(state, direction, degree):
    if direction == "R":
        new_degree = state["heading"] + degree
    if direction == "L":
        new_degree = state["heading"] - degree

    state["heading"] = new_degree % 360

    return state


def move(state, direction, distance):
    if direction == "E":
        state["x"] += distance
    if direction == "S":
        state["y"] += distance
    if direction == "W":
        state["x"] -= distance
    if direction == "N":
        state["y"] -= distance

    return state


def do_instruction(state, row):
    instruction = row[:1]
    value = int(row[1:])

    if instruction in ["R", "L"]:
        return turn(state, instruction, value)
    elif instruction == "F":
        return move(state, heading_to_compass[state["heading"]], value)
    else:
        return move(state, instruction, value)


with open("./12/real.in") as f:
    final_state = reduce(
        do_instruction,
        f.read().splitlines(),
        {
            "x": 0,
            "y": 0,
            "heading": 90,
        },
    )

    assert 1457 == abs(final_state["x"]) + abs(final_state["y"])