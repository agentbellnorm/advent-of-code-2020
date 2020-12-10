with open("./10/real.in") as f:
    jolts = list(map(int, f.read().splitlines()))
    jolts.append(0)
    jolts.sort()
    jolts.reverse()

    outlet = jolts[0] + 3

    paths_to_outlet = {}

    for jolt in jolts:
        paths_to_outlet[jolt] = 0

    paths_to_outlet[jolts[0]] = 1

    for jolt in jolts[1:]:
        possible_jumps = filter(
            lambda jump: (jolt + jump) in paths_to_outlet.keys(), [1, 2, 3]
        )
        for jump in possible_jumps:
            paths_to_outlet[jolt] += paths_to_outlet[jolt + jump]

    assert paths_to_outlet[0] == 3100448333024
