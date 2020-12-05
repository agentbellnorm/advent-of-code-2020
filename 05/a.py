def bsp(l, mask):
    bit, *rest = mask
    lower = l[: len(l) // 2]
    upper = l[len(l) // 2 :]

    if not rest and bit == "0":
        return lower[0]
    if not rest and bit == "1":
        return upper[0]

    if bit == "0":
        return bsp(lower, rest)
    if bit == "1":
        return bsp(upper, rest)


with open("./05/real.in") as f:
    highest = 0
    for boarding_pass in f.readlines():
        boarding_pass = boarding_pass.rstrip()
        row_mask = boarding_pass[:7].replace("F", "0").replace("B", "1")
        row = bsp(range(128), row_mask)

        column_mask = boarding_pass[7:11].replace("L", "0").replace("R", "1")
        column = bsp(range(8), column_mask)

        seat_id = row * 8 + column
        highest = seat_id if seat_id > highest else highest

    assert highest == 832
