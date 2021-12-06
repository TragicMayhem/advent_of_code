# https://adventofcode.com/2021/day/XX

import sys

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


print("Advent of Code 2021 - Day 3a")

# filename = 'test.txt'  # 198
filename = 'input.txt'  #  

rate_gamma = []
rate_epsilon = []

with open(dirpath + filename, 'r') as file:

  instr = file.read().split('\n')
  
  for check_pos in range(len(instr[0])):
  
    count_one = count_zero = 0

    for item in instr:

      if item[check_pos] == '1':
        count_one += 1
      else:
        count_zero += 1
    
    if count_one > count_zero:
      rate_gamma.append("1")
      rate_epsilon.append("0")
    else:
      rate_gamma.append("0")
      rate_epsilon.append("1")
    
# print(rate_gamma, rate_epsilon)

rateg_bin = "".join(rate_gamma)
ratee_bin = "".join(rate_epsilon)
print(rateg_bin, ratee_bin)
ans = int(rateg_bin,2) * int(ratee_bin,2)

print("Answer:",int(rateg_bin,2),"*",int(ratee_bin,2),"=", ans)