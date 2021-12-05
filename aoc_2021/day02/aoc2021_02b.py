import sys

# https://adventofcode.com/2021/day/1

print("Advent of Code 2021 - Day 2b")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


# filename = 'test.txt'  # 900 
filename = 'input.txt'  #  

pos_h = 0
pos_d = 0
aim = 0

with open(dirpath + filename, 'r') as file:
  instr=[line.split() for line in file]

  for l in instr:
    direction = l[0][0].upper()
    if direction=='F':
      pos_h += int(l[1])
      pos_d += aim * int(l[1])
    elif direction=='U':
      aim -= int(l[1])
    elif direction=='D':
      aim += int(l[1])

print(pos_h,pos_d)
print("Total increase is", pos_d*pos_h)  
