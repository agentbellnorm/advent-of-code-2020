import re
import itertools


def dec_to_bin(x):
    return "{:036b}".format(x)


def bin_to_dec(x):
    return int(x, 2)


def insert(s, position, value):
    return s[:position] + value + s[position + 1 :]


def get_addresses(mask):
    masks = []
    float_positions = [m.start() for m in re.finditer("X", mask)]
    for combination in itertools.product("10", repeat=mask.count("X")):
        m = mask
        for comb_position, float_position in enumerate(float_positions):
            m = insert(m, float_position, combination[comb_position])
        masks.append(m)

    return masks


with open("./14/real.in") as f:
    mask = ""
    memory = {}
    for line in f.readlines():
        if "mask" in line:
            mask = re.search("mask = (.{36})", line).group(1)

        if "mem" in line:
            mem = re.search(r"mem\[(\d*)\] = (\d*)", line)
            addr = mem.group(1)
            addr_bin = dec_to_bin(int(addr))
            val = int(mem.group(2))

            masked_address = ""
            for i, char in enumerate(mask):
                if char == "0":
                    masked_address += addr_bin[i]
                else:
                    masked_address += char

            for address in get_addresses(masked_address):
                memory[address] = val

    assert 3706820676200 == sum(memory.values())