# https://adventofcode.com/2021/day/5

import pathlib

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  # 5 
input = script_path / 'input.txt'  #  6005

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

      if (x1 == x2) or (y1 == y2):
        # print("  >> H or V line", x1, x2, y1 ,y2)  

        x_str = x1 if x1 < x2 else x2
        x_end = x2 if x1 < x2 else x1     
      
        y_str = y1 if y1 < y2 else y2
        y_end = y2 if y1 < y2 else y1

        for i in range(x_str, x_end+1):
          for j in range(y_str, y_end+1):
            grid[i][j] += 1

tally = 0

for i in range(grid_size):
  for j  in range(grid_size):
    if grid[i][j] > 1:
      tally += 1

print("Tally:", tally)
