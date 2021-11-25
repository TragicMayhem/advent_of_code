import sys
from pprint import pprint

# https://adventofcode.com/2015/day/2

print("Advent of Code 2015 - Day 2 part 2")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


# filename = 'test.txt'  # 34 and 14
filename = 'input.txt'  # 


#  Ribbon calculation is 
#    the shortest distance around its sides, or the smallest perimeter of any one face
#    the perfect bow is equal to the cubic feet of volume of the present

# A present with dimensions 2x3x4 
#   requires 2+2+3+3 = 10 feet of ribbon to wrap the present 
#   plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.

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
    smallest_perimeter = min([2 * x for x in [l+w, h+l, w+h] ])  # Build list of one pair sides, double for each perimter, find min
    volume = w*h*l
    total += smallest_perimeter + volume

print("Total ribbon required is", total)  
