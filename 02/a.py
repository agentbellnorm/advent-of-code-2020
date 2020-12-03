import re

valid = 0

with open("./a.in") as f:
    for line in f.readlines():
        match = re.search("(\d*)-(\d*) ([a-z]): ([a-z]*)", line)
        min = int(match.group(1))
        max = int(match.group(2))
        char = str(match.group(3))
        chars = str(match.group(4))
        # print('min: {}, max: {}, char: {}, chars: {}'.format(min, max, char, chars))

        if chars.count(char) >= min and chars.count(char) <= max:
            valid += 1

    print(valid)
