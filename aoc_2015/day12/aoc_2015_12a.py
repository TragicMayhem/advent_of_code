import sys
import re
from pprint import pprint

# https://adventofcode.com/2015/day/12

print("Advent of Code 2015 - Day 12 part 1")

dirpath = sys.path[0] + '\\'

filename = 'test.json'  # 23
# filename = 'input.json'  # 191164

digits_re =  re.compile(r'-?\d+')

with open(dirpath + filename, 'r') as file:
  text = file.read()
  numbers = [int(s) for s in  digits_re.findall(text)]

pprint(numbers)
print("Sum of numbers is", sum(numbers))