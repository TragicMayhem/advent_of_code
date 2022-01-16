# https://adventofcode.com/2016/day/4

import pathlib
import time

import  collections
from typing import Counter

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  #
input_test = script_path / 'test.txt'  # 


def parse(puzzle_input):
    """Parse input """
    data = []
    with open(puzzle_input, 'r') as file:
        lines = file.read().split('\n')
        for l in lines:
            a, checksum = l[:-1].split('[')
            tally = dict(Counter(a.replace('-','')).most_common(5))
            # tally = Counter(a.replace('-','')).most_common(5)
            breakup = a.split('-')
            data.append((breakup[:-1], int(breakup[-1]), tally, checksum)) 

    return data


def part1(data):
    """Solve part 1""" 

    for room in data:
        for ele in room:
            print(ele)

        prev = 0
        for c in room[-1]:
            print(c)
            if 
# look round check sum and then tally the order, 
# if each order is greater than or eq to previos ok, else not valid

    return 1


def part2(data):
    """Solve part 2"""
    
    return 1
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    times.append(time.perf_counter())

    solution1 = part1(data)
    times.append(time.perf_counter())

    solution2 = part2(data)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runAllTests():

    print("\nTests\n")
    a, b, t  = solve(input_test)
    print(f'Test1 Part 1: {a} in {t[1]-t[0]:.4f}s')
    print(f'      Part 2: {b} in {t[2]-t[1]:.4f}s')
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":    # print()

    runAllTests()

    # sol1, sol2, times = solve(input)
    # print('\nAOC')
    # print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    # print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    # print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")