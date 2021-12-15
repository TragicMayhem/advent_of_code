# https://adventofcode.com/2021/day/15

import pathlib
import time
import heapq
from collections import defaultdict
from math import inf as INFINITY

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 

'''
Reference https://www.redblobgames.com/pathfinding/a-star/introduction.html

Version 2
- Part 1 works

'''

def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        data=[[int(x) for x in row] for row in data]      
        grid=defaultdict(int)

        # grid = tuple(tuple(map(int, row)) for row in file.read().split('\n'))

        for r, row in enumerate(data):
           for c, cell in enumerate(row):
               grid[(r,c)] = cell

        size = len(data)

    return grid, size


def get_coords_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def grid_search(grid, size):

    startNode = (0,0)
    goalNode = (size-1, size-1)

    frontier = [(startNode, 0)]
    came_from = set()
    risks = defaultdict(lambda: INFINITY, {startNode: 0})
    risks[startNode] = 0

    # Construct a map of all possible paths for the startNode across the map
    while frontier:
        current, risk = heapq.heappop(frontier)
        # print('curr:',current,risk, 'cost', grid.get(current))

        if current == goalNode:
            return risk

        if current in came_from:
            continue

        came_from.add(current)
        # print(came_from)
        x,y = current

        for cardinal in get_coords_cardinals(x,y, size, size):
            # print('cardinal cost',cardinal, grid.get(cardinal))
            
            if cardinal in came_from:
                continue

            xx, yy  = cardinal
            newrisk = risk + grid.get(cardinal)  #[xx][yy]

            if newrisk < risks[cardinal]:
                risks[cardinal] = newrisk
                heapq.heappush(frontier, (cardinal, newrisk))

    return 404


def part1(grid, size):
    """Solve part 1""" 
    
    ans = grid_search(grid, size)


    return ans


def part2(data, size):
    """Solve part 2"""   
   
    return 1
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data, size = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1(data, size)
    times.append(time.perf_counter())
    solution2 = part2(data, size)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runTest(test_file):
    data, size = parse(test_file)
    test_solution1 = part1(data,size)
    test_solution2 = part2(data,size)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runTest(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

    #not 584 too low

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")