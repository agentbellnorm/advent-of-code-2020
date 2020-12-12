from itertools import zip_longest


def is_taken(row, index):
    return 0 <= index < len(row) and row[index] == "#"


def is_open(row, index):
    return 0 <= index < len(row) and row[index] == "L"


def get_row(seats, row_numer):
    if 0 <= row_numer < len(seats):
        return seats[row_numer]

    return "".join([char * 10 for char in "."])


def count_visible_taken(seatmap, x, y):
    horiz_right = []
    horiz_left = []
    vertical_up = []
    vertical_down = []
    top_right = []
    top_left = []
    bottom_right = []
    bottom_left = []

    xmax = len(seatmap[0])
    ymax = len(seatmap)

    for _x in range(x + 1, xmax):
        horiz_right.append((_x, y))

    for _x in reversed(range(x)):
        horiz_left.append((_x, y))

    for _y in range(y + 1, ymax):
        vertical_down.append((x, _y))

    for _y in reversed(range(y)):
        vertical_up.append((x, _y))

    for _x, _y in zip_longest(range(x + 1, xmax), range(y + 1, ymax)):
        if _x is not None and _y is not None:
            bottom_right.append((_x, _y))

    for _x, _y in zip_longest(range(x + 1, xmax), reversed(range(y))):
        if _x is not None and _y is not None:
            top_right.append((_x, _y))

    for _x, _y in zip_longest(reversed(range(x)), range(y + 1, ymax)):
        if _x is not None and _y is not None:
            bottom_left.append((_x, _y))

    for _x, _y in zip_longest(reversed(range(x)), reversed(range(y))):
        if _x is not None and _y is not None:
            top_left.append((_x, _y))

    to_check = []

    to_check.append(vertical_up)
    to_check.append(top_right)
    to_check.append(horiz_right)
    to_check.append(bottom_right)
    to_check.append(vertical_down)
    to_check.append(bottom_left)
    to_check.append(horiz_left)
    to_check.append(top_left)

    visible_taken = 0

    for line_of_sight in to_check:
        for x, y in line_of_sight:
            if is_taken(seatmap[y], x):
                visible_taken += 1
                break
            elif is_open(seatmap[y], x):
                break

    return visible_taken


def next_seat_map(seatmap):
    rows = seatmap.splitlines()
    new_seat_map = []
    for y in range(len(rows)):
        new_row = ""
        for x in range(len(rows[y])):
            if rows[y][x] == ".":
                new_row += "."
            else:
                taken_adj = count_visible_taken(rows, x, y)
                if is_open(rows[y], x) and taken_adj == 0:
                    new_row += "#"
                elif is_taken(rows[y], x) and taken_adj >= 5:
                    new_row += "L"
                else:
                    new_row += rows[y][x]
        new_seat_map.append(new_row)

    return "\n".join(new_seat_map)


with open("./11/real.in") as f:
    seats = f.read()
    current = next_seat_map(seats)
    while True:
        next_map = next_seat_map(current)
        if current == next_map:
            break
        current = next_map

    assert 2138 == current.count("#")