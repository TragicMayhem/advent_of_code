import sys
from pprint import pprint

# https://adventofcode.com/2015/day/2

print("Advent of Code 2015 - Day 2 part 1")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


# Test 2x3x4 - 2*6 + 2*12 + 2*8 = 52 plus 6 = 58
# Test - 2*1 + 2*10 + 2*10 = 42 plus 1 = 43
# filename = 'test.txt'  # 58 and 43

filename = 'input.txt'  # 1588178


# Calculation is 2*l*w + 2*w*h + 2*h*l plus area of smallest side

total = 0

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')   #  Read each line (split \n) and form a list of strings
  lst = [x.replace('x', ' ').split() for x in lst]  # Split on 'x' in each string ('1x2x3')
  
  # lst is now a list of lists, sub lists have single characters e.g. [['2', '3', '4'], ['1', '1', '10']]
  # To convert each of the strings to integers you use list comprehension twice anduse [] to put back in list
  converted_list = [[int(dim) for dim in sub_list] for sub_list in lst]

  for x in converted_list:
    # Each x should be three numbers
    w, l, h = x
    side_areas = [w*l, w*h, h*l]
    total += 2*sum(side_areas) + min(side_areas)
    
print("Total square foot of paper required is", total)  
