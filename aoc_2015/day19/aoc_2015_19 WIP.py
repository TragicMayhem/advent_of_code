# https://adventofcode.com/2015/day/19

import pathlib
import time
from pprint import pprint
import re
from collections import defaultdict

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 576 / 
input_test = script_path / 'input_test.txt'  # 4 distinct in 1 replacements
input_test2 = script_path / 'input_test2.txt'  # 7 distinct in 9 replacements
input_test3 = script_path / 'input_test3pt2.txt'  # 7 distinct in 9 replacements
input_test4 = script_path / 'input_test4pt2.txt'  # 7 distinct in 9 replacements


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
            e = match.end()
            # print( 'String match "%s" at %d:%d' % (chain[s:e], s, e))
            for m in combis:
                tmp_molecule = chain[:s] + m + chain[s+len(key):]
                molecules.add(tmp_molecule)
     
    return len(molecules)


def apply_change(med, pos, source, target):
    # take med upto pos, add in target, add rest of med after the pos+len(source)
    return med[:pos] + target + med[pos+len(source):]


def reverse_engineer(medicine, reverse_replacements):

    current_molecule = medicine
    results = []
    more_to_do = True

    # while more_to_do:
    #     more_to_do = False

    #     for target, source in reverse_replacements.items():
    #         if source == 'e':
    #             continue

    #         matches = len(re.findall(target, current_molecule))
    #         if matches > 0:
    #             current_molecule = re.sub(target, source, current_molecule)
    #             more_to_do = True
    #             results.append([matches, current_molecule])
    
    # for target, source in reverse_replacements.items():
    #     print(target,source)
    #     if source != 'e':
    #         continue

    #     matches = len(re.findall(target, current_molecule))
    #     if matches > 0:
    #         current_molecule = re.sub(target, source, current_molecule))
    #         results.append([matches, current_molecule])

    # # print(results)
    # print('-'*50)
    # print(current_molecule)
    # answer = sum(step[0] for step in results)
    answer = 1
    return answer


def part2(medicine, replacements):
    """Solve part 2"""   

    reverse_replacements = defaultdict(list)
    for k, v in replacements.items():
        for target in v:
            reverse_replacements[target] = k
    
    print('target:',medicine)
    print(reverse_replacements)

    answer = reverse_engineer(medicine, reverse_replacements)

    return answer
 

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