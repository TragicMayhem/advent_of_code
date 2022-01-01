# https://adventofcode.com/2015/day/16

import pathlib
import time
from pprint import pprint
from collections import defaultdict

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  #  213 / 323
dna_info = script_path / 'dna_target.txt'

props_higher = ['cats','trees']
props_lower = ['pomeranians','goldfish']


def parse(puzzle_input):
    """Parse input """

    dna_target = {}
    with open(dna_info, 'r') as file:
        data = file.read().split('\n')
        for d in data:
            props = d.split(": ")
            dna_target.update({props[0] : int(props[1])})

    aunt_info = defaultdict(dict)
    with open(puzzle_input, 'r') as file:
        data = file.read().replace(' ','').split('\n')
        data = [d.split(',') for d in data]

        for item in data:
            tmp = item[0].split(':')
            id = tmp[0][3:]
            aunt_info[id].update({tmp[1]: int(tmp[2])})    
            for i in range(1,len(item)):
                tmp = item[i].split(':')
                aunt_info[id].update({tmp[0]: int(tmp[1])})

    return dna_target, aunt_info


def part1(dna, aunts):
    """Solve part 1""" 
    
    matches = defaultdict(dict)

    for k, v in aunts.items():
        current_sue = v
        for prop, val in current_sue.items():
            if dna.get(prop, None) == val:
                # print(f"Sue {k} has property {prop} : {val}")
                matches[k].update({prop : val })

    # pprint(matches)
    best_matches = 0
    best_match_id = None

    for k, v in matches.items():
        if len(v.keys()) > best_matches:
            best_matches = len(v.keys())
            best_match_id = k 

    print(f'Most matches is {best_matches} for Sue ID # {best_match_id}')
    
    return best_match_id


def part2(dna, aunts):
    """Solve part 2"""
    matches = defaultdict(dict)

    for k, v in aunts.items():
        current_sue = v
        for prop, val in current_sue.items():
            target_val = dna.get(prop, None)

            if prop in props_higher and target_val < val:
                # print(f"Sue {k} has property {prop} : {val} > {target_val}")
                matches[k].update({prop : val })

            elif prop in props_lower and target_val > val:
                # print(f"Sue {k} has property {prop} : {val} < {target_val}")
                matches[k].update({prop : val })

            elif prop not in props_lower + props_higher and target_val == val:
                # print(f"Sue {k} has property {prop} : {val} = {target_val}")
                matches[k].update({prop : val })

    # pprint(matches)
    best_matches = 0
    best_match_id = None

    for k, v in matches.items():
        if len(v.keys()) > best_matches:
            best_matches = len(v.keys())
            best_match_id = k 

    print(f'Most matches is {best_matches} for Sue ID # {best_match_id}')
    return best_match_id
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    dna_data, aunt_dict = parse(puzzle_input)
    times.append(time.perf_counter())

    solution1 = part1(dna_data, aunt_dict)
    times.append(time.perf_counter())

    solution2 = part2(dna_data, aunt_dict)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


if __name__ == "__main__":    # print()

    sol1, sol2, times = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")