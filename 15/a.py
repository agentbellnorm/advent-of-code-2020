def append_or_create(d, key, val):
    if key in d:
        d[key].append(val)
    else:
        d[key] = [val]


starting_numbers = [1, 20, 11, 6, 12, 0]
# starting_numbers = [0, 3, 6]

spoken = {}
for i, number in enumerate(starting_numbers):
    spoken[number] = [i + 1]

last_spoken = starting_numbers[-1]
starting_turn = len(starting_numbers) + 1

for turn in range(starting_turn, 30000000 + 1):
    if last_spoken not in spoken:
        spoken[last_spoken] = [turn]
        last_spoken = 0
    elif len(spoken[last_spoken]) == 1:
        last_spoken = 0
    else:
        prepre, pre = spoken[last_spoken][-2:]
        last_spoken = pre - prepre

    append_or_create(spoken, last_spoken, turn)

assert 10652 == last_spoken
