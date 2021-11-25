import sys

# https://adventofcode.com/2016/day/3

print("Advent of Code 2016 - Day 3 part 1")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'  #
filename = 'input.txt'  # 

impossible = []
valid = []


with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')  # Read file make list bu splitting on new line \n
  data = [' '.join(d.split()).split() for d in data] # Splits/rejoins (to replace the multiple spaces), the splits into list
  data = [[int(i) for i in d] for d in data]
