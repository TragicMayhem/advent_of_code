# https://adventofcode.com/2021/day/1

import sys

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"

print("Advent of Code 2021 - Day 1b")

filename = 'test.txt'  # 5 
filename = 'input.txt'  #  1235

total = 0
prev = 0

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')   #  Read each line (split \n) and form a list of strings
  lst = [int(n) for n in lst]

  for i, x in enumerate(lst[:-3]):
    next = sum(lst[i:i+3])
    total = total + 1 if (next > prev) else total
    prev = next

print("Total increase is", total)  
