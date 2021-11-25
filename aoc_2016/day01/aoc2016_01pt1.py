import sys

# https://adventofcode.com/2016/day/1

print("Advent of Code 2016 - Day 1 part 1")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


filename = 'test.txt'  # 12
filename = 'input.txt'  # 236

directions = ['N', 'E', 'S', 'W']

with open(dirpath + filename, 'r') as file:
  data = file.read().split(', ')

  val_ns = val_ew = 0
  facing_ind = 0
  facing = directions[facing_ind]

  for i in data:
    move_val = int(i[1:])
    
    if i[0] == 'R': 
      facing_ind = (facing_ind + 1) if facing_ind <3 else 0
      
    if i[0] == 'L':
      facing_ind = (facing_ind - 1) if facing_ind > 0 else 3
      
    if directions[facing_ind] == 'N':  val_ns += move_val
    if directions[facing_ind] == 'S':  val_ns -= move_val
    if directions[facing_ind] == 'E':  val_ew += move_val
    if directions[facing_ind] == 'W':  val_ew -= move_val

    # print(f'END {i}; {facing_ind}; {directions[facing_ind]} > NS {val_ns} EW {val_ew}\n')
 

val_ew =  val_ew * -1 if val_ew < 0 else val_ew
val_ns =  val_ns * -1 if val_ns < 0 else val_ns

print(f'N-S difference: {val_ns} and E-W difference: {val_ew} so distance is {val_ns + val_ew}\n')
 