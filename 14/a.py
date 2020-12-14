import re


def dec_to_bin(x):
    return "{:036b}".format(x)


def bin_to_dec(x):
    return int(x, 2)


with open("./14/real.in") as f:
    mask = ""
    memory = {}
    for line in f.readlines():
        if "mask" in line:
            mask = re.search("mask = (.{36})", line).group(1)

        if "mem" in line:
            mem = re.search(r"mem\[(\d*)\] = (\d*)", line)
            addr = mem.group(1)
            val = int(mem.group(2))
            val_bin = dec_to_bin(val)

            res = ""
            for i, char in enumerate(mask):
                if char == "X":
                    res += val_bin[i]
                else:
                    res += char

            memory[addr] = bin_to_dec(res)

    assert 14925946402938 == sum(memory.values())