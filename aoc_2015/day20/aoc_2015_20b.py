from pprint import pprint

# https://adventofcode.com/2015/day/20

print("Advent of Code 2015 - Day 20 part 2")
print("....patient, it will get the answer soon....")

# elf 1 - every hours 10 presents
# elf 7 - 7th house, 70 presents
# elf 100 - 100th house. 1000 presents

# test_input = 1000 and max houe 5 >>  48
# puzzle_input = 29000000 and max house 50 >>  705600

target_num_presents = 29000000     
max_houses_per_elf = 50   
present_multiplier = 11

presents = []
limiter = target_num_presents // 4
presents = [0] * limiter
elves = [0] * limiter

for i in range(1, limiter):
  num_pres = i * present_multiplier
  elves[i] = 1

  for j in range(i, len(presents), i):
    if elves[i] > max_houses_per_elf:
      break
    presents[j] += num_pres    
    elves[i] += 1

for house, num_presents in enumerate(presents):
  if num_presents > target_num_presents:
    print(f"The solution is house {house} with {num_presents} presents") 
    break
