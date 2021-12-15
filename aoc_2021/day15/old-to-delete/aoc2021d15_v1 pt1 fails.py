# https://adventofcode.com/2021/day/15

'''
Reference https://www.redblobgames.com/pathfinding/a-star/introduction.html

Version 2
- Part 1 works for test not input - too low (584)

'''
import pathlib
import time
import queue

from collections import defaultdict

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 


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

    # print(grid)

    startNode = (0,0)
    goalNode = (size-1,size-1)

    frontier = queue.PriorityQueue()
    frontier.put(startNode, 0)
    came_from = {}
    cost_so_far = {}
    came_from[startNode] = None #Python version of "null"
    cost_so_far[startNode] = 0

    # Construct a map of all possible paths for the startNode across the map
    while not frontier.empty():
        current = frontier.get() # Get instead of peek, dequeues the item
        # print('curr:',current,grid.get(current))

        for neighbour in get_coords_cardinals(*current, size, size):
            # print('neighbour cost',neighbour, grid.get(neighbour))

            new_cost = cost_so_far[current] + grid.get(neighbour)

            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost
                frontier.put(neighbour, priority)
                came_from[neighbour] = current

    # print('came from\n',came_from)
    # Create the path between the startNode and goalNode
    risk=0
    risks=[]
    currentNode = goalNode
    path = [currentNode]
    while currentNode != startNode:
        currentNode = came_from[currentNode]
        path.append(currentNode)
        risks.append(grid[currentNode])
        risk+=grid[currentNode]


    risks.reverse()
    print()
    print(path)
    print(len(path))
    print(risks)
    print(risk)

    return risk


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