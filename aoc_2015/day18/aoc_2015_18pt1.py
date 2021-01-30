import itertools
import sys
import copy
from pprint import pprint

# https://adventofcode.com/2015/day/18

print("Advent of Code 2015 - Day 18 part 1")
dirpath = sys.path[0] + '\\'

filename = 'test_part1.txt'  # 6*6 grid after 4 steps 4 lights on
filename = 'input.txt'  # 821 lights on after 100 steps in a 100*100 grid

steps = 100

def next_state(posx, posy, grid):
  '''
    Updates lights based on neighbours status
    On: Stays on if 2 or 3 neighbours on else off.  
    Off: Turns on if 3 neighbours on, else stays off
    Edges (assume off)

    Parameters:
      x (int): row of the grid
      y (int): column of the grid
      [][] (bool): Grid with True/False

    Returns:
      next state (Bool):  True (on) False (off)
  '''
  current_status = grid[posx][posy]
  neighbours = []
  
  for x in range(posx-1, posx+2):
    if x < 0 or x > grid_size-1:
      continue
    for y in range(posy-1, posy+2):
      if y < 0 or y > grid_size-1 or (posx, posy) == (x, y):
        continue
      neighbours.append((x,y))

  neighbours_state = []
  for x, y in neighbours:
    neighbours_state.append(grid[x][y])
  
  lights_on = sum(neighbours_state)
  lights_off = len(neighbours_state) - lights_on

  # print(neighbours)
  # print(neighbours_state)
  # print(lights_on, lights_off)

  if current_status and 2 <= lights_on <= 3:
    return True
  
  if not current_status and lights_on == 3:
    return True
  
  return False


with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')
  data = [list(d) for d in data]

  lights_grid = []
  for d in data:
    res = list(map(lambda ele: True if ele == '#' else False, d))
    lights_grid.append(res)

  # print(lights_grid)
  grid_size = len(lights_grid)
  print("START lights on:", sum([sum(d) for d in lights_grid]))

  for step in range(steps):
    new_state_grid = [None] * grid_size
    for i in range(grid_size):
      tmp = []
      for j in range(grid_size):
        tmp.append(next_state(i, j, lights_grid))
      new_state_grid[i] = tmp
      # print(new_state_grid[i])
    
    print(f"State {step} has {sum([sum(d) for d in new_state_grid])} lights on")
    lights_grid = copy.deepcopy(new_state_grid)
    print("")
  

