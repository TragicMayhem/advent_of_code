import sys

# https://adventofcode.com/2015/day/1

print("Advent of Code 2015 - Day 1 part 1")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"

# filename = 'test.txt'  # 3
filename = 'input.txt'  # 74

with open(dirpath + filename, 'r') as file:
  lst = file.read()
  up = lst.count('(')
  down = lst.count(')')
  print(f'Up= { up } Down= { down } Final floor = { up-down } \n')
  