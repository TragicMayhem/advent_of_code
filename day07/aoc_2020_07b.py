import sys
import re
from pprint import pprint

print("Advent of Code 2020 - Day 7 part 2")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'  # 32
# filename = 'test2.txt'  # 126
filename = 'input.txt'

search_bag = 'shiny gold'
bag_rules = {}
bag_queue = {search_bag}
possible_bags = set()
bag_counter = []

def count_bags(bg):
  # print("Call:", bg)
  running_total = 0
  tmp = bag_rules.get(bg, '')
      
  if isinstance(tmp, dict):
    # print("  dict:", tmp)

    for k, v in tmp.items():
      # print("  current k,v :", k, v)
      how_many_of_this_type = v
      sub_bags = count_bags(k)  # Recursive call to calculate sub_bag(s)
      running_total = running_total + (sub_bags * how_many_of_this_type) + how_many_of_this_type
      # print("  > after sub_bags:", sub_bags, " how_many_of_this_type:", how_many_of_this_type, " val:", running_total)
    
    return running_total
  
  # print("  Contains no others - return 0\n")
  return 0


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

# pprint(bag_rules)
print("")
print(f"\n Total number of bags inside '{search_bag}' is {count_bags(search_bag)}")
