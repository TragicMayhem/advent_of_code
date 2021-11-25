import sys
from collections import defaultdict
import itertools 
import math
from pprint import pprint
import timeit

# https://adventofcode.com/2015/day/15

print("Advent of Code 2015 - Day 15 part 1 and 2")
print("....wait for it to run its computing a lot of permutations (approx 30-40s)")
dirpath = sys.path[0] + '\\'

# input sample line: "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8"

# Part 1: 44 B 65 C score is 62842880   Part 2: 40 B and 60 C = 500 calories and score 57600000
# filename = 'test.txt'  # 2 items, 49 combis to make 100  

filename = 'input.txt'  # Part 1: 21367368     Part 2: 1766400

max_teaspoons = 100
keep_combinations = []
ingredients = defaultdict(dict)
properties = [ 'capacity', 'durability', 'flavor', 'texture', 'calories']  # Ignore calories in part 1 calc of the score


def calc_combinations(target, splits):
  '''
    range 1 to target for each of the splits to form all combinations
    remove all that are not eq target
    return the list
  '''
  output = []
  results = list(itertools.permutations(range(1, target+1), splits))

  for i in results:
      if sum(i) == target:
          output.append(i)
  
  return output

time_start = timeit.default_timer()

with open(dirpath + filename, 'r') as file:
  data = file.read().replace(': ',',').replace(', ', ',').split('\n')
  data = [d.split(',') for d in data]

  for item in data:
    name = item[0]

    for i in range(1,len(item)):
      tmp = item[i].split(' ')
      ingredients[name].update({tmp[0]: int(tmp[1])})
  
  number_of_ingredients = len(ingredients.keys()) 
  names_of_ingredients = list(ingredients.keys())
  keep_combinations = calc_combinations(max_teaspoons, number_of_ingredients)

  print("A. Time difference after calc_combinations :", timeit.default_timer() - time_start)

  pprint(ingredients)
  print("No. ingredients:", number_of_ingredients, "List:", names_of_ingredients) 
  
  all_answers = []
  valid_property_lists = []
  
  for mix in keep_combinations:
    # print("\nmix >", mix)
    current_mix_list = []
    for i, teaspoons in enumerate(mix):
      # print(" > i", i,"teaspoons", teaspoons)
      prop_list = []

      for j in range(len(properties)):
        prop_list.append(ingredients[names_of_ingredients[i]].get(properties[j], 0) * teaspoons)

      current_mix_list.append(prop_list)
    
    # Use zip to to sum all the elements in each list together to get the answer for each property
    property_totals_list = [sum(i) for i in zip(*current_mix_list)]
    
    all_answers.append(property_totals_list)
    # print("Are all above 0?", all(i > 0 for i in ans))
    if all(i >= 0 for i in property_totals_list):
      valid_property_lists.append(property_totals_list)

  print("B. Time difference after mixes loop :", timeit.default_timer() - time_start)

# print(all_answers)

  scores = []
  for a in valid_property_lists:
    scores.append(math.prod(a[:-1]))  # Ignore calories in the score

  print("\nPart 1")
  print("Number of filtered multiplied answers:", len(valid_property_lists))
  # print(list(valid_property_lists))
  # print("All scores:\n", scores)
  print("\nThe highest score is:", max(scores))

  print("C. Time difference after Part 1 :", timeit.default_timer() - time_start)

  print("\nPart 2")
  low_cal_cookies = []
  for i in range(len(valid_property_lists)):
    if valid_property_lists[i][4] == 500:
      low_cal_cookies.append(scores[i])
      # print(f"Cookie with 500 calories has a score of {scores[i]}")

  print("Highest scoring low calories cookie: ", max(low_cal_cookies))

print("The time difference is :", timeit.default_timer() - time_start)