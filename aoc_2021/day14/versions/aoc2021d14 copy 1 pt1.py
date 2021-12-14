
# https://adventofcode.com/2021/day/14

import pathlib
import time
from collections import defaultdict
from collections import Counter

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 2447 / 
input_test = script_path / 'test.txt'  # 


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        polymer, instructions = file.read().split('\n\n')
        rules = defaultdict()
        tmp = [[r for r in pair.split(' -> ')] for pair in instructions.split('\n')]
        for l,r in tmp:
            rules[l] = r

        print(polymer)
        print(rules)

    return polymer, rules

    return data


def part1(polymer, insertion_rules, steps=10):
    """Solve part 1""" 

    current_polymer = polymer
    print(insertion_rules)

    for i in range(steps):
        # print("Polymer = ",current_polymer)
        next_polymer = ''

        for c in range(len(current_polymer)-1):
            check=current_polymer[c]+current_polymer[c+1]
            # print('\n',c, current_polymer, check)    

            if check in insertion_rules.keys():
                insertion = check[0] + insertion_rules[check] #+ check[1]
            else:
                insertion_rules = check[0]

            next_polymer = next_polymer + insertion

            # print(next_polymer)
        next_polymer = next_polymer + current_polymer[-1]

        # print(current_polymer,' > ', next_polymer)
        current_polymer = next_polymer
        # print('\nstep end',c,len(current_polymer))   

        char_count = Counter(current_polymer)
        print(char_count)

        answer = max(char_count.values())- min(char_count.values())

    return answer


def part2(polymer, insertion_rules):
    """Solve part 2"""   
   
    return 1
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    polymer, insertion_rules = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1(polymer, insertion_rules)
    times.append(time.perf_counter())
    solution2 = part2(polymer, insertion_rules)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runTest(test_file):
    polymer, insertion_rules = parse(test_file)
    test_solution1 = part1(polymer, insertion_rules)
    test_solution2 = part2(polymer, insertion_rules)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runTest(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")