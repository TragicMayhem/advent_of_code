import sys
import re
from pprint import pprint
from collections import defaultdict

# https://adventofcode.com/2015/day/16

print("Advent of Code 2015 - Day 16 part 2")
dirpath = sys.path[0] + '\\'

dna_file = 'dna_target.txt'    # Best match part 2 = 323 (3 matches)
filename = 'input.txt' 

props_higher = ['cats','trees']
props_lower = ['pomeranians','goldfish']

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
    target_val = item[0].split(':')
    id = target_val[0][3:]
    aunt_info[id].update({target_val[1]: int(target_val[2])})    
    for i in range(1,len(item)):
      target_val = item[i].split(':')
      aunt_info[id].update({target_val[0]: int(target_val[1])})
  
# pprint(aunt_info)

matches = defaultdict(dict)

for k, v in aunt_info.items():
  current_sue = v
  for prop, val in current_sue.items():
    target_val = dna_target.get(prop, None)

    if prop in props_higher and target_val < val:
      print(f"Sue {k} has property {prop} : {val} > {target_val}")
      matches[k].update({prop : val })

    elif prop in props_lower and target_val > val:
      print(f"Sue {k} has property {prop} : {val} < {target_val}")
      matches[k].update({prop : val })

    elif prop not in props_lower + props_higher and target_val == val:
      print(f"Sue {k} has property {prop} : {val} = {target_val}")
      matches[k].update({prop : val })

pprint(matches)
best_matches = 0
best_match_id = None

for k, v in matches.items():
  if len(v.keys()) > best_matches:
    best_matches = len(v.keys())
    best_match_id = k 

print(f'Most matches is {best_matches} for Sue ID # {best_match_id}')