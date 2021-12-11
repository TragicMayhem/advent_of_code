import sys
import re
from pprint import pprint

print("Advent of Code 2020 - Day 7 part 2")

# First attempt to use recursion to solve this.
# It works and is correct but not efficient. 

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


# filename = 'test.txt'  # 32
# filename = 'test2.txt'  # 126
filename = 'input.txt'  # 18925

search_bag = 'shiny gold'
bag_rules = {}
bag_queue = {search_bag}
possible_bags = set()
bag_counter = []


def count_bags(bg):
  '''
    Count all the bags that can contain target (bg)
    Recursive call for each sub bag in the dictionary
    Each call's return value is the total of sub bags.
    Running total built each time, adding correct number of the parent quantity
  '''
  # print("Call:", bg)
  running_total = 0
  tmp = bag_rules.get(bg, '')  # Get rules or empty string if not found
      
  if isinstance(tmp, dict):
    # print("  dict:", tmp)

    for k, v in tmp.items():
      # print("  current k,v :", k, v)
      how_many_of_this_type = v
      sub_bags = count_bags(k)  # RECURSION - call to calculate sub_bag(s)
  
      running_total = running_total + (sub_bags * how_many_of_this_type) + how_many_of_this_type
      # print("  > after sub_bags:", sub_bags, " how_many_of_this_type:", how_many_of_this_type, " val:", running_total)
    
    return running_total
  
  # print("  Contains no others - return 0\n")
  return 0


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


# pprint(bag_rules)
print(f"\nTotal number of bags inside '{search_bag}' is {count_bags(search_bag)}\n")
