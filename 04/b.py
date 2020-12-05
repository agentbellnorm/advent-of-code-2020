import re

validations = {
    "byr": lambda val: 1920 <= int(val) <= 2002,
    "iyr": lambda val: 2010 <= int(val) <= 2020,
    "eyr": lambda val: 2020 <= int(val) <= 2030,
    "hgt": lambda val: re.search("^1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in$", val),
    "hcl": lambda val: re.search("^#[0-9a-f]{6}$", val),
    "ecl": lambda val: re.search("^amb|blu|brn|gry|grn|hzl|oth$", val),
    "pid": lambda val: re.search("^[0-9]{9}$", val),
}

with open("./04/real.in") as f:
    passports = f.read().split("\n\n")
    valid = len(passports)
    for passport in passports:
        for field in validations:
            match = re.search("{}:([a-z0-9#]*)".format(field), passport)
            if not match or not validations.get(field)(match.group(1)):
                valid -= 1
                break

    print(valid)  # 145
