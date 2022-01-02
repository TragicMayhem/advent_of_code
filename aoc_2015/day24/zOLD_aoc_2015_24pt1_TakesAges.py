import itertools
import sys
import math
from pprint import pprint

# https://adventofcode.com/2015/day/24

print("Advent of Code 2015 - Day 24 part 1")
print(".......patient, its running. some comments left in to show where it is up to.")
print(".......it is A LOT of combinations and inefficient code.... but it got the right answer")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


filename = 'test.txt'  # Num parcels 10 with total weight of 60 Group target weight is 20.0  > 99
filename = 'input.txt'  # 
# PART1 with 3 groups = Num parcels 28 with total weight of 1548 Group target weight is 516.0  > 11266889531  (TAKES AGES!)
# PART2 with 4 groups = Num parcels 28 with total weight of 1548 Group target weight is 387.0  >  (TAKES AGES!)

target_groups_part1 = 3
target_groups_part2 = 4

number_groups = target_groups_part2
answers = []

with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')
  parcels = [int(d) for d in data]
  num_parcels = len(parcels)
  total_weight = sum(parcels)
  target_weight = total_weight / number_groups

  print("\nParcels:", parcels)
  print('Num parcels',num_parcels,'with total weight of',total_weight,'Group target weight is', target_weight, "\n")

  parcels.sort(reverse=True)

  for g1 in range(4, len(parcels) // number_groups):
    print("working....", g1)
    # group1_combis = itertools.combinations(parcels, g1)

    for c1 in itertools.combinations(parcels, g1):
      left_after_group1 = [x for x in parcels if x not in c1]  # Calculate parcel weights left (not used)  (Possible Group 2 and Group3)

      if sum(c1) == target_weight:  # Group 1 target weight met
        for g2 in range(4,len(left_after_group1)):
          # group2_combis = itertools.combinations(left_after_group1, g2)  # Calc whats left from previous pool of parcels (Group 3)
          
          for c2 in itertools.combinations(left_after_group1, g2):
            if sum(c2) == target_weight:  # Group 2 combination total equals target weight (and therefore group 3 must too)
              left_after_group2 =  [] # [x for x in left_after_group1 if x not in c2]  # Calc remaining parcels (would be Group 3)
              # print("G1 with", c1, "G2 with", c2, " G3 (remaining)", left_after_group2)
              answers.append([c1,c2,tuple(left_after_group2)])
    
    if answers: break

  # pprint(answers)

  print('Post processiong for the answer....')

  min_group_count = min([len(a[0]) for a in answers])
  print("Smallest number of parcels in Group 1 = ", min_group_count)

  smallest_g1_combinations = [a for a in answers if len(a[0]) == min_group_count]
  # pprint(smallest_g1_combinations)

  qe = [math.prod(a[0]) for a in smallest_g1_combinations]
  print("The first ten quantum entanglements with smallest number of parcels:")
  print(qe[:10])