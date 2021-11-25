import sys
import re
from pprint import pprint

# https://adventofcode.com/2015/day/5

print("Advent of Code 2015 - Day 5 part 1")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'  # nice, nice, naughty, naughty, naughty = 2 nice
filename = 'input.txt'  # 238

# A nice string is one with all of the following properties:
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

anti_list = ['ab', 'cd', 'pq', 'xy']
total_nice = 0

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')   
  
for current_string in lst:
  vowels_check = len(re.findall(r"([aeiou])", current_string)) >= 3
  double_check = len(re.findall(r"(\w)\1", current_string)) >= 1
  anti_check = not any([ptrn in current_string for ptrn in anti_list])
  nice_string = all([vowels_check, double_check, anti_check])
  # print('\nString:', current_string,'> vowels_check:',vowels_check, '> double_check:',double_check, '> anti_check:',anti_check, '> nice_string', nice_string)
  
  if nice_string:
    total_nice += 1

print("\nTotal nice strings: ", total_nice)