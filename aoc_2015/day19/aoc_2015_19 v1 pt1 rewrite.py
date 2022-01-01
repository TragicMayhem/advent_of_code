# https://adventofcode.com/2015/day/19

import pathlib
import time
from pprint import pprint
import re

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'             # 576 / 
input_test = script_path / 'input_test.txt'  # 4 distinct in 1 replacements
input_test2 = script_path / 'input_test2.txt'  # 7 distinct in 9 replacements


def parse(puzzle_input):
    """Parse input """

    replacements = {}

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        chain = data.pop(-1)

        for d in data:
            if d == '': continue
            tmp = d.split(' => ')
            if replacements.get(tmp[0], None) == None:
                replacements[tmp[0]] = []
            replacements.get(tmp[0]).append(tmp[1])

    print("Input: Chain")   
    print(chain)
    print("\nInput: Replacements")   
    print(replacements)

    return chain, replacements    


def part1(chain, replacements):
    """Solve part 1""" 
    molecules = set()

    for key, combis in replacements.items():
        pattern = key
        for match in re.finditer(pattern, chain):
            s = match.start()
            # e = match.end()
            # print( 'String match "%s" at %d:%d' % (chain[s:e], s, e))
            for m in combis:
                tmp_molecule = chain[:s] + m + chain[s+len(key):]
                molecules.add(tmp_molecule)
    
    return len(molecules)


def part2(chain, replacements):
    """Solve part 2"""   
   
    return 1
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    chain, replacements = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1(chain, replacements)
    times.append(time.perf_counter())
    solution2 = part2(chain, replacements)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runTest(test_file):
    chain, replacements = parse(test_file)
    test_solution1 = part1(chain, replacements)
    test_solution2 = part2(chain, replacements)
    return test_solution1, test_solution2


def runAllTests():
    
    print("\nTests\n")
    a, b, t  = solve(input_test)
    print(f'Test1 Part 1: {a} in {t[1]-t[0]:.4f}s')
    print(f'      Part 2: {b} in {t[2]-t[1]:.4f}s')
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")
    
    a, b, t  = solve(input_test2)
    print(f'Test2 Part 1: {a} in {t[1]-t[0]:.4f}s')
    print(f'      Part 2: {b} in {t[2]-t[1]:.4f}s')
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":

    runAllTests()

    sol1, sol2, times = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")