# https://adventofcode.com/2021/day/XX

import sys

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


print("Advent of Code 2021 - Day 3b")

filename = 'test.txt'  # 230
filename = 'input.txt'  #  

with open(dirpath + filename, 'r') as file:

  instr = file.read().split('\n')
  rate_oxygen = instr[:]
  rate_co2 = instr[:]

  for check_pos in range(len(rate_oxygen[0])):
  
    count_one = count_zero = 0

    for item in rate_oxygen:
      if item[check_pos] == '1':
        count_one += 1
      else:
        count_zero += 1

    print(count_one,count_zero)

    if len(rate_oxygen) == 1:
      break

    if count_one == count_zero:
      rate_oxygen = [x for x in rate_oxygen if x[check_pos] == '1']
    
    elif count_one > count_zero:
      rate_oxygen = [x for x in rate_oxygen if x[check_pos] == '1']
    
    elif count_one < count_zero:
      rate_oxygen = [x for x in rate_oxygen if x[check_pos] == '0']
      
    print(rate_oxygen)
    
    
  for check_pos in range(len(rate_co2[0])):
  
    count_one = count_zero = 0

    for item in rate_co2:
      if item[check_pos] == '1':
        count_one += 1
      else:
        count_zero += 1

    print(count_one,count_zero)

    if len(rate_co2) == 1:
      break
  
    if count_one == count_zero:
      rate_co2 = [x for x in rate_co2 if x[check_pos] == '0']
    
    elif count_one > count_zero:
      rate_co2 = [x for x in rate_co2 if x[check_pos] == '0']
    
    elif count_one < count_zero:
      rate_co2 = [x for x in rate_co2 if x[check_pos] == '1']
    
    print(rate_co2)
    
    
print(int(rate_oxygen[0],2), int(rate_co2[0],2))
ans = int(rate_oxygen[0],2) * int(rate_co2[0],2)

print("Answer:", ans)