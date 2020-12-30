import sys

print("Advent of Code 2020 - Day 9 part 1")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'
# filename = 'input.txt'

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n\n')   
  lst = [x.replace('\n', ' ').split() for x in lst]
