# https://adventofcode.com/2016/day/4

import pathlib
import time

import  collections
from typing import Counter

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  #                     Not 179969
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
        print()
        for ele in room:
            print(ele)

        name = room[0]
        sector = room[1]
        checksum = room[2]

        prev = 0
        valid_room = True

        # list of Tuples: letter & count, in order. If same value, listed in order found
        tally = Counter(name).most_common()  

        # Flip the counts to validate against the checksum        
        d = {}
        for k, v in tally:
            d.setdefault(v, []).append(k)
        stack = list(checksum)

        for k,v in d.items():
            next = stack.pop(0)
            print('kv', k,v,'next', next)
            if next not in v:
                valid_room = False
                break

        # for c in checksum:
        #     print(c, tally.get(c,-1))
        #     if tally.get(c,-1) < prev:
        #         valid_room = False
        #         break
        
        if valid_room:
            valid_sectors.append(sector)

    print(valid_sectors)

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

    # sol1, sol2, times = solve(input)
    # print('\nAOC')
    # print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    # print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    # print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")