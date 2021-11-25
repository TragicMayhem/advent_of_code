import sys
import re
from pprint import pprint

# https://adventofcode.com/2015/day/6

print("Advent of Code 2015 - Day 6 part 2")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


# filename = 'test.txt'  # 1,001,996 Though not a good test set of data
# filename = 'test2.txt'  # 3,001,993 = 1m + 2k - 4 + 1 + 2m - 4 = 3m + 2k -7 
filename = 'input.txt'  # 15,343,601

# Grid = 0,0 to 999,999
# Input: (turn on|turn off|togggle) x1,y1 through x2,y2
# The phrase turn on actually means that you should increase the brightness of those lights by 1.
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
# The phrase toggle actually means that you should increase the brightness of those lights by 2.

grid = [[0 for j in range(1000)] for i in range(1000)]


def update_lights(change, st, en):
  counter = 0
  st_x, st_y = map(int, st.split(','))
  en_x, en_y = map(int, en.split(','))

  for a in range(st_x, en_x+1):
    for b in range(st_y, en_y+1):
      if instr == 'turn on':
        grid[a][b] += 1

      elif instr == 'turn off':
        grid[a][b] -= 1 if grid[a][b] > 0 else 0

      else:  # instr == 'toggle':
        grid[a][b] += 2


with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')

  for item in lst:
    # Return list (one tuple) of matches [('turn off', '499,499', '500,500')]
    break_item = re.findall(r"(\w*|\w* \w*) (\d{1,},\d{1,}) through (\d{1,},\d{1,})", item)  
    
    if break_item:
      instr, coord_start, coord_end = break_item[0]
      # print(instr, coord_start, coord_end)
      update_lights(instr, coord_start, coord_end)

lights_brightness = 0
      
for i in range(len(grid)):
  for j in range(len(grid[0])):
    lights_brightness += grid[i][j]

print("Lights brightness = ", lights_brightness)
