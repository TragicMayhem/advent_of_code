from itertools import groupby
from pprint import pprint

# https://adventofcode.com/2015/day/10

print("Advent of Code 2015 - Day 10 part 1 and 2")

test_input = '1'  # 312211 > len = 6
puzzle_input = '1113222113'  # Part 1 = 252594  // Part 2 = 3579328

latest_ouput = puzzle_input   ## Set to input string test or P
max_count = 40   ## Set to 40 for part 1 or 50 for Part 2

for i in range(max_count):
  new_list = list()
  grouped_content = ["".join(g) for k, g in groupby(latest_ouput)]
  # print("LOOP:", i, latest_ouput)
  # print("Grouped:", grouped_content)

  for g in grouped_content:
    new_list.append(str(len(g)) + g[0])

  latest_ouput = "".join(new_list)
  
print("\nOutput:", len(latest_ouput))
