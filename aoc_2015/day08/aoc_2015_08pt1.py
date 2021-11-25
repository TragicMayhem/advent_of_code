import sys
import re
from pprint import pprint

# https://adventofcode.com/2015/day/8

print("Advent of Code 2015 - Day 8 part 1")

dirpath = sys.path[0] + '\\'

# Disregarding the whitespace in the file, 
# what is the number of characters of code for string literals minus the number of characters # in memory 
# for the values of the strings in total for the entire file?

filename = 'test.txt'  # string chars (2 + 5 + 10 + 6 = 23) in memory (0 + 3 + 7 + 1 = 11) so 23 - 11 = 12
filename = 'test2.txt'  # 50
filename = 'input.txt'  # 1350

# (\\\\)  - Expression matches \\  = 2 char-space
# (\\x[0-9a-z]{2})  - Expression matches \x and 2 chars/digits [0-9a-z]  = 4 char-space
# (\\\")  - Expression matches \"  = 2 char-space
# (\\\\)|(\\x[\w]{2})|(\\\")   - Match all but group each component pattern
# (\\\\|\\x[\w]{2}|\\\")   - Match all but just each one separately, so get a single list

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')

  tot_space = 0
  tot_char_len = 0

  for l in lst:
    tmp = l[1:-1]
    
    find_escaped = re.findall(r"(\\\\|\\x[\w]{2}|\\\")", l)  
    # print(find_escaped)

    tot_space += len(l)
    tot_char_len += len(l) - 2 - sum(len(f) for f in find_escaped) + len(find_escaped)

print("Answer:", tot_space - tot_char_len)