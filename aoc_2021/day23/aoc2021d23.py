# https://adventofcode.com/2021/day/x

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 

'''
NOTES
hallway is 11 long - actually 7 if they cannot stop in the space outside room
4 rooms each 2 spaces
rooms L-R target is to hold A-B-C-D

7 holding spaces
8 spaces in rooms
8 target spaces

A cost 1
B cost 10
C cost 100
D cost 1000 

need to know each status for the rules
- locked hallway (after moving there, then waiting for their room)
- not in target
- still in start room
- hasnt moved yet, allowed to stay in rooms
- once in a hallway, wont move unless their room is free (target room)
- cant wait in space outside the rooms (effectively blocked?)
- cant go into a room if there is one already not in final place
- need to count number of moves with each. unique id

- if pos in source room, is low(1), and not target room,     need to move before target can move in 

'''

target_layout = ('AA','BB','CC','DD')
hallway = '...........'
valid_hallway_idn = (0,1,3,4,7,9,10)   # Not in the spaces outside the rooms


COSTS = {
    'A' : 1,
    'B' : 10,
    'C' : 100,
    'D' : 1000
}


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
    #    data = [d.split(' | ') for d in file.read().split('\n')]

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