import sys

# https://adventofcode.com/2015/day/1

print("Advent of Code 2015 - Day 1 part 2")

dirpath = sys.path[0] + '\\'

# filename = 'test2.txt'  # 5
filename = 'input.txt'  # 1795

with open(dirpath + filename, 'r') as file:
  lst = file.read()

  for x in range(len(lst)):
    instructions_sofar = lst[:x+1]  # Use string slicing to take string upto and including current position
    up_sofar = instructions_sofar.count('(')
    down_sofar = instructions_sofar.count(')')

    # If more down than up then moving to the basement, so report and stop
    if down_sofar > up_sofar:
      print(f'\nPos x+1: {x + 1} Up  = { up_sofar } Down = { down_sofar } (Difference should be -1: {up_sofar-down_sofar }) \n')
      break
