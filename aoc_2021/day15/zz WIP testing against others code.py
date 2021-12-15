# https://adventofcode.com/2021/day/15

import pathlib
import time
import heapq
from collections import defaultdict
from math import inf as INFINITY   ## NEW: I was missing this for the risk checking default value

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 592 / 
input_test = script_path / 'test.txt'  # 40 / 315


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        data=[[int(x) for x in row] for row in data]

    size = len(data)
    return data, size


def build_grid(data):
    grid=defaultdict(int)
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            grid[(r,c)] = cell
    
    size = len(data)
    return grid, size


def expand_grid(data, from_size):
    grid=defaultdict(int)
    
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


    # for r, row in enumerate(expanded_grid):
    #     for c, cell in enumerate(row):
    #         grid[(r,c)] = cell

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

    frontier = [(startNode, 0)]
    risks = defaultdict(lambda: INFINITY) #, {startNode: 0})
    risks[startNode] = 0
    came_from = set()

    # Construct a map of all possible paths for the startNode across the map
    while frontier:
        current, risk = heapq.heappop(frontier)
        # print('curr:',current, risk, 'cost', grid.get(current))

        if current == goalNode:
            print(len(risks),risks)
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
            # newrisk = risk + grid.get(cardinal) 

            if newrisk < risks[cardinal]:
                risks[cardinal] = newrisk
                heapq.heappush(frontier, (cardinal, newrisk))

            # print(frontier[-10:])
            # print(risks)

    return INFINITY  #404


########################################################################################################################

def dijkstra(grid):
    h, w = len(grid), len(grid[0])
    source = (0, 0)
    destination = (h - 1, w - 1)

    # Start with only the source in our queue of nodes to visit and in the
    # mindist dictionary, with distance 0.
    queue = [(0, source)]
    mindist = defaultdict(lambda: INFINITY, {source: 0})
    visited = set()

    while queue:
        # Get the node with lowest distance from the queue (and its distance)
        dist, node = heapq.heappop(queue)

        # If we got to the destination, we have our answer.
        if node == destination:
            return dist

        # If we already visited this node, skip it, proceed to the next one.
        if node in visited:
            continue

        # Mark the node as visited.
        visited.add(node)
        r, c = node

        # For each unvisited neighbor of this node...
        for neighbor in get_coords_cardinals(r, c, h, w):
            if neighbor in visited:
                continue

            # Calculate the total distance from the source to this neighbor
            # passing through this node.
            nr, nc  = neighbor
            newdist = dist + grid[nr][nc]

            # If the new distance is lower than the minimum distance we have to
            # reach this neighbor, then update its minimum distance and add it
            # to the queue, as we found a "better" path to it.
            if newdist < mindist[neighbor]:
                mindist[neighbor] = newdist
                heapq.heappush(queue, (newdist, neighbor))

    # If we ever empty the queue without entering the node == destination check
    # in the above loop, there is no path from source to destination!
    return INFINITY


def tmpcheck():
    with open(input, 'r') as file:
        data = file.read().split('\n')

    grid = list(list(map(int, row)) for row in map(str.rstrip, data))
    # print(grid)
    tmp = dijkstra(grid)
    print(tmp)

    tilew = len(grid)
    tileh = len(grid[0])

    for _ in range(4):
        for row in grid:
            tail = row[-tilew:]
            row.extend((x + 1) if x < 9 else 1 for x in tail)

    for _ in range(4):
        for row in grid[-tileh:]:
            row = [(x + 1) if x < 9 else 1 for x in row]
            grid.append(row)

    tmp = dijkstra(grid)
    print(tmp)
    print('-----------------')

############################################################################################################################################



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
    # initial_size = len(data)

    times.append(time.perf_counter())

    # grid, size = build_grid(data)
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

    tmpcheck()

    # runAllTests()

# \ not 3330 to high  
# \ not 2905

# think 2897 answer

    # solutions = solve(input)
    # print('\nAOC')
    # print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    # print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    # print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")