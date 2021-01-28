import sys
import re
from pprint import pprint
from collections import defaultdict

# https://adventofcode.com/2015/day/14

print("Advent of Code 2015 - Day 14 part 1")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'  # Comet 1120 for 1000 seconds
filename = 'input.txt'  # Rudolph 2640 in 2503 seconds

# race_time = 1000   # 1000 for test file
race_time = 2503

# psuedo
# dict reindeer
  # info: speed, flying for seconds, resting seconds
  # change: current fly time, current rest time, flying true false - on change, reset the current timer, total dist
# loop counter = seconds until flytime max
# on each check against each ren, if flying increment counter, if not leave. reset on change over

reindeer = defaultdict(dict)

with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')

  for item in data:
    break_item = re.findall(r"^(\w*) can fly (\d+) km/s for (\d+) sec.* for (\d+) seconds\.$", item)  
    
    if break_item:
      reindeer_name, speed, fly_time, rest_time = break_item[0]
      
      reindeer[reindeer_name].update({'fly_time': int(fly_time)})
      reindeer[reindeer_name].update({'speed': int(speed)})
      reindeer[reindeer_name].update({'rest_time': int(rest_time)})
      reindeer[reindeer_name].update({'current_fly_time': 0})
      reindeer[reindeer_name].update({'current_rest_time': 0})
      reindeer[reindeer_name].update({'is_flying': True})
      reindeer[reindeer_name].update({'distance': 0})

# pprint(reindeer)

for s in range(race_time):
  # print('-------',s,'-------')
  for k, v in reindeer.items():

    if reindeer[k]['is_flying']:
      reindeer[k]['distance'] += reindeer[k]['speed']
      reindeer[k]['current_fly_time'] += 1

      if reindeer[k]['current_fly_time'] >= reindeer[k]['fly_time']:
        reindeer[k]['current_fly_time'] = 0
        reindeer[k]['is_flying'] = False

    else:
      reindeer[k]['current_rest_time'] += 1

      if reindeer[k]['current_rest_time'] >= reindeer[k]['rest_time']:
        reindeer[k]['current_rest_time'] = 0
        reindeer[k]['is_flying'] = True

# pprint(reindeer)
winning_dist = 0

for k in reindeer.keys():
  winning_dist = reindeer[k]['distance'] if reindeer[k]['distance'] > winning_dist else winning_dist
  print(f"{k} travelled {reindeer[k]['distance']} km in {race_time} seconds")

print(f"The winner is {winning_dist} km")