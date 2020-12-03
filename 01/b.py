from itertools import combinations

with open("./a.in") as f:
    for n1, n2, n3 in combinations(map(int, f.readlines()), 3):
        if n1 + n2 + n3 == 2020:
            print(n1 * n2 * n3)
