import sys
from pprint import pprint

# https://adventofcode.com/2015/day/25

print("Advent of Code 2015 - Day 25 part 1")
print(".....takes a few seconds to work out the grid of numbers....")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'  # row 1, column 2   = 18749137   result: 18749137
# filename = 'test2.txt'  # row 2, column 4  = 7726640    result: 7726640
# filename = 'test3.txt'  # row 4, column 5  = 10600672   result: 10600672

filename = 'input.txt'  # row 3010, column 3019 result: 8997277

starting_val = 20151125
multiplier = 252533
modulas = 33554393


def print_grid():
  for r in range(grid_rows):
    for c in range(grid_cols):
      print(f"r {r} c {c} codes[{r}][{c}] {codes[r][c]}")


with open(dirpath + filename, 'r') as file:
  data = file.read().split(',')
  target_row = int(data[0].split(' ')[-1]) - 1 
  target_col = int(data[1].split(' ')[-1]) - 1
  print("\nTarget row:", target_row, "Target column:", target_col)

  grid_rows = grid_cols = target_row + target_col + 1
  codes = [[0 for i in range(grid_rows)] for j in range(grid_cols)]
  codes[0][0] = starting_val

  print("Check size of codes grid:", len(codes[0]), len(codes[1])) 
  print()

  # NOTES:
  # 1st: r0 c0 = 20151125
  # 2nd: r1 c0 > uses r0 c0 next r0 c1
  # 3rd: r0 c1 > uses r1 c0 next r2 c0
  # 4th: r2 c0 > uses r0 c1 next r1 c1
  # 5th: r1 c1 > uses r2 c0 next r0 c2
  # 6th: r0 c2 > uses r1 c1 next r3 c0

  r = 0 
  c = 0  
  previous_val = codes[0][0]
  print("r, target_row, c, target_col", r, target_row, c, target_col)

  while r != target_row or c != target_col:

      if c == 0 and r > 1:
        # print("col is zero", r, c)
        r -= 1   
        c += 1

      elif r == 0:
        # print("row is zero", r, c)
        r = c + 1
        c = 0
        
      else:  # r > 0 and c > 0
        # print("mid grid", r, c)
        r -= 1
        c += 1

      new_val = (previous_val * multiplier) % modulas
      codes[r][c] = new_val
      previous_val = new_val
      # print(f'new val = {new_val} for r({r}) c({c})')

  print("\nAnswer:", codes[target_row][target_col])