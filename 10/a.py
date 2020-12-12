with open("./10/real.in") as f:
    jolts = list(map(int, f.read().splitlines()))
    jolts.append(0)
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    one = 0
    three = 0

    for index, jolt in enumerate(jolts):
        if index == len(jolts) - 1:
            break
        next_jolt = jolts[index + 1]
        if next_jolt - jolt == 1:
            one += 1
        elif next_jolt - jolt == 3:
            three += 1

    assert one * three == 1625
