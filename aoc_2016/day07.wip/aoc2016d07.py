# https://adventofcode.com/2016/day/7

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  #
input_test = script_path / 'test.txt'  # 

#      ****
# abcd[bddb]xyyx
check_in_brackets = re.compile(r'\[([a-z]*([a-z])([a-z])(\3)(\2))\]|')

# Split the string on [] to get three parts and check pattern for each part
# Use the any check below?
check_pattern = re.compile(r'([a-z])([a-z])(\2)(\1)')

capture_chars = re.compile(r'([a-z]+)')
capture_in_brackets = re.compile(r'(\[[a-z]+\])')
capture_any = re.compile(r'([a-z]+|\[[a-z]+\])')

def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        print(data)
    return data



    # vowels_check = len(re.findall(r"([aeiou])", current_string)) >= 3
    # double_check = len(re.findall(r"(\w)\1", current_string)) >= 1
    # anti_check = not any([ptrn in current_string for ptrn in anti_list])
    # nice_string = all([vowels_check, double_check, anti_check])
    
    # two_digits_pattern = re.compile('(\d{2})')
    # find_digit = re.compile(r'(\d+)')
    # find_last_digit = re.compile(r'(\d+)(?!.*\d)')
    # find_digit_pair = re.compile(r'(\d+)[, ]+(\d+)')
    # next_left_num_pos = find_last_digit.search(to_the_left)
    # next_right_num_pos = find_digit.search(to_the_right)

    # numbers = [int(s) for s in  digits_re.findall(text)]



def part1(data):
    """Solve part 1""" 
    
    for d in data:
        print('d', d)
        parts = re.split('\[|\]', d)
        print('parts', parts)


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