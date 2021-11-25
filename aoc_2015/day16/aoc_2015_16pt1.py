import sys
import re
from pprint import pprint
from collections import defaultdict

# https://adventofcode.com/2015/day/16

print("Advent of Code 2015 - Day 16 part 1")
dirpath = sys.path[0] + '\\'

dna_file = 'dna_target.txt'    # Best match part 1 = 213 (3 matches)
filename = 'input.txt' 

dna_target = {}
aunt_info = defaultdict(dict)

with open(dirpath + dna_file, 'r') as file:
  data = file.read().split('\n')
  for d in data:
    props = d.split(": ")
    dna_target.update({props[0] : int(props[1])})

# pprint(dna_target)

with open(dirpath + filename, 'r') as file:
  data = file.read().replace(' ','').split('\n')
  data = [d.split(',') for d in data]

  for item in data:
    tmp = item[0].split(':')
    id = tmp[0][3:]
    aunt_info[id].update({tmp[1]: int(tmp[2])})    
    for i in range(1,len(item)):
      tmp = item[i].split(':')
      aunt_info[id].update({tmp[0]: int(tmp[1])})
  
# pprint(aunt_info)

matches = defaultdict(dict)

for k, v in aunt_info.items():
  current_sue = v
  for prop, val in current_sue.items():
    # for target_prop, target_val in dna_target:
    if dna_target.get(prop, None) == val:
      print(f"Sue {k} has property {prop} : {val}")
      matches[k].update({prop : val })

pprint(matches)
best_matches = 0
best_match_id = None

for k, v in matches.items():
  if len(v.keys()) > best_matches:
    best_matches = len(v.keys())
    best_match_id = k 

print(f'Most matches is {best_matches} for Sue ID # {best_match_id}')