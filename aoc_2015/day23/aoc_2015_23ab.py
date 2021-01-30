import sys
from pprint import pprint

print("Advent of Code 2015 - Day 23 part 1 and 2")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'    # a=2, b=0
filename = 'input.txt'   # a=1 b=307

part1 = [0, 0]   # a=1 b=307
part2 = [1, 0]   # a=1 b=160


def process_instructions(start):
  pointer = 0
  registers = start
  while pointer < len(data):
    d = data[pointer]
    reg_to_change = 0 if d[1] == 'a' else 1
    # print("Current pointer:", pointer,"d:" , d, "reg idx:" ,reg_to_change)

    if d[0] == 'jie':  # 3 element tuple
      if registers[reg_to_change] % 2 == 0:
        pointer += d[2]
      else:
        pointer += 1

    elif d[0] == 'jio': # 3 element tuple
      if registers[reg_to_change] == 1:
        pointer += d[2]
      else:
        pointer += 1

    elif d[0] == 'inc':
      registers[reg_to_change] += 1
      pointer += 1

    elif d[0] == 'tpl':
      registers[reg_to_change] *= 3
      pointer += 1

    elif d[0] == 'hlf':    
      registers[reg_to_change] //= 2
      pointer += 1
      
    elif d[0] == 'jmp':    
      pointer += d[1]
  
  return registers


with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')  # Read file make list bu splitting on new line \n
  data = []
  for x in lst:
    if x.find(',') > 0:
      line = x.split()
      data.append((line[0],line[1][:-1],int(line[2])))
    else:
      line = x.split()
      try:
        val = int(line[1])
      except:
        val = line[1]
      data.append((line[0],val))

  # print(data)
  
print("\nPart 1 final registers (a, b):", process_instructions(part1))
print("\nPart 2 final registers (a, b):", process_instructions(part2))
