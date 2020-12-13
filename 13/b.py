import re
import itertools


def departs(line, time):
    return (time + line[1]) % line[0] == 0


with open("./13/real.in") as f:
    start_time, notes = f.read().splitlines()
    start_time = int(start_time)
    bus_lines = []
    for i, line in enumerate(notes.split(",")):
        if line != "x":
            bus_lines.append((int(line), i))

    jump = i = bus_lines[0][0]

    # this part is stolen from the internet 🤷🏼‍♂️
    for b in bus_lines[1:]:
        while (i + b[1]) % b[0] != 0:
            i += jump
        jump *= b[0]

    assert 598411311431841 == i