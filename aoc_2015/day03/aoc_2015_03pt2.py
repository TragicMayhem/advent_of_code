# https://adventofcode.com/2015/day/3

from pprint import pprint
import pathlib

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  
input_test = script_path / 'test.txt' 
input_test2 = script_path / 'test2.txt' 
 
file_in = input#_test

# filename = 'test.txt'  # 11
# filename = 'test2.txt'  # 3
# filename = 'input.txt'  # 2360

# Begins by delivering a present to the house at his starting location
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<). 
# After each move, he delivers another present to the house at his new location.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
# then take turns moving based on instructions

santa_x = santa_y = robo_x = robo_y = 0

locations = {'0,0': 1}

santas_move = True

with open(file_in, 'r') as file:
  directions = list(file.read())  
  for dir in directions:
    if santas_move:
      pos = [santa_x, santa_y]
    else:
      pos = [robo_x, robo_y]

    if dir == '^': pos[1] += 1
    if dir == 'v': pos[1] -= 1
    if dir == '<': pos[0] -= 1
    if dir == '>': pos[0] += 1
   
    loc = str(pos[0]) + ',' + str(pos[1])
    locations[loc] = locations.get(loc, 0) + 1
    
    if santas_move:
      santa_x = pos[0]
      santa_y = pos[1]
    else:
      robo_x = pos[0]
      robo_y = pos[1]

    santas_move = not santas_move
    
# pprint(locations)

print(f'\nTotal houses visited at least once = {len(locations)}\n')

