import sys
import re
from pprint import pprint

print("Advent of Code 2020 - Day 7 part 1")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'
filename = 'input.txt'

search_bag = 'shiny gold'
bag_rules = {}
bag_queue = {search_bag}
possible_bags = set()

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


while bag_queue:
  srch = bag_queue.pop()

  for k, v in bag_rules.items():

    if isinstance(v, dict):
      if srch in v.keys():
        print(k, "can contain search bag", search_bag)
        bag_queue.add(k)
        possible_bags.add(k)
print("Possible bags are:")
pprint(possible_bags)
print(f"\n Total number of possible bags to hold '{search_bag}' is {len(possible_bags)}")

