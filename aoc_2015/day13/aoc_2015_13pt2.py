import sys
import re
from pprint import pprint

from collections import defaultdict
from itertools import permutations

# https://adventofcode.com/2015/day/13

print("Advent of Code 2015 - Day 13 part 2")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


filename = 'test.txt'  # 330
filename = 'input.txt' # 640

relationships = dict()
relationships_happiness = dict()
no_guests = 0

with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')
  
  for item in data:
    break_item = re.findall(r"^(\w*) would (gain|lose) (\d+) [\w\ ]+ (\w*)\.$", item)  
    
    if break_item:
      name, ind, points, target = break_item[0]
      try:
        points = '-' + points if ind == 'lose' else points
        val = int(points)
      except:
        val = 0

      if relationships.get(name, None) == None:   # ? Could look at module collections with defaultdict 
        relationships[name] = {}

      relationships[name].update({target: val})

no_guests = len(relationships.keys())

# Add me to the source relationships
guest_names = list(relationships.keys())
relationships['me'] = {}
for name in guest_names:
  relationships['me'].update({name: 0})
  relationships[name].update({'me': 0})


for source_name, target_dict in relationships.items():
  
  if relationships_happiness.get(source_name, None) == None:
    relationships_happiness[source_name] = {}

  for target_key, target_val in target_dict.items():
    happiness_match_val = relationships[target_key].get(source_name, 0) + target_val
    relationships_happiness[source_name].update({target_key: happiness_match_val})

seating_combis = list(permutations(relationships))
possible_scores = []

# seating_combis = [('Alice', 'Bob', 'Carol', 'David'),
# ('Alice', 'Bob', 'David', 'Carol'), ...... ]

for seating_ind in range(len(seating_combis)):
  first_position_name = seating_combis[seating_ind][0]
  last_position_name = seating_combis[seating_ind][-1]
  seating_tmp_score = relationships_happiness[first_position_name][last_position_name]

  for pos in range(1, len(seating_combis[seating_ind])):
    seating_tmp_score += relationships_happiness[seating_combis[seating_ind][pos]][seating_combis[seating_ind][pos-1]]

  possible_scores.append(seating_tmp_score)

print(f'Highest happiness is {max(possible_scores)}')