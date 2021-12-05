# https://adventofcode.com/2021/day/5

import pathlib
from pprint import pprint

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  # 12
input_test2 = script_path / 'test2.txt'  # 2
input_test3 = script_path / 'test3.txt'  # 4
input_test4 = script_path / 'test4.txt'  # 0
input = script_path / 'input.txt'  #  23864

file_in = input #_test

grid_size = 1000
lines = []
grid = [[0 for j in range(grid_size)] for i in range(grid_size)]


if __name__ == "__main__":

  with open(file_in, 'r') as file:
    data=[line.split() for line in file]

    for d in data:
      del(d[1])
      tmp = d[0].split(',')
      (x1,y1) = int(tmp[0]) , int(tmp[1])
      tmp = d[1].split(',')
      (x2,y2) = int(tmp[0]) , int(tmp[1])

      lines.append([(x1, y1), (x2, y2)])

      # print("LATEST", lines[-1])

      is_diag = abs(x1-x2) == abs(y1-y2)
      
      if (x1<=x2 and y1<=y2) or (x1>x2 and y1>y2):
        dir=1
      else:
        dir=-1
      
      x_start = min(x1,x2)  
      x_end = max(x1,x2)
      y_start = min(y1,y2)
      y_end = max(y1,y2)

      if (x1 == x2) or (y1 == y2) or is_diag :
        # print("  coords", (x1, y1), (x2, y2))
        # print("  >> line Using:", (x_start, y_start), (x_end, y_end), is_diag, dir)  
        # print("  >> x:", x_start, "to", x_end, " y:", y_start, "to", y_end)  

        if is_diag:
          j=y_start if dir==1 else y_end

          for i in range(x_start, x_end+1):
            grid[j][i] += 1
            j+=(1 * dir)

        else:
          for i in range(x_start, x_end+1):
            for j in range(y_start, y_end+1):
              grid[j][i] += 1

# pprint(grid)

tally = 0

for i in range(grid_size):
  for j in range(grid_size):
    if grid[i][j] > 1:
      tally += 1

print("Tally:", tally)
