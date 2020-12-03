import re

valid = 0

with open("./a.in") as f:
    for line in f.readlines():
        match = re.search("(\d*)-(\d*) ([a-z]): ([a-z]*)", line)
        p1 = int(match.group(1))
        p2 = int(match.group(2))
        char = str(match.group(3))
        chars = str(match.group(4))
        # print('p1: {}, p2: {}, char: {}, chars: {}'.format(p1, p2, char, chars))

        if (chars[p1 - 1] is char) ^ (chars[p2 - 1] is char):
            valid += 1

    print(valid)
