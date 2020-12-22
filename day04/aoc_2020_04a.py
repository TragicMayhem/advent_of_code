import sys
import re

print("Advent of Code 2020 - Day 4 part 1")

dirpath = sys.path[0] + '\\'

# handle = open(dirpath + 'test.txt', 'r')
handle = open(dirpath + 'input.txt', 'r')

lines = handle.readlines()
handle.close()

# master_passport_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
# optional_passport_keys = ['cid']

current = []
passports = []
valid_passport_count = 0

data = [l.rstrip() for l in lines]

def turn_to_dict(pp):
  parts = []
  for i in pp:
    parts.extend(re.findall(r"([a-z]{3}):([a-zA-Z0-9#]+)", i))

  return dict(parts)

for line in data:
  current.extend(line.split(" "))
  if line == '':
    passports.append(turn_to_dict(current))
    current = []
else:
  passports.append(turn_to_dict(current))

# print(passports)

for p in passports:
  if len(p.keys()) == 8 or (len(p.keys()) ==7 and 'cid' not in p.keys()):
    valid_passport_count += 1

print(f"\nValid passports: {valid_passport_count} \n")