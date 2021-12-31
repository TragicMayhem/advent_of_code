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


if __name__ == "__main__":    # print()

    runAllTests()

    sol1, sol2, times = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")