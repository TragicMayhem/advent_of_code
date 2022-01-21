# https://adventofcode.com/2016/day/4

import pathlib
from tabnanny import check
import time

import  collections
from tkinter.tix import Tree
from typing import Counter

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 158835
input_test = script_path / 'test.txt'  # 1514 / 


def parse(puzzle_input):
    """Parse input """
    data = []
    with open(puzzle_input, 'r') as file:
        lines = file.read().split('\n')
        for l in lines:
            a, checksum = l[:-1].split('[')
            breakup = a.split('-')
            encrypt_name = ''.join(breakup[:-1])
            sector = int(breakup[-1])
            # tally = dict(Counter(encrypt_name.replace('-','')).most_common())
            data.append((encrypt_name, sector, checksum)) 

    return data


def part1(data):
    """Solve part 1""" 

    valid_sectors = []

    for room in data:
        (name, sector, checksum) = tuple(room)
        # print(name)
        # print(sector)
        # print(checksum)

        # list of Tuples: letter & count, in order. If same value, listed in order found
        tally = Counter(name).most_common()  
        # resort this using lambda function to return altered tuple
        #    1st: descending count (using -m[1])
        #    2nd: alphabetical (using m[0])
        tally = sorted(tally, key=lambda m: (-m[1],m[0]))

        # Just take the first 5 most common and form a check sequence
        seq = ''.join([str(x) for x, _ in tally[:5]])
        
        if seq == checksum:
            valid_sectors.append(sector)

    print("Valid Room sectors:", valid_sectors)

    return sum(valid_sectors)


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

    sol1, sol2, times = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")