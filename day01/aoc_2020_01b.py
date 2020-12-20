from itertools import combinations 

# Input file is a list of numbers, one per line
# three numbers add to 2020, then multiple to get the answer

print("Advent of Code 2020 - Day 1 - Part 2")

numbers = []

# handle = open('test.txt', 'r')
handle = open('input.txt', 'r')
lines_list = handle.readlines()
handle.close()

for i in range(len(lines_list)):
  numbers.append(int(lines_list[i].rstrip()))

numbers = sorted(numbers)
combination_list = list(combinations(numbers, 3))

for tup in combination_list:
  if sum(tup) == 2020:
    print(tup, "Multiplied = ", tup[0] * tup[1] * tup[2])

