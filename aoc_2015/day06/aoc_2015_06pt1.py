import sys
import re
from pprint import pprint

# https://adventofcode.com/2015/day/6

print("Advent of Code 2015 - Day 6 part 1")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'  # 1,000,000 - 1,000 - 4 = 998,996
filename = 'input.txt'  # 400,410  (Runs slowly!)

# Grid = 0,0 to 999,999
# Input: (turn on|turn off|togggle) x1,y1 through x2,y2

grid = [[0 for j in range(1000)] for i in range(1000)]


def update_lights(change, st, en):
  counter = 0
  st_x, st_y = map(int, st.split(','))
  en_x, en_y = map(int, en.split(','))

  for a in range(st_x, en_x+1):
    for b in range(st_y, en_y+1):
      if instr == 'turn on':
        grid[a][b] = 1
      elif instr == 'turn off':
        grid[a][b] = 0
      else:  # instr == 'toggle':
        grid[a][b] = 0 if grid[a][b] else 1  ## Alternate way: grid[a][b] = 1 - grid[a][b]
      counter += 1
  return counter


with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')

  for item in lst:
    # Return list (one tuple) of matches [('turn off', '499,499', '500,500')]
    break_item = re.findall(r"(\w*|\w* \w*) (\d{1,},\d{1,}) through (\d{1,},\d{1,})", item)  
    
    if break_item:
      instr, coord_start, coord_end = break_item[0]
      # print(instr, coord_start, coord_end)
      update_lights(instr, coord_start, coord_end)

lights_on = 0
      
for i in range(len(grid)):
  lights_on += grid[i].count(1)
  # print(i, grid[i].count(1))

print("Lights on = ", lights_on)