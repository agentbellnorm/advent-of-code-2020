from itertools import zip_longest


def is_taken(row, index):
    return 0 <= index < len(row) and row[index] == "#"


def is_open(row, index):
    return 0 <= index < len(row) and row[index] == "L"


def get_row(seats, row_numer):
    if 0 <= row_numer < len(seats):
        return seats[row_numer]

    return "".join([char * 10 for char in "."])


""" def count_taken_adj(seatmap, x, y):
    n = 0
    for adj_x, adj_y in get_adjacent(x, y, len(seatmap[0]), len(seatmap)):
        if is_taken(get_row(seatmap, adj_y), adj_x):
            n += 1
    return n
 """


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

    for _x, _y in zip_longest(x, xmax), range(y, ymax), fillvalue=10000):
        print("_x: {}, _y: {}".format(_x, _y))
        opposite_y = y - (_y - y)
        opposite_x = x - (_x - x)
        if opposite_x >= 0 and _y < ymax:
            bottom_left.append((opposite_x, _y))
            horiz_left.append((opposite_x, y))

        if opposite_y >= 0 and _x < xmax:
            vertical_up.append((x, opposite_y))
            top_right.append((_x, opposite_y))

        if opposite_x >= 0 and opposite_y >= 0:
            top_left.append((opposite_x, opposite_y))

        if _x < xmax:
            horiz_right.append((_x, y))
        else:
            print(_x)

        if _y < ymax:
            bottom_right.append((_x, _y))

        if _x < xmax and _y < ymax:
            vertical_down.append((x, _y))

    to_check = []

    to_check.append(vertical_up)
    to_check.append(top_right)
    to_check.append(horiz_right)
    to_check.append(bottom_right)
    to_check.append(vertical_down)
    to_check.append(bottom_left)
    to_check.append(horiz_left)
    to_check.append(top_left)
    print("x: {}, y: {}".format(x, y))
    print("vertical_up: {}".format(vertical_up))
    print("top_right: {}".format(top_right))
    print("horiz_right: {}".format(horiz_right))
    print("bottom_right: {}".format(bottom_right))
    print("vertical_down: {}".format(vertical_down))
    print("bottom_left: {}".format(bottom_left))
    print("horiz_left: {}".format(horiz_left))
    print("top_left: {}".format(top_left))
    visible_taken = 0

    for line_of_sight in to_check:
        for x, y in line_of_sight:
            if is_taken(seatmap[y], x):
                # print("saw ({}, {})".format(x, y))
                visible_taken += 1
                break

    return visible_taken


"""     for x, y in to_check:
        if is_taken(seatmap[y], x):
            visible_taken += 1 """


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
                print("({}, {}) taken adj: {}".format(x, y, taken_adj))
                if is_open(rows[y], x) and taken_adj == 0:
                    new_row += "#"
                elif is_taken(rows[y], x) and taken_adj >= 5:
                    new_row += "L"
                else:
                    new_row += rows[y][x]
        new_seat_map.append(new_row)

    return "\n".join(new_seat_map)


with open("./11/test.in") as f:
    # print(get_adjacent(2, 2, 5, 5))
    seats = f.read()
    print(seats)
    print("\n")
    current = next_seat_map(seats)
    print(current)
""" 
    print("\n")
    current = next_seat_map(current)
    print(current)
    while True:
        next_map = next_seat_map(current)
        if current == next_map:
            break
        current = next_map

    print(current.count("#")) """