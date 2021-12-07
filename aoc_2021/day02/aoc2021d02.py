# https://adventofcode.com/2021/day/2

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt' # 150 / 900
input = script_path / 'input.txt' # 2187380 / 2086357770
 
file_in = input#_test

def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, 'r') as file:
      instr=[line.split() for line in file]

    return instr



def part1(data):
    """Solve part 1""" 
    pos_h = 0
    pos_d = 0

    for l in data:
      direction = l[0][0].upper()
      if direction=='F':
        pos_h += int(l[1])
      elif direction=='U':
        pos_d -= int(l[1])
      elif direction=='D':
        pos_d += int(l[1])

    return pos_d*pos_h


def part2(data):
    """Solve part 2"""   

    pos_h = 0
    pos_d = 0
    aim = 0

    for l in data:
      direction = l[0][0].upper()
      if direction=='F':
        pos_h += int(l[1])
        pos_d += aim * int(l[1])
      elif direction=='U':
        aim -= int(l[1])
      elif direction=='D':
        aim += int(l[1])

    return pos_d*pos_h
 

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
