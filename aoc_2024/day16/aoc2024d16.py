# https://adventofcode.com/2024/day/16

import pathlib
import time
import queue

from collections import defaultdict

"""
Reference https://www.redblobgames.com/pathfinding/a-star/introduction.html


"""
script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #
test_file = script_path / "test.txt"  #


# FACING = {
#     "^": (-1, 0),  # Up
#     "v": (1, 0),  # Down
#     "<": (0, -1),  # Left
#     ">": (0, 1),  # Right
# }


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [[x for x in row] for row in file.read().split("\n")]

    h = len(lst)
    w = len(lst[0])
    start_pos = end_pos = None
    walls = set()

    for r, row in enumerate(lst):
        for c, cell in enumerate(row):
            if cell == "#":
                walls.add((r,c))
            elif  cell == "S":
                start_pos = (r,c)
            elif  cell == "E":
                end_pos = (r,c)

    return walls, start_pos, end_pos, h, w


def get_coords_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def get_next_direction(current_value):
    # Turning right each time
    # dirns = [1, 2, 3, 4]  # N, E, S, W
    return (current_value % 4) + 1



def grid_search(grid, start_pos, end_pos):

    h = len(grid)
    w = len(grid[0])

    frontier = queue.PriorityQueue()
    frontier.put(start_pos, 0)

    came_from = {}
    cost_so_far = {}
    came_from[start_pos] = None  
    cost_so_far[start_pos] = 0

    # Construct a map of all possible paths for the startNode across the map
    while not frontier.empty():
        current = frontier.get()  # Get instead of peek, dequeues the item
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
    risk = 0
    risks = []
    currentNode = end_pos
    path = [currentNode]
    while currentNode != start_pos:
        currentNode = came_from[currentNode]
        path.append(currentNode)
        risks.append(grid[currentNode])
        risk += grid[currentNode]

    risks.reverse()
    print()
    print(path)
    print(len(path))
    print(risks)
    print(risk)

    return risk


def part1(data):
    """Solve part 1"""

    return 1


def part2(data):
    """Solve part 2"""

    return 1


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(test_file, run="Test")

    print()
    # solutions = solve(soln_file)
