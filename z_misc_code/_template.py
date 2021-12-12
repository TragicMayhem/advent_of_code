# https://adventofcode.com/2021/day/x

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 
 
file_in = input #_test


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
      data = file.read().split('\n')
    #   data = [d.split(' | ') for d in file.read().split('\n')]

    return data


def part1(data):
    """Solve part 1""" 
                  
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


def runTests():
    
    data = parse(input_test)
    solution1a = part1(data)
    solution1b = part2(data)
    
    print("Tests")
    print(f'Test1.  Part1 {solution1a} Part 2 {solution1b}')
    

if __name__ == "__main__":    # print()

    runTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")