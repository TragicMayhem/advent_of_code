# https://adventofcode.com/2016/day/11

import pathlib
import time

script_path = pathlib.Path(__file__).parent

input = (('E','SG', 'SM', 'PG', 'PM'),
        ('TG', 'RG', 'RM', 'CG', 'CM'),
        ('TM'),
        ())

input_test = (('E','HM','LM'),
            ('HG'),
            ('LG'),
            ())




def parse(puzzle_input):
    """Parse input """

    data = tuple()

    data = (('E',''),(),(),())

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