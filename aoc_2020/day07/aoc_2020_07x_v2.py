import sys
import re
from pprint import pprint

print("Advent of Code 2020 - Day 7 part 2")

# Second attempt at using recursion to solve this.
# Works using a list to stop recursive calls there not needed. Improves execution time (I think)

dirpath = sys.path[0] + '\\'

filename = 'test.txt'  # 32   
# filename = 'test2.txt'  # 126 
# filename = 'input.txt'  # 18295 

search_bag = 'shiny gold'
bag_rules = {}
bag_queue = {search_bag}
possible_bags = set()
bag_counter = []


def count_bags_new(bg, counts = None):
  '''
    Recursive call to count sub bags for parent (bg)
    Initial call is for just the "target bag".  This will create an empty dictionary for lookups
    
    Each call, if its not in the lookup dictionary it will store it. Future calls will just return lookup
    Reduces the complexity and time.
  '''
  if counts == None: counts={}
  if bg in counts.keys():  # already calculated, so just return
    return counts[bg]

  tmp = bag_rules.get(bg, '') 
  running_total = 0
  
  if isinstance(tmp, dict):
    for sub_bag, qty_of_sub_bag in tmp.items():
      counts[sub_bag] = count_bags_new(sub_bag, counts)  # Recursive call for sub_bag, store in counts (used by any recurcive call ny reference)
     
      # Running total for the parent bag, is current sub_bags * qty, plus the number of this type
      running_total += (counts[sub_bag] * qty_of_sub_bag) + qty_of_sub_bag

  # Will default to store 0 (running total) if tmp isnt a dictionary 
  counts[bg] = running_total
  return counts[bg]


with open(dirpath + filename, 'r') as file:
  
  # Replaces plurals and splites the lines to separate parent from children. 
  # lst will end as a list of lists (sub lists have 2 parts - 0 = parent and 1 = all chilren in one string)
  lst = file.read().split('\n')   
  lst = [x.replace('bags', 'bag').replace('.','').split(' bag contain ') for x in lst]

  # pprint(lst)

  # Loop round the sub lists (so x is a list that has parent(0) and then children(1))
  for x in lst:
    if x[1] == 'no other bag':
      tmp = []
    else:
      tmp = re.findall(r'(\d+) ([\w ]+) bag', x[1])  # RegEx to find all the patterns and groups for (num) (name) bag 
      tmp = [(b, int(a)) for (a,b) in tmp]  # Convert the groups to a list of tuples with bag name and integer quantity

    # pprint(tmp)
    
    bag_rules[x[0]] = dict(tmp) if tmp else None  # Dictionary(parent) = a sub dictionary created from the list of tuples
    # pprint(bag_rules[x[0]])


pprint(bag_rules)

print("\n------------------------------------------------")
print(f"\n Total number of bags inside '{search_bag}' is {count_bags_new(search_bag)}\n")
