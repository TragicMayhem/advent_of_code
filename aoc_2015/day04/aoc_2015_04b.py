import hashlib

# https://adventofcode.com/2015/day/4

print("Advent of Code 2015 - Day 4 part 2")

# Looking for starting six zeroes
key = 'yzbqklnj'  # 9962624

i = 0

while True:
  current = key + str(i)
  current_hash = hashlib.md5(current.encode()).hexdigest()
  if current_hash.startswith('000000'):
    break
  i += 1

print(f"The solution is {i} MD5 of {current} is {current_hash}") 
