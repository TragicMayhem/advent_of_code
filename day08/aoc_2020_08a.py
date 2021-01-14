import sys
from pprint import pprint

print("Advent of Code 2020 - Day 8 part 1")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'  # 5
# filename = 'input.txt'  # 2051


with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')  # Read file make list bu splitting on new line \n
  lst = [x.split() for x in lst]  # Split each string in the list on default (space) to make a list of lists
  lst = [[x[0], int(x[1])] for x in lst]  # Convert the list to string and integer

  pprint(lst)

  accumulator = 0
  pointer = 0  # Start at the beginning, will point to next instruction
  visited = []  # Store the positions visited to check against and locate the issue

  # Note: This assumes the input will cause a problem (as it has an infinte loop in the instrctions)
  while pointer not in visited:
    visited.append(pointer)  # Add the current position to visited list
   
    if lst[pointer][0] == 'nop':
      pointer += 1

    elif lst[pointer][0] == 'jmp':
      pointer += lst[pointer][1]

    elif lst[pointer][0] == 'acc':    
      accumulator += lst[pointer][1]
      pointer += 1
    
    # print("  pointer is now", pointer, "already visited", visited, "accumulator =", accumulator)

print("\nFinal - pointer:", pointer, " accumulator:", accumulator)
