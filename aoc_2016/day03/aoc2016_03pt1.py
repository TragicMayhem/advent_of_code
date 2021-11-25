import sys

# https://adventofcode.com/2016/day/3

print("Advent of Code 2016 - Day 3 part 1")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'  # 4
filename = 'input.txt'  #  1050 Valid / 942 impossible

impossible = []
valid = []

with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')  # Read file make list bu splitting on new line \n
  data = [' '.join(d.split()).split() for d in data] # Splits/rejoins (to replace the multiple spaces), the splits into list
  data = [[int(i) for i in d] for d in data]

  for triangle in data:
    if len(triangle) == 3:
      combi1 = triangle[0] + triangle[1] > triangle[2]
      combi2 = triangle[0] + triangle[2] > triangle[1]
      combi3 = triangle[1] + triangle[2] > triangle[0]
      valid_triangle = all([combi1, combi2, combi3])

      # print(f'Tri: {triangle}, {combi1} {combi2} {combi3} >>> Status = {valid_triangle}')

      if valid_triangle:
        valid.append(triangle)
      else:
        impossible.append(triangle)
      

    else:
      print("Incorect number of sides)")
  
  print()
  print(f"Input: {len(data)} with {len(valid)} valid triangles and {len(impossible)} impossible")

