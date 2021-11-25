import sys
import re
from pprint import pprint
from collections import defaultdict

# https://adventofcode.com/2015/day/14

print("Advent of Code 2015 - Day 14 part 2")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


# filename = 'test.txt'  # Dancer 689 points for 1000 seconds  (Comet 312)
# race_time = 1000   # for test file

filename = 'input.txt'  #  1102 for Donner
race_time = 2503 #  for main race

# psuedo
# dict reindeer
  # info: speed, flying for seconds, resting seconds
  # change: current fly time, current rest time, flying true false - on change, reset the current timer, total dist
# loop counter = seconds until flytime max
# on each check against each ren, if flying increment counter, if not leave. reset on change over

reindeer = defaultdict(dict)


def change_status(name, info):
  '''
    Updates given reindeers flight information. Builds subkey from info and updates
    dictionary of Reindeer information

      Parameters:
              names (str): name (key) for the reindeer to be updated
              info (str): sub key 'fly_time' or 'rest_time'

      Returns:
              Nothing
  '''
  current = 'current_' + info

  reindeer[name][current] += 1  
  
  if reindeer[name][current] >= reindeer[k][info]:
    reindeer[name][current] = 0
    reindeer[name]['is_flying'] = not reindeer[name]['is_flying']


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
      reindeer[reindeer_name].update({'points': 0})


for s in range(race_time):
  # print('-------',s,'-------')
  leaders = []
  leading_distance = 0

  for k, v in reindeer.items():

    if reindeer[k]['is_flying']:
      reindeer[k]['distance'] += reindeer[k]['speed']
      change_status(k, 'fly_time')
    else:
      change_status(k, 'rest_time')
    
    if reindeer[k]['distance'] > leading_distance:
      leaders = [k]
      leading_distance = reindeer[k]['distance']
    elif reindeer[k]['distance'] == leading_distance:
      leaders.append(k)

  # check points
  for l in leaders:
    reindeer[l]['points'] += 1
  


# pprint(reindeer)
winning_dist = winning_points = 0
print()
for k in reindeer.keys():
  winning_dist = reindeer[k]['distance'] if reindeer[k]['distance'] > winning_dist else winning_dist
  winning_points = reindeer[k]['points'] if reindeer[k]['points'] > winning_points else winning_points
  print(f"{k} travelled {reindeer[k]['distance']} km in {race_time} seconds. Points {reindeer[k]['points']}")

print()
print(f"The winning is {winning_dist} km")
print(f"The winning points {winning_points}")