from itertools import combinations

with open('./a.in') as f:
  for n1, n2, n3 in combinations(f.readlines(), 3):
    i1 = int(n1)
    i2 = int(n2)
    i3 = int(n3)
    if i1 + i2 + i3 == 2020:
      print(i1 * i2 * i3)