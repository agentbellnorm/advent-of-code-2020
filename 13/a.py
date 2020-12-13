import re
import itertools


def departs(line, time):
    return time % line == 0


with open("./13/real.in") as f:
    start_time, notes = f.read().splitlines()
    start_time = int(start_time)
    bus_lines = list(map(int, filter(lambda x: x, re.findall("\d*", notes))))

    result = None
    for time in itertools.count(int(start_time)):
        departure = next((line for line in bus_lines if departs(line, time)), None)
        if departure:
            result = (time - start_time) * departure
            break

    assert 2095 == result
