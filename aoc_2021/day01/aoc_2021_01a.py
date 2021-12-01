import sys
from pprint import pprint

# https://adventofcode.com/2021/day/1

print("Advent of Code 2021 - Day 1a")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


filename = 'test.txt'  # 7 
filename = 'input.txt'  # 1195 

total = 0
prev = 0

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')   #  Read each line (split \n) and form a list of strings
  lst = [int(n) for n in lst]

  for x in lst[1:]:
    total = total +1 if (x > prev) else total 
    prev = x
  
print("Total increase is", total)  
