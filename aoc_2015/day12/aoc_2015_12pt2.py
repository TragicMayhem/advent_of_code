import sys
import json
import re
from pprint import pprint

# https://adventofcode.com/2015/day/12

print("Advent of Code 2015 - Day 12 part 2")

dirpath = sys.path[0] + '\\'

filename = 'test.json' # 19   (not 14, doh read rules. Not lists only objects!)
filename = 'input.json'  #  87842

digits_re =  re.compile(r'-?\d+')
bad_string = "red"


def look_through_item(source):
  print("look", source)

  if isinstance(source, dict):
    print("dict")
    return exclude_bad_from_dict(source)

  elif isinstance(source, list):
    print("list")
    return exclude_bad_from_list(source)
  
  return source


def exclude_bad_from_list(source_list):
  tmp_list = list()

  for i in source_list:
    tmp_list.append(look_through_item(i))
  
  return tmp_list


def exclude_bad_from_dict(source_dict):
  tmp_dict = dict()

  if bad_string not in source_dict.values():
    for k, v in source_dict.items():
        tmp_dict[k] = look_through_item(v)
  
  return tmp_dict


with open(dirpath + filename, 'r') as file:
  data = json.load(file)
  pprint(data)

  valid_items = look_through_item(data)
  new_text = json.dumps(valid_items)
  print("  new:", new_text)

  pprint(valid_items)
  numbers = [int(s) for s in  digits_re.findall(new_text)]
  pprint(numbers)
  print("Sum of numbers is", sum(numbers))