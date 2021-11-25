from pprint import pprint

# https://adventofcode.com/2015/day/20

print("Advent of Code 2015 - Day 20 part 1")
print("....patient, it will get the answer soon....")

# elf 1 - every hours 10 presents
# elf 7 - 7th house, 70 presents
# elf 100 - 100th house. 1000 presents

# test_input = 130 , 1000
# puzzle_input = 29000000  # 665280

target_num_presents = 29000000

presents = []
max_houses = target_num_presents // 4
presents = [0] * max_houses

for i in range(1, max_houses+1):
  num_pres = i * 10
  for j in range(i, len(presents), i):
    presents[j] += num_pres    

for house, num_presents in enumerate(presents):
  if num_presents > target_num_presents:
    print(f"The solution is house {house} with {num_presents} presents") 
    break
