# https://adventofcode.com/2021/day/x

import pathlib
import time
from collections import defaultdict

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 


# class scanner:
#     def __init__(self, id):
#         self.id = None
#         self. = None
#         self.data = data



def parse(puzzle_input):
    """Parse input """

    scannerdata = defaultdict()

    with open(puzzle_input, 'r') as file:
        lines = file.read().split('\n')
        
        beacons = []
        for l in lines:
            print(l)
            if l == '':
                scannerdata[scanner_id] = beacons
                beacons = ()
                continue
            
            if l.find('---'):
                parts = l.split(' ')
                scanner_id = parts[2]
                scannerdata[scanner_id] = defaultdict(tuple)
                continue

            parts = l.split(',')
            beacons.append((int(parts[0]),int(parts[1]),(int(parts[3]))))

    print(scannerdata)

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