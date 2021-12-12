# https://adventofcode.com/2021/day/2

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt' # 331067 / 92881128
input_test = script_path / 'test.txt' # 37 / 168


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input, 'r') as file:
        input=[[int(x) for x in row] for row in [line.split(',') for line in file]]
    return input.pop()


def part1(data):
    """Solve part 1""" 
    min_pos=min(data)
    max_pos=max(data)

    answers = {}
    for i in range(min_pos+1,max_pos+1):
      answers[str(i)] = 0
      for crabpos in data:
        crab_fuel = abs(crabpos - i)
        answers[str(i)] += crab_fuel

    return min(answers.values())


def part2(data):
    """Solve part 2"""   
    min_pos=min(data)
    max_pos=max(data)
    answers=dict()

    for i in range(min_pos+1, max_pos+1):
      answers[str(i)] = 0

      for crabpos in data:
        # Slower version using range and lists
        # gap = list(range(1, abs(crabpos - i)+1))
        t=abs(crabpos - i)
        answers[str(i)] += (t*(t+1))/2

    return min(answers.values())
 

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


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runTest(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')
    

if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
