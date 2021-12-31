# https://adventofcode.com/2015/day/8

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'       # 1350 / 2085
input_test = script_path / 'test.txt'   # string chars (2 + 5 + 10 + 6 = 23) in memory (0 + 3 + 7 + 1 = 11) so 23 - 11 = 12
                                        # (6 + 9 + 16 + 11 = 42)  42 - 23 = 19
input_test2 = script_path / 'test2.txt' # 50 / 75 

# Disregarding the whitespace in the file, 
# what is the number of characters of code for string literals minus the number of characters # in memory 
# for the values of the strings in total for the entire file?

# (\\\\)  - Expression matches \\  = 2 char-space
# (\\x[0-9a-z]{2})  - Expression matches \x and 2 chars/digits [0-9a-z]  = 4 char-space
# (\\\")  - Expression matches \"  = 2 char-space
# (\\\\)|(\\x[\w]{2})|(\\\")   - Match all but group each component pattern
# (\\\\|\\x[\w]{2}|\\\")   - Match all but just each one separately, so get a single list


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
    return data


def part1(data):
    """Solve part 1""" 
    tot_space = 0
    tot_char_len = 0

    for l in data:
        tmp = l[1:-1]
        
        find_escaped = re.findall(r"(\\\\|\\x[\w]{2}|\\\")", l)  
        # print(find_escaped)

        tot_space += len(l)
        tot_char_len += len(l) - 2 - sum(len(f) for f in find_escaped) + len(find_escaped)

    # print("Answer:", tot_space - tot_char_len)             
    return tot_space - tot_char_len


def part2(data):
    """Solve part 2"""   
    tot_space = 0

    for l in data:
        tmp = l
        tmp = tmp.replace('\\x', '^x')   # 'Cheat' replace this with char not there, replace rest then change this back with extra \
        tmp = tmp.replace('\\', '\\\\').replace('"','\\"')
        tmp = tmp.replace('^x', '\\\\x')
        tmp = '"' + tmp + '"'

        tot_space += len(tmp) - len(l)

    # print("Answer:", tot_space)
    return tot_space
 

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

    def runSingleTestData(test_file):
        data = parse(test_file)
        test_solution1 = part1(data)
        test_solution2 = part2(data)
        return test_solution1, test_solution2
   
    print("Tests")
    a, b  = runSingleTestData(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')
    a, b  = runSingleTestData(input_test2)
    print(f'Test3.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")