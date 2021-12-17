# https://adventofcode.com/2015/day/12

import pathlib
import time
import json
import re
from pprint import pprint

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.json'  # 191164 / 87842
input_test = script_path / 'test.json'  # 23 / 19 (not 14, doh read rules. Not lists only objects!)

digits_re =  re.compile(r'-?\d+')
bad_string = "red"

def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = json.load(file)
    return data 


def look_through_item(source):
#   print("look", source)

  if isinstance(source, dict):
    # print("dict")
    return exclude_bad_from_dict(source)

  elif isinstance(source, list):
    # print("list")
    return exclude_bad_from_list(source)
  
  return source


def exclude_bad_from_list(source_list):
  tmp_list = list()

  for i in source_list:
    tmp_list.append(look_through_item(i))
  
  return tmp_list


def exclude_bad_from_dict(source_dict):
  tmp_dict = dict()

  if bad_string not in source_dict.values():
    for k, v in source_dict.items():
        tmp_dict[k] = look_through_item(v)
  
  return tmp_dict


def part1(data):
    """Solve part 1""" 
    text = json.dumps(data)
    numbers = [int(s) for s in  digits_re.findall(text)]
    return sum(numbers)


def part2(data):
    """Solve part 2"""
    
    valid_items = look_through_item(data)
    new_text = json.dumps(valid_items)
    # print("  new:", new_text)

    # pprint(valid_items)
    numbers = [int(s) for s in  digits_re.findall(new_text)]
    # pprint(numbers)

    return sum(numbers)
 

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


if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")