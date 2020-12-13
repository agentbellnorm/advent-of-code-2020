import re
import itertools


def departs(line, time):
    line_number, offset = line
    return (time + offset) % line_number == 0


with open("./13/test.in") as f:
    start_time, notes = f.read().splitlines()
    start_time = int(start_time)
    bus_lines = []
    for i, line in enumerate(notes.split(",")):
        if line != "x":
            bus_lines.append((int(line), i))
    print(bus_lines)

    result = None
    for time in itertools.count(int(start_time)):
        if all(map(lambda line: departs(line, time), bus_lines)):
            print(time)
            break