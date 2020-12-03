from itertools import cycle, islice

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

total_trees = 1

with open("./03/a.in") as f:
    for dx, dy in slopes:
        x, trees = 0, 0
        for y, line in enumerate(f.readlines()):
            is_tree = next(islice(cycle(line.rstrip()), x, None)) is "#"
            moving_x = y % dy is 0
            if is_tree and moving_x:
                trees += 1
            if moving_x:
                x += dx
        total_trees *= trees
        f.seek(0)

print(total_trees)  # 6818112000
