import sys
from pprint import pprint

print("Advent of Code 2020 - Day 9 part 1")

dirpath = sys.path[0] + '\\'

# filename = 'test_5num_preamble.txt'  # 127
filename = 'input.txt'   # 393911906 

# 5 for test data, 25 for input
preamble_len = 25


def canSum(targetsum, numbers, memo=None):
  # print("__call:", targetsum, numbers, memo)
  if memo == None: memo = {}
  if targetsum in memo.keys(): return memo[targetsum]
  if targetsum == 0: return True
  if targetsum < 0: return False
  
  for i, val in enumerate(numbers):
    # print("__loop:", i, val)
    remainder = targetsum - val
    nums_left = numbers[:i] + numbers[i+1:]

    if canSum(remainder, nums_left, memo):
      memo[targetsum] = True
      return memo[targetsum]
  
  memo[targetsum] = False
  return memo[targetsum]


with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')   
  lst = [int(x) for x in lst]

  print("")
  for x in range(preamble_len, len(lst)):
      # print(x, "lst[x]", lst[x], "pass:", canSum(lst[x], lst[x - preamble_len :x]))
      if not canSum(lst[x], lst[x - preamble_len :x]):
        print("lst[",x, "] =", lst[x], "  pass:", canSum(lst[x], lst[x - preamble_len :x]))
        break
