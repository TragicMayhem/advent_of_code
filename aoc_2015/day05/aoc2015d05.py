# https://adventofcode.com/2015/day/5

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 238 /69
input_test = script_path / 'test.txt'  # nice, nice, naughty, naughty, naughty = 2 nice
input_test2 = script_path / 'test2.txt' # nice, nice, naughty, naughty = 2 nice

# A nice string is one with all of the following properties:
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.


def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
    return data


def part1(data):
    """Solve part 1""" 
    anti_list = ['ab', 'cd', 'pq', 'xy']
    total_nice = 0   
    
    for current_string in data:
        vowels_check = len(re.findall(r"([aeiou])", current_string)) >= 3
        double_check = len(re.findall(r"(\w)\1", current_string)) >= 1
        anti_check = not any([ptrn in current_string for ptrn in anti_list])
        nice_string = all([vowels_check, double_check, anti_check])
        # print('\nString:', current_string,'> vowels_check:',vowels_check, '> double_check:',double_check, '> anti_check:',anti_check, '> nice_string', nice_string)
        
        if nice_string:
            total_nice += 1

    # print("\nTotal nice strings: ", total_nice)      

    return total_nice


def part2(data):
    """Solve part 2"""   
    total_nice = 0
        
    for current_string in data:
        check1 = len(re.findall(r"(\w)[a-z]\1", current_string)) >= 1
        check2 = len(re.findall(r"(\w{2}).*?\1", current_string)) >= 1
        nice_string = all([check1, check2])
    
        if nice_string:
            total_nice += 1

    # print("\nTotal nice strings: ", total_nice)
    return total_nice
 

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


def runSingleTestData(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runSingleTestData(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')
    a, b  = runSingleTestData(input_test2)
    print(f'Test2.  Part1: {a} Part 2: {b}')

if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")