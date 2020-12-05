import re

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0

with open("./04/real.in") as f:
    for passport in f.read().split("\n\n"):
        if all(field in passport for field in required):
            valid += 1

print(valid) # 247