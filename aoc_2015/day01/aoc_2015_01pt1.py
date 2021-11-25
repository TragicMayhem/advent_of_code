import sys

# https://adventofcode.com/2015/day/1

print("Advent of Code 2015 - Day 1 part 1")

dir_separator = ''

if sys.platform == "linux" or sys.platform == "linux2":
  dir_separator = "/"
elif sys.platform == "darwin":
  dir_separator = "/"
elif sys.platform == "win32":
  dir_separator = "\\\\"

dirpath = sys.path[0] + dir_separator

# filename = 'test.txt'  # 3
filename = 'input.txt'  # 74

with open(dirpath + filename, 'r') as file:
  lst = file.read()
  up = lst.count('(')
  down = lst.count(')')
  print(f'Up= { up } Down= { down } Final floor = { up-down } \n')
  