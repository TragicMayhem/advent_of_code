# https://adventofcode.com/2021/day/XX

import sys

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


print("Advent of Code 2021 - Day 4a")

filename = 'test.txt'  # 
#filename = 'input.txt'  #  

with open(dirpath + filename, 'r') as file:
  instr=[line.split() for line in file]

