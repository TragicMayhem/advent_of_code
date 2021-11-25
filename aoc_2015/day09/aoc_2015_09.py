import sys
import itertools
from pprint import pprint

# https://adventofcode.com/2015/day/9

print("Advent of Code 2015 - Day 9 part 1 and 2")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'  # London -> Dublin -> Belfast = 605
filename = 'input.txt'  # Part 1 = 141 (Shortest)   Part 2 = 736 (Longest)

routes = dict()

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')   
  lst = [x.replace('to ','').replace('= ','').split(' ') for x in lst]

  for l in lst:
    if l[0] not in routes.keys(): routes[l[0]] = dict()
    if l[1] not in routes.keys(): routes[l[1]] = dict()
    routes[l[0]][l[1]] =  int(l[2])
    routes[l[1]][l[0]] =  int(l[2])
    
destinations = set(routes.keys())  # Unique set of destinations
possible_routes = list(itertools.permutations(destinations))  # All the permutations of the destinations/. List tuples

distances = list()

for route in possible_routes:
  # print("\n", route)
  running_total = 0
  i = 0
  while i < len(route)-1: # Loop untiul the second to last element (thats the destination)
    # print(i, route[i], routes[route[i]], routes[route[i]][route[i+1]])
    running_total += routes[route[i]][route[i+1]]
    i += 1
  
  distances.append(running_total)

# print("\nPossible routes")
# pprint(possible_routes)
# print("\nRoute distances")
# pprint(distances)
print("\nShortest route:", min(distances))
print("\nLongest route:", max(distances))