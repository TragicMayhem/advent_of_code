import itertools
import sys
from pprint import pprint
from itertools import combinations, permutations 

# https://adventofcode.com/2015/day/17

print("Advent of Code 2015 - Day 17 part 1")
dirpath = sys.path[0] + '\\'

test = ['test.txt', 25]   # 4
puzzle = ['input.txt', 150]  # 1304

filename, target_litres = puzzle

def howtostore(target_amt, quantities):
  ways = []
  for n in range(1, target_amt):
    for combination in itertools.combinations(quantities, n):
      if sum(combination) == target_amt:
        ways.append(combination)
  return ways
 

with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')
  data = sorted([int(d) for d in data])

  possible_ways = howtostore(target_litres, data)
  print(possible_ways)

  print("\nAnswer Part 1")
  print(f'Target litres: {target_litres} using a list with {len(data)} quantities')
  print(data)
  print(f'\nPossible combinations: {len(possible_ways)}')
