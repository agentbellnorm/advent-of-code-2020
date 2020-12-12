def is_taken(row, index):
    return 0 <= index < len(row) and row[index] == "#"


def is_open(row, index):
    return 0 <= index < len(row) and row[index] == "L"


def get_row(seats, row_numer):
    if 0 <= row_numer < len(seats):
        return seats[row_numer]

    return "".join([char * 10 for char in "."])


def get_adjacent(x, y):
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]


def count_taken_adj(seatmap, x, y):
    n = 0
    for adj_x, adj_y in get_adjacent(x, y):
        if is_taken(get_row(seatmap, adj_y), adj_x):
            n += 1
    return n


def next_seat_map(seatmap):
    rows = seatmap.splitlines()
    new_seat_map = []
    for y in range(len(rows)):
        new_row = ""
        for x in range(len(rows[y])):
            taken_adj = count_taken_adj(rows, x, y)
            if is_open(rows[y], x) and taken_adj == 0:
                new_row = new_row + "#"
            elif is_taken(rows[y], x) and taken_adj >= 4:
                new_row = new_row + "L"
            else:
                new_row = new_row + rows[y][x]
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

    assert 2329 == current.count("#")
