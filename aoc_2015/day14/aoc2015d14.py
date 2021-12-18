# https://adventofcode.com/2015/day/14

import pathlib
import time
import re
from pprint import pprint
from collections import defaultdict

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # Rudolph 2640 in 2503 seconds
input_test = script_path / 'test.txt'  # Comet 1120 for 1000 seconds

# race_time = 1000 for test file / race_time = 2503 for input

# psuedo
# dict reindeer
  # info: speed, flying for seconds, resting seconds
  # change: current fly time, current rest time, flying true false - on change, reset the current timer, total dist
# loop counter = seconds until flytime max
# on each check against each ren, if flying increment counter, if not leave. reset on change over


def parse(puzzle_input):
    """Parse input """

    reindeer = defaultdict(dict)

    with open(puzzle_input, 'r') as file:
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

    return reindeer


def change_status(reindeer, name, info):
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
  
  if reindeer[name][current] >= reindeer[name][info]:
    reindeer[name][current] = 0
    reindeer[name]['is_flying'] = not reindeer[name]['is_flying']


def part1(reindeer, race_time):
    """Solve part 1""" 

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

    winning_dist = 0

    for k in reindeer.keys():
        winning_dist = reindeer[k]['distance'] if reindeer[k]['distance'] > winning_dist else winning_dist
        print(f"{k} travelled {reindeer[k]['distance']} km in {race_time} seconds")

    print(f"The winner is {winning_dist} km")        
    
    return winning_dist


def part2(reindeer, race_time):
    """Solve part 2"""   
    for s in range(race_time):
        # print('-------',s,'-------')
        leaders = []
        leading_distance = 0

        for k, v in reindeer.items():

            if reindeer[k]['is_flying']:
                reindeer[k]['distance'] += reindeer[k]['speed']
                change_status(reindeer, k, 'fly_time')
            else:
                change_status(reindeer, k, 'rest_time')
            
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

    return winning_points
 

def solve(puzzle_input, race_time):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runSingleTestData(test_file, race_time):
    data = parse(test_file)
    test_solution1 = part1(data, race_time)
    test_solution2 = part2(data, race_time)
    return test_solution1, test_solution2


def runAllTests(race_time):
    
    print("Tests")
    a, b  = runSingleTestData(input_test, race_time)
    print(f'Test1.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests(1000)

    # solutions = solve(input, 2503)
    # print('\nAOC')
    # print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    # print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    # print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")