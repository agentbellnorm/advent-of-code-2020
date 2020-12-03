from itertools import cycle, islice

dx = 3
trees = 0

with open("./03/a.in") as f:
    for y, line in enumerate(f.readlines()):
        trees += 1 if next(islice(cycle(line.rstrip()), y * dx, None)) is "#" else 0

print(trees)  # 228
