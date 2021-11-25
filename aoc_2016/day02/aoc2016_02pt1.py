import sys

# https://adventofcode.com/2016/day/2

print("Advent of Code 2016 - Day 2 part 1")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


filename = 'test.txt'  # Code 1985
filename = 'input.txt'  # Code 92435

keypad_layout1 = [[1,2,3],[4,5,6],[7,8,9]]
pos_ud = pos_lr = 1
pos = [pos_ud, pos_lr]

code = []


def convert(ch):
  '''
    Convert character (ch) to direction +ve down or right, -ve up or left
  '''
  if ch == 'D' or ch == 'R': return 1
  if ch == 'U' or ch == 'L': return -1
  return 0


with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')  # Read file make list bu splitting on new line \n
  data = [[char for char in d] for d in data]
  
  # print(data)

  for line in data:
    print()
    # print(line)
    print("Number of instructions:", len(line))

    for char in line:
      # print('START:', ' pos ', pos_ud, pos_lr, 'Instr:', char, convert(char) )
      change = convert(char)

      if char == 'D':
        pos_ud += change
        if pos_ud > 2:  # edge bottom
          pos_ud = 2

      elif char == 'R':  
        pos_lr += change
        if pos_lr > 2: # edge right
          pos_lr = 2

      elif char == 'U':
        pos_ud += change
        if pos_ud < 0:  # edge top
          pos_ud = 0

      elif char == 'L':
        pos_lr += change
        if pos_lr < 0:  # edge left
          pos_lr = 0
      
      # print('END:', '   pos ', pos_ud, pos_lr, "Number:", keypad[pos_ud][pos_lr])
    

    code.append(keypad_layout1[pos_ud][pos_lr])
    print('FINAL NUMBER:', keypad_layout1[pos_ud][pos_lr])
  
  print()
  print("Code:", ''.join(str(c) for c in code))