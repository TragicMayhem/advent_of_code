import sys
import re

print("Advent of Code 2020 - Day 4 part 1")

if sys.platform == "linux" or sys.platform == "linux2":
    dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
    dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
    dirpath = sys.path[0] + "\\\\"


# handle = open(dirpath + 'test.txt', 'r')
handle = open(dirpath + "input.txt", "r")

lines = handle.readlines()
handle.close()

# master_passport_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
# optional_passport_keys = ['cid']

current = []
passports = []
valid_passport_count = 0

data = [l.rstrip() for l in lines]  # pos process every line to strip text


def turn_to_dict(pp):
    """
    function to take in string
    use regular expression to find all the numbers
    store in an list then return as a dictionary
    """
    parts = []
    for i in pp:
        parts.extend(re.findall(r"([a-z]{3}):([a-zA-Z0-9#]+)", i))

    return dict(parts)


for line in data:
    current.extend(line.split(" "))
    if line == "":
        passports.append(turn_to_dict(current))
        current = []
else:  # executes after the loop completes normally. Catches last one (not nicest way!)
    passports.append(turn_to_dict(current))

# print(passports)

# Data is now in a dictionary so can count the keys and validity in a loop/if comibination
for p in passports:
    if len(p.keys()) == 8 or (len(p.keys()) == 7 and "cid" not in p.keys()):
        valid_passport_count += 1

print(f"\nValid passports: {valid_passport_count} \n")
