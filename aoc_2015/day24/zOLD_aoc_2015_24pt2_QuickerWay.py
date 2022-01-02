import itertools
import sys
import math
from pprint import pprint

# https://adventofcode.com/2015/day/24

print("Advent of Code 2015 - Day 24 part 1&2")
print(".......patient, its running. some comments left in to show where it is up to.")
print(".......it is A LOT of combinations and inefficient code.... but it got the right answer")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


filename = 'test.txt'  # Num parcels 10 with total weight of 60 Group target weight is 20.0  > 99
# filename = 'input.txt'  # 
# PART1 with 3 groups = Num parcels 28 with total weight of 1548 Group target weight is 516.0  > 11266889531  (TAKES AGES!)
# PART2 with 4 groups = Num parcels 28 with total weight of 1548 Group target weight is 387.0  > 77387711 (Quick only calcs group 1!)

target_groups_part1 = 3
target_groups_part2 = 4
number_groups = target_groups_part1

answers = []

def solve_groups_v1(weight_list, num_grps):
  '''
  First attempt, works out group1 then with remaining checks group2.
  Group3 is built for completeness but not checked.
  Appends combinations to res(ult) and returns

  Very slow for part 1 but does work out the lists and return combinations
  '''
  num_parcels = len(weight_list)
  total_weight = sum(weight_list)
  target_weight = total_weight / num_grps
  
  print("\nParcels:", weights)
  print('Num parcels',num_parcels,'with total weight of',total_weight,'Group target weight is', target_weight, "\n")

  res = []
  for g1 in range(4, len(weight_list) // num_grps):
    print("working....", g1)

    for c1 in itertools.combinations(weight_list, g1):# Calculate parcel weights left (not used)  (Possible Group 2 and Group3)
      left_after_group1 = [x for x in weights if x not in c1]  

      if sum(c1) == target_weight:  # Group 1 target weight met
        for g2 in range(4,len(left_after_group1)):
          
          for c2 in itertools.combinations(left_after_group1, g2):# Calc whats left from previous pool of parcels (Group 3)
            if sum(c2) == target_weight:  # Group 2 combination total equals target weight (and therefore group 3 must too)
              left_after_group2 =  [x for x in left_after_group1 if x not in c2]  # Calc remaining parcels (would be Group 3)
              # print("G1 with", c1, "G2 with", c2, " G3 (remaining)", left_after_group2)
              res.append(c1)   #Orignial was to send back a list of tuples ([c1,c2,tuple(left_after_group2)])
    
    if res: break
  return res


def solve_groups_v2(weight_list, num_grps):
  '''
  Second attempt
  Calcuates group combination for the first group ONLY.
  If it matches the target, then assumes the other groups can be calculated too (maybe bad!) but runs now
  '''
  num_parcels = len(weight_list)
  total_weight = sum(weight_list)
  target_weight = total_weight / num_grps
  
  print("\nParcels:", weights)
  print('Num parcels',num_parcels,'with total weight of',total_weight,'Group target weight is', target_weight, "\n")

  res = []
  print(f"solving for {len(weight_list)} parcel weights and {num_grps} groups and target of {target_weight}")

  for g1_size in range(4, len(weight_list) // num_grps):
    print("working....", g1_size)

    for c1 in itertools.combinations(weight_list, g1_size):
      if sum(c1) == target_weight:  # Group 1 target weight met
        res.append(c1)
        
  return res


def check_answers(ans):
  '''
  Take in list of answers for combinations for group 1
  '''
  print('\nPost processing for the answer....')
  print("Number of combinations for group 1:", len(ans), "the first few shown below:")  
  pprint(ans[:6])
  
  min_group_count = min([len(a) for a in ans])
  print("\nSmallest number of parcels in Group 1 = ", min_group_count)

  smallest_g1_combinations = [a for a in ans if len(a) == min_group_count]
  smallest_g1_combinations.sort()
  print("Number of combinations with smallest size:",len(smallest_g1_combinations), "the first few shown below:")
  pprint(smallest_g1_combinations[:6])

  qe = [math.prod(a) for a in smallest_g1_combinations]
  qe.sort()

  print("\nThe first few quantum entanglements with smallest number of parcels:")
  pprint(qe[:5])
  print("\nThe lowest qe:", qe[0])

  return qe[0]


with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')
  weights = [int(d) for d in data]
  weights.sort(reverse=True)
 
  # TAKES AGES
  # answers = solve_groups_v1(weights[:], target_weight ,target_groups_part1)
  # check_answers(answers)
  
  answers = solve_groups_v2(weights[:], target_groups_part1)
  check_answers(answers)

  answers = solve_groups_v2(weights[:], target_groups_part2)
  check_answers(answers)