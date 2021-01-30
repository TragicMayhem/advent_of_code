import sys
import re
from pprint import pprint

# https://adventofcode.com/2015/day/8

print("Advent of Code 2015 - Day 8 part 2")

dirpath = sys.path[0] + '\\'

# Disregarding the whitespace in the file, 
# what is the number of characters of code for string literals minus the number of characters # in memory 
# for the values of the strings in total for the entire file?

# filename = 'test.txt'  # (6 + 9 + 16 + 11 = 42)  42 - 23 = 19
# filename = 'test2.txt'  # 75
filename = 'input.txt'  # 2085

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')

  tot_space = 0

  for l in lst:
    tmp = l
    tmp = tmp.replace('\\x', '^x')   # 'Cheat' replace this with char not there, replace rest then change this back with extra \
    tmp = tmp.replace('\\', '\\\\').replace('"','\\"')
    tmp = tmp.replace('^x', '\\\\x')
    tmp = '"' + tmp + '"'

    tot_space += len(tmp) - len(l)

print("Answer:", tot_space)