# https://adventofcode.com/2021/day/24

'''
Multiple read throughs and working out, but finally got there.  
Not sure I would without assistance in future AOC problems!

Sources: 
    Reddit for hints and AOC solutions/hints - https://www.reddit.com/r/adventofcode/comments/rnejv5/2021_day_24_solutions/
    PJ (swift) https://github.com/pjcook/Advent-of-Code/blob/master/AdventOfCode/Year2021/Day24.swift
    DD (python) https://github.com/derailed-dash/Advent-of-Code-2021/blob/master/src/d24_alu_cartesian_creating_input_digits/alu.py

    D24 tutorial/info
    https://github.com/kemmel-dev/AdventOfCode2021/blob/master/day24/AoC%20Day%2024.pdf
'''


import functools
import pathlib
import time
from collections import deque
from functools import reduce

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 


def parse(puzzle_input):
    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        
        key_numbers = []
        alu_queue = deque()
        sections_count = 0

        # there are 14 blocks of 18 instructions.
        # Use this loop to process each looking at key instructions and altering queue as needed

        # Re-doing the simplification of the input shows
        # The pattern off the instructions is mis-leading as some are pointless (not needed) and
        # three numbers are key. (line 5, line 6 and line 16) once you simplify the instructions 
        
        # Two types of blocks  ("div z 1" and "div z 26")
        # others on reddit all talk about stacks (queues) with former pushing on and latter popping last value
        # There are 7 on and 7 off to work out digits of the 14-digit number, and the difference being the checks.

        while sections_count < 14:
            pos = sections_count * 18  # Moves index on to the next block
            # print('Section:', sections_count, 'pos:', pos)
            
            instr = data[pos + 4]
            # This should be 
            #     'div z 1'  which is push onto queue or 
            #     'div z 26' which is then pop from queue and work out values
            # Can check with .startswith but cant be bothered
            # print('\n',instr,'\n')

            if instr == 'div z 1': 
                key_instr = data[pos + 15]  # "add y a"
                
                # Split and read the number at the end (need split, not just last char in case -ve or 2-digit, oops)
                a = int(key_instr.split()[-1])  
                alu_queue.append((sections_count, a))
                # print('key_instr:', key_instr, ' value a:', a)

            else:
                key_instr = data[pos + 5]  # "add x b"
                b = int(key_instr.split()[-1])  
                pos2, a = alu_queue.pop()

                # the digits in 14-digit number, digit[sections_count] - digit[pos2] = a + b 
                key_numbers.append((sections_count, pos2, a + b))
                
                # print('key_instr:', key_instr, ' value b:', b, '  From q:', pos2, a)

            sections_count += 1

    # print('Key Numbers:', key_numbers)

    return key_numbers


def compute_model_numbers(data):
    print('\n')
    print("-"*50)
    print('Key numbers (a, b, difference):\n', data)

    highest_model_num_digits = [0] * 14   # To store the individual digits will be 1-9 each
    lowest_model_num_digits = [0] * 14    # To store the individual digits will be 1-9 each


    # If dealing with addition/=ve then the 9 is on the first digit and
    # if subtraction/-ve then the 9 is on the second digit
    # This is flipped if we want the lowest
    for digit1, digit2, diff in data:
        if diff > 0:
            highest_model_num_digits[digit1] = 9
            highest_model_num_digits[digit2] = 9 - diff

            lowest_model_num_digits[digit1] = 1 + diff
            lowest_model_num_digits[digit2] = 1
        else:
            highest_model_num_digits[digit1] = 9 + diff
            highest_model_num_digits[digit2] = 9

            lowest_model_num_digits[digit1] = 1
            lowest_model_num_digits[digit2] = 1 - diff


    # Calc number digit by digit
    # num = 0
    # for d in model_num_digits:
    #     num = num * 10 + d
    # print(num)

    # Simpler way to accumulate the total using functools.reduce and a lambda function
    # https://www.geeksforgeeks.org/reduce-in-python/

    highest_model_num = reduce(lambda tot, d: tot*10 + d, highest_model_num_digits)
    lowest_model_num = reduce(lambda tot, d: tot*10 + d, lowest_model_num_digits)

    return highest_model_num, lowest_model_num


if __name__ == "__main__":    # print()
    times=[]

    data = parse(input)
    
    times.append(time.perf_counter())
    highest, lowest = compute_model_numbers(data)
    times.append(time.perf_counter())
    
    print('\nAOC')
    print(f"Highest: {highest} and the Lowest: {lowest}")
    print(f"Execution total: {times[-1]-times[0]:.4f} seconds")