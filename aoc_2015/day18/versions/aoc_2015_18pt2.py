import itertools
import sys
import copy
from pprint import pprint

# https://adventofcode.com/2015/day/18

print("Advent of Code 2015 - Day 18 part 2")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"

# InCOmPleTE DOESNT WORK - WHERE I STOPPED.......



# filename = 'test_part2.txt'  # 6*6 grid after 5 steps 17 lights on - when the corners dont turn off
filename = 'input.txt'  # 100*100, 100 steps corneers locked - lights on at the ends = 
# 865 too low

steps = 100

def next_state(posx, posy, grid):
  '''
    Updates lights based on neighbours status
    On: Stays on if 2 or 3 neighbours on else off.  
    Off: Turns on if 3 neighbours on, else stays off
    Edges (assume off)
    Corners are ALWAYS on (Part 2 update)

    Parameters:
      x (int): row of the grid
      y (int): column of the grid
      [][] (bool): Grid with True/False
    
    Returns:
      next state (Bool):  True (on) False (off)
  '''
  current_status = grid[posx][posy]
  neighbours = []
  
  # Part 2 for the corners always on
  coords = (posx, posy)
  if coords == (0,0) or coords == (0, grid_size-1) or coords == (grid_size-1, 0) or coords == (grid_size-1, grid_size-1):
    return True

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
  # print('x',posx, 'y',posy, 'on',lights_on, 'off',lights_off, '\n')

  if current_status and 2 <= lights_on <= 3:
    return True
  
  if not current_status and lights_on == 3:
    return True
  
  return False


with open(dirpath + filename, 'r') as file:
  
  # Prepare initial grid from input file
  
  data = file.read().split('\n')
  data = [list(d) for d in data]

  lights_grid = []
  for d in data:
    res = list(map(lambda ele: True if ele == '#' else False, d))
    lights_grid.append(res)
  grid_size = len(lights_grid)
  print("START lights on:", sum([sum(d) for d in lights_grid]))
  
  # Start iteraing

  # for step in range(steps):
  #   new_state_grid = [None] * grid_size
  #   for i in range(grid_size):
  #     tmp = []
  #     for j in range(grid_size):
  #       tmp.append(next_state(i, j, lights_grid))
  #     new_state_grid[i] = tmp
  #     # print(sum(new_state_grid[i]),new_state_grid[i])
    
  #   print(f"State {step} has {sum([sum(d) for d in new_state_grid])} lights on")
  #   lights_grid = copy.deepcopy(new_state_grid)   #new_lights = [row[:] for row in lights]??
  #   print("")
  
# 
# def corner(x, y): return (x,y) in [(0,0),(0,99),(99,0),(99,99)]
