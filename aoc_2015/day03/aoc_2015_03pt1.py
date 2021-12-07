# https://adventofcode.com/2015/day/3

from pprint import pprint
import pathlib

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt' 
input_test2 = script_path / 'test2.txt' 
input = script_path / 'input.txt'  
 
file_in = input#_test

# filename = 'test.txt'  # 2 
# filename = 'test2.txt'  # 4
# filename = 'input.txt'  # 2592

# Begins by delivering a present to the house at his starting location
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<). 
# After each move, he delivers another present to the house at his new location.

x_pos = y_pos = 0

locations = {'0,0': 1}

with open(file_in, 'r') as file:
  directions = list(file.read())  
  for dir in directions:
    if dir == '^': y_pos += 1
    if dir == 'v': y_pos -= 1
    if dir == '<': x_pos -= 1
    if dir == '>': x_pos += 1
   
    loc = str(x_pos) + ',' + str(y_pos)
    locations[loc] = locations.get(loc, 0) + 1
    
# pprint(locations)

print(f'\nTotal houses visited at least once = {len(locations)}\n')

