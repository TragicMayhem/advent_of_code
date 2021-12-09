# https://adventofcode.com/2015/day/5

import pathlib
import re
from pprint import pprint

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'
input_test = script_path / 'test.txt' 
input_test2 = script_path / 'test2.txt' 
  
 
file_in = input#_test
# filename = 'test2.txt'  # nice, nice, naughty, naughty = 2 nice
# filename = 'input.txt'  # 69

# A nice string is one with all of the following properties:
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

total_nice = 0

with open(file_in, 'r') as file:
  lst = file.read().split('\n')   
  
for current_string in lst:
  check1 = len(re.findall(r"(\w)[a-z]\1", current_string)) >= 1
  check2 = len(re.findall(r"(\w{2}).*?\1", current_string)) >= 1
  nice_string = all([check1, check2])
  
  if nice_string:
    total_nice += 1

print("\nTotal nice strings: ", total_nice)