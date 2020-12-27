import sys
from pprint import pprint

print("Advent of Code 2020 - Day X part 1")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'
filename = 'input.txt'

accumulator = 0

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')
  lst = [x.split() for x in lst]
  lst = [[x[0], int(x[1])] for x in lst]

  pprint(lst)

  pointer = 0 
  visited = []

  while pointer not in visited:
    visited.append(pointer)
   
    if lst[pointer][0] == 'nop':
      pointer += 1
    elif lst[pointer][0] == 'jmp':
      pointer += lst[pointer][1]
    elif lst[pointer][0] == 'acc':    
      accumulator += lst[pointer][1]
      pointer += 1
    
    # print("  pointer is now", pointer, "already visited", visited, "accumulator =", accumulator)

print("\nFinal - pointer:", pointer, " accumulator:", accumulator)
