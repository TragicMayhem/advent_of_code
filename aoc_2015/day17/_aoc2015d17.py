# https://adventofcode.com/2015/day/17

import pathlib
import time
from itertools import combinations

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 1304 / 18 (ways to use 4 containers)
input_test = script_path / 'test.txt'  # 4 / 3


def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        data = sorted([int(d) for d in data])
    return data


def howtostore(target_amt, quantities):
  ways = []
  for n in range(1, target_amt):
    for combination in combinations(quantities, n):
      if sum(combination) == target_amt:
        ways.append(combination)
  return ways


def part1(data, target=25):
    """Solve part 1""" 
    
    possible_ways = howtostore(target, data)

    # print(f'Target litres: {target_litres} using a list with {len(data)} quantities')
    # print(f'\nPossible combinations: {len(possible_ways)}')

    return len(possible_ways)


def part2(data, target=25):
    """Solve part 2"""
    
    possible_ways = howtostore(target, data)

    min_num_of_containers = None
    for i in range(len(possible_ways)):
        if min_num_of_containers == None or min_num_of_containers > len(possible_ways[i]):
            min_num_of_containers = len(possible_ways[i])
            # print(min_num_of_containers, ":", possible_ways[i])

    count = 0
    for i in range(len(possible_ways)):
        if min_num_of_containers == len(possible_ways[i]):
            count += 1 

    # print(f'Minimum number of containers is {min_num_of_containers} and there are {count} possible ways to use that number')

    return count
 

def solve(puzzle_input, target_amount):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    times.append(time.perf_counter())

    solution1 = part1(data, target_amount)
    times.append(time.perf_counter())

    solution2 = part2(data, target_amount)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runAllTests(target_amount):

    print("\nTests\n")
    a, b, t  = solve(input_test, target_amount)
    print(f'Test1 Part 1: {a} in {t[1]-t[0]:.4f}s')
    print(f'      Part 2: {b} in {t[2]-t[1]:.4f}s')
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":    # print()

    runAllTests(25)

    sol1, sol2, times = solve(input, 150)
    print('\nAOC')
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")