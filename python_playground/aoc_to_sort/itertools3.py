
import itertools 
from pprint import pprint


def calc_combinations(target, splits):
  '''
    range 1 to target for each of the splits to form all combinations
    remove all that are not eq target
    return the list
  '''
  output = []
  results = list(itertools.combinations(range(1, target+1), splits))

  for i in results:
      if sum(i) == target:
          output.append(i)
  
  return output


def calc_perms(target, splits):
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


keep_combs = calc_combinations(100, 4)
print(len(keep_combs))

keep_perms = calc_perms(100, 4)
print(len(keep_perms))