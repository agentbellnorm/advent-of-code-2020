with open('./a.in') as f:
  lines = f.readlines()
  for n1 in lines:
    for n2 in lines:
      if int(n1) + int(n2) == 2020:
        print(int(n1) * int(n2))