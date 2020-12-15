pre = "pre"
prepre = "prepre"


def init(spoken, starting_numbers):
    for i, number in enumerate(starting_numbers):
        spoken[number] = {pre: i + 1}


def has_only_pre(spoken, number):
    return pre in spoken[number] and prepre not in spoken[number]


def append_or_create(d, number, turn):
    if number not in d:
        d[number] = {pre: turn}
    else:
        d[number][prepre] = d[number][pre]
        d[number][pre] = turn


starting_numbers = [1, 20, 11, 6, 12, 0]
spoken = {}
init(spoken, starting_numbers)
last_spoken = starting_numbers[-1]
starting_turn = len(starting_numbers) + 1

for turn in range(starting_turn, 30000000 + 1):
    if last_spoken not in spoken or has_only_pre(spoken, last_spoken):
        last_spoken = 0
    else:
        last_spoken = spoken[last_spoken][pre] - spoken[last_spoken][prepre]

    append_or_create(spoken, last_spoken, turn)

assert 10652 == last_spoken
