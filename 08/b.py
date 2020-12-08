import re
from copy import deepcopy
from operator import add, sub

calc = {"+": add, "-": sub}


def halt_at_loop(ins, acc, idx):
    if idx == len(ins):
        return acc
    if not ins[idx]:
        return -1 * acc

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
        instructions.append([parsed.group(1), parsed.group(2), int(parsed.group(3))])

    final_acc = None

    for idx, instruction in enumerate(instructions):
        op = instruction[0]
        if op == "nop" or op == "jmp":
            alt_instructions = deepcopy(instructions)
            alt_instructions[idx][0] = "jmp" if op == "nop" else "nop"
            acc = halt_at_loop(alt_instructions, 0, 0)
            if acc > 0:
                final_acc = acc
                break

    assert final_acc == 758
