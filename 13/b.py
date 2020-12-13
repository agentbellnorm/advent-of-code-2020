import re
import itertools


def departs(line, time):
    return (time + line[1]) % line[0] == 0


with open("./13/test.in") as f:
    start_time, notes = f.read().splitlines()
    start_time = int(start_time)
    bus_lines = []
    for i, line in enumerate(notes.split(",")):
        if line != "x":
            bus_lines.append((int(line), i))

    first_line = bus_lines[0][0]
    for time in itertools.count(0, first_line):
        if all(map(lambda line: departs(line, time), bus_lines)):
            print(time)
            break