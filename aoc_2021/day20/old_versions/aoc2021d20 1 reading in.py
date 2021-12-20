# https://adventofcode.com/2021/day/x

import pathlib
import time
import numpy as np

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        parts = file.read().split('\n\n')
    
        enhancements_converted = parts[0].replace('.','0').replace('#','1')
        enhancements = [char for char in enhancements_converted]

        print(enhancements)

        parts[1] = parts[1].replace('.','0').replace('#','1')
        image_list = [l for l in parts[1].split('\n')]
        new_converted_image = []
        for p in image_list:
            print(p)
            
            new_converted_image.append(list(map(int,[char for char in p])))

        print(new_converted_image)

        y=np.array([np.array(xi) for xi in new_converted_image])
        # new_a = np.pad(a, ((1,1),(1,1)), mode='constant', constant_values=0)
        print(y)

        y2 = np.pad(y, ((1,1),(1,1)), mode='constant', constant_values=0)
        print(y2)

    return 1


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

    # solutions = solve(input)
    # print('\nAOC')
    # print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    # print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    # print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")