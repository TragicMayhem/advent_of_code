import sys

# https://adventofcode.com/2015/day/1

print("Advent of Code 2015 - Day 1 part 1")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'  # 3
filename = 'input.txt'  # 74

with open(dirpath + filename, 'r') as file:
  lst = file.read()
  up = lst.count('(')
  down = lst.count(')')
  print(f'Up= { up } Down= { down } Final floor = { up-down } \n')
  