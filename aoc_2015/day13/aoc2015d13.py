# https://adventofcode.com/2015/day/13

import pathlib
import time
import re
from pprint import pprint
from collections import defaultdict
from itertools import permutations

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  #  664 / 640
input_test = script_path / 'test.txt'  # 330 / 286


def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
    return data


def build_relationships(data):
    relationships = dict()
    relationships_happiness = dict()
    no_guests = 0
    
    for item in data:
        break_item = re.findall(r"^(\w*) would (gain|lose) (\d+) [\w\ ]+ (\w*)\.$", item)  
    
        if break_item:
            name, ind, points, target = break_item[0]
        try:
            points = '-' + points if ind == 'lose' else points
            val = int(points)
        except:
            val = 0

        if relationships.get(name, None) == None:   # ? Could look at module collections with defaultdict 
            relationships[name] = {}

        relationships[name].update({target: val})

    # no_guests = len(relationships.keys())
    
    return (relationships, relationships_happiness)


def work_out_happiness(relationships, relationships_happiness):

    for source_name, target_dict in relationships.items():
        if relationships_happiness.get(source_name, None) == None:
            relationships_happiness[source_name] = {}

        for target_key, target_val in target_dict.items():
            happiness_match_val = relationships[target_key].get(source_name, 0) + target_val
            relationships_happiness[source_name].update({target_key: happiness_match_val})

    seating_combis = list(permutations(relationships))
    possible_scores = []

    # seating_combis = [('Alice', 'Bob', 'Carol', 'David'),
    # ('Alice', 'Bob', 'David', 'Carol'), ...... ]

    for seating_ind in range(len(seating_combis)):
        first_position_name = seating_combis[seating_ind][0]
        last_position_name = seating_combis[seating_ind][-1]
        seating_tmp_score = relationships_happiness[first_position_name][last_position_name]

        for pos in range(1, len(seating_combis[seating_ind])):
            seating_tmp_score += relationships_happiness[seating_combis[seating_ind][pos]][seating_combis[seating_ind][pos-1]]

        possible_scores.append(seating_tmp_score)

    # print(f'Highest happiness is {max(possible_scores)}')

    return max(possible_scores)

def part1(data):
    """Solve part 1""" 
    relationships, relationships_happiness = build_relationships(data)
    ans = work_out_happiness(relationships, relationships_happiness)

    return ans


def part2(data):
    """Solve part 2"""   
    
    relationships, relationships_happiness = build_relationships(data)

    # Add me to the source relationships
    guest_names = list(relationships.keys())
    relationships['me'] = {}
    for name in guest_names:
        relationships['me'].update({name: 0})
        relationships[name].update({'me': 0})

    ans = work_out_happiness(relationships, relationships_happiness)
    return ans
 

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