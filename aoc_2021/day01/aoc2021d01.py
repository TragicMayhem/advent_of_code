# https://adventofcode.com/2021/day/1

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  # 5 
input = script_path / 'input.txt'  #  
 
file_in = input_test


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, 'r') as file:
      lst = file.read().split('\n')   #  Read each line (split \n) and form a list of strings

    return [int(n) for n in lst]



def part1(data):
    """Solve part 1""" 

    total = 0
    prev = 0
    for x in data[1:]:
      total = total +1 if (x > prev) else total 
      prev = x
      
    return total


def part2(data):
    """Solve part 2"""   

    total = 0
    prev = 0

    for i, x in enumerate(data[:-3]):
      next = sum(data[i:i+3])
      total = total + 1 if (next > prev) else total
      prev = next

    return total
 

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

if __name__ == "__main__":    # print()

    solutions = solve(file_in)
    print()
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")