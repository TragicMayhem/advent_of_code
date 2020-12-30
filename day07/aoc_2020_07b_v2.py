import sys
import re
from pprint import pprint

print("Advent of Code 2020 - Day 7 part 2")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'  # 32
# filename = 'test2.txt'  # 126
# filename = 'input.txt'  # 18295 

search_bag = 'shiny gold'
bag_rules = {}
bag_queue = {search_bag}
possible_bags = set()
bag_counter = []

def count_bags_new(bg, counts = {}):
  if bg in counts.keys():  # already calculated, so just return
    return counts[bg]

  tmp = bag_rules.get(bg, '') 
  running_total = 0
  
  if isinstance(tmp, dict):
    for sub_bag, qty_of_sub_bag in tmp.items():
      counts[sub_bag] = count_bags_new(sub_bag, counts)
      # Running total for the parent bag, is current sub_bags * qty, plus the number of this type
      running_total += (counts[sub_bag] * qty_of_sub_bag) + qty_of_sub_bag

  # Dont need this as will default to store 0 (running total) 
  # if tmp == None: # Contains no bags, so store and return
  #   counts[bg] = 0
  #   return counts[bg]

  counts[bg] = running_total
  return counts[bg]


with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')   
  lst = [x.replace('bags', 'bag').replace('.','').split(' bag contain ') for x in lst]
  
  for x in lst:
    if x[1] == 'no other bag':
      tmp = []
    else:
      tmp = re.findall(r'(\d+) ([\w ]+) bag', x[1])
      tmp = [(b, int(a)) for (a,b) in tmp]
    
    bag_rules[x[0]] = dict(tmp) if tmp else None

pprint(bag_rules)

print("\n------------------------- NEW -------------------------\n")
print("")
print(f"\n Total number of bags inside '{search_bag}' is {count_bags_new(search_bag)}")
