import re
from operator import add, sub

calc = {"+": add, "-": sub}


def halt_at_loop(ins, acc, idx):
    if not ins[idx]:
        return acc

    op, sign, diff = ins[idx]
    ins[idx] = None

    if op == "nop":
        return halt_at_loop(ins, acc, idx + 1)
    if op == "acc":
        return halt_at_loop(ins, calc[sign](acc, diff), idx + 1)
    if op == "jmp":
        return halt_at_loop(ins, acc, calc[sign](idx, diff))


with open("./08/real.in") as f:
    instructions = []
    for line in f.readlines():
        parsed = re.search("([a-z]{3}) ([+-])(\d+)", line.rstrip())
        instructions.append((parsed.group(1), parsed.group(2), int(parsed.group(3))))

    assert 1594 == halt_at_loop(instructions, 0, 0)
