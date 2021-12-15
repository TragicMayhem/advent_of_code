# https://adventofcode.com/2021/day/15

import pathlib
import time
import heapq
from collections import defaultdict
from math import inf as INFINITY   ## NEW: I was missing this for the risk checking default value

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 592 / 2897
input_test = script_path / 'test.txt'  # 40 / 315


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        data=[[int(x) for x in row] for row in data]

    size = len(data)
    return data, size


def expand_grid(data, from_size):
    
    expanded_grid = data[:]

    w = h = from_size
    extra_grids = 4

    # go across
    for _ in range(extra_grids):
        for line in data:
            cells = line[-w:]
            line.extend((x+1) if x < 9 else 1 for x in cells)

    # go down
    for _ in range(extra_grids):
        for line in expanded_grid[-h:]:
            newline = list((x+1) if x < 9 else 1 for x in line)
            expanded_grid.append(newline)

    size = len(expanded_grid)

    return expanded_grid, size


def get_coords_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def grid_search(grid, size):

    startNode = (0,0)
    goalNode = (size-1, size-1)

    print(startNode, goalNode)

    # frontier = [(startNode, 0)]
    frontier = [(0, startNode)]
    risks = defaultdict(lambda: INFINITY) #, {startNode: 0})
    risks[startNode] = 0
    came_from = set()

    # Construct a map of all possible paths for the startNode across the map
    while frontier:
        risk, current = heapq.heappop(frontier)
        # current, risk = heapq.heappop(frontier)
        # print('curr:',current, risk)

        if current == goalNode:
            # print(len(risks),risks)
            return risk

        if current in came_from:
            continue

        came_from.add(current)
        x,y = current

        for cardinal in get_coords_cardinals(x,y, size, size):
            # print('cardinal cost',cardinal, grid.get(cardinal))
            if cardinal in came_from:
                continue

            x,y = cardinal
            newrisk = risk + grid[x][y]

            if newrisk < risks[cardinal]:
                risks[cardinal] = newrisk
                heapq.heappush(frontier, (newrisk, cardinal))

    return INFINITY  #404


def part1(grid, size):
    """Solve part 1""" 
    
    ans = grid_search(grid, size)

    return ans


def part2(grid, size):
    """Solve part 2"""   
   
    ans = grid_search(grid, size)

    return ans
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data, size_sm = parse(puzzle_input)

    times.append(time.perf_counter())

    solution1 = part1(data, size_sm)
    
    times.append(time.perf_counter())

    data, size_lg = expand_grid(data, size_sm)
    solution2 = part2(data, size_lg)
    
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runTest(test_file):
    data, size_sm = parse(test_file)

    test_solution1 = part1( data, size_sm)

    data, size_lg = expand_grid(data, size_sm)
    test_solution2 = part2(data, size_lg )

    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runTest(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

# \ not 3330 to high  
# \ not 2905

# think 2897 answer

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")