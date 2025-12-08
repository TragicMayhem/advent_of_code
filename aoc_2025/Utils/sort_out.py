import math
import heapq


# new
def get_deltas_8d():
    deltas = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    for r, c in deltas:
        yield (r, c)


# new
def get_deltas_4diag():
    deltas = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    for r, c in deltas:
        yield (r, c)


def get_coords4d(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def get_coords8d(r, c, h, w):
    for delta_r, delta_c in (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def convert_to_numbers(list_of_lists):
    """Converts a list of list of strings into a list of list of integers.

    Args:
        list_of_lists: A list of list of strings.

    Returns:
        A list of list of numbers.
    """
    return [[int(s) for s in inner_list] for inner_list in list_of_lists]


# aoc2024d06
def find_obstacles(data):
    start = None
    positions = []
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell == "#":
                positions.append((r, c))
                continue
            elif cell == "^":
                start = (r, c)

    return (positions, start)


# aoc2024d07 functions with recursion


# aoc2024d08 functions


def find_antinodes(point1, point2):
    """Finds two antinodes on the line connecting the given points.

    Args:
      point1: A tuple representing the coordinates of the first point (x1, y1).
      point2: A tuple representing the coordinates of the second point (x2, y2).

    Returns:
      A list of two tuples, each representing the coordinates of an antinode.
    """

    x1, y1 = point1
    x2, y2 = point2

    # Calculate the vector between the points
    vector_x = x2 - x1
    vector_y = y2 - y1

    # Calculate the antinodes by adding/subtracting the vector from each point
    antinode1 = (x1 - vector_x, y1 - vector_y)
    antinode2 = (x2 + vector_x, y2 + vector_y)

    return [antinode1, antinode2]


def find_antinodes_in_grid(point1, point2, grid_width, grid_height):
    """Finds antinodes on the line connecting the given points within a grid.

    Args:
        p1: A tuple representing the first point (x1, y1).
        p2: A tuple representing the second point (x2, y2).
        grid_width: The width of the grid.
        grid_height: The height of the grid.

    Returns:
        A list of tuples representing the coordinates of the antinodes.
    """
    antinodes = []

    x1, y1 = point1
    x2, y2 = point2

    # Calculate the vector between the points
    vector_x = x2 - x1
    vector_y = y2 - y1

    x, y = point1
    # Extend the line in one direction
    while 0 <= x < grid_width and 0 <= y < grid_height:
        # Add the antinode found
        antinodes.append((x, y))
        x += vector_x
        y += vector_y

    # Reset to the original point and extend in the other direction
    x, y = point2
    while 0 <= x < grid_width and 0 <= y < grid_height:
        # Add the antinode found
        antinodes.append((x, y))
        x -= vector_x
        y -= vector_y

    return antinodes


def filter_in_range(points_list, height, width):
    """Filters a list of tuples to keep only those within the specified height and width.

    Args:
      tuples_list: A list of tuples, where each tuple represents a point (x, y).
      height: The maximum height of the grid.
      width: The maximum width of the grid.

    Returns:
      A list of tuples that are within the specified height and width.
    """

    return [(x, y) for x, y in points_list if 0 <= x < width and 0 <= y < height]


def create_point_dictionary(grid):
    """
    Creates a dictionary of lists of points from a grid of characters.

    Args:
      grid: A list of strings representing the grid.

    Returns:
      A dictionary where keys are characters and values are
      lists of (x, y) tuples representing the points.
    """

    point_dict = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != ".":
                if char not in point_dict:
                    point_dict[char] = []
                point_dict[char].append((x, y))

    return point_dict


# ---
# aoc2024d10


def get_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def filter_zero_height_points(points_with_height):
    """Filters a list of (point, height) tuples, returning only those with height 0."""
    # if (x, y)
    return [point for point, height in points_with_height if height == 0]

    # if ((x, y), h)
    # return [point for row in points_with_height for point, height in row if height == 0]


def filter_zero_height_points_from_grid(grid):
    """Filters a list of (point, height) tuples, returning only those with height 0."""
    zero_points = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 0:
                zero_points.append((r, c))
    return zero_points


# aoc2024d18 A Star


def a_star_search(grid_size, walls, start, end):
    """
    Finds the shortest path between start and end in a grid with dynamic walls.

    Args:
        grid_size: The size of the grid.
        walls: A list of walls, where each wall is a tuple (x, y).
        start: The starting position (x, y).
        end: The end position (x, y).

    Returns:
        A list of coordinates representing the shortest path, or None if no path exists.
    """

    def heuristic(a, b):
        # Manhattan distance heuristic
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(node, walls):
        x, y = node
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [
            (nx, ny)
            for nx, ny in neighbors
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in walls
        ]

    open_set = [(0, 0, heuristic(start, end))]  # (cost, moves, node)
    heapq.heapify(open_set)
    closed_set = set()
    parent = {}

    while open_set:
        cost, moves, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        closed_set.add(current)

        for neighbor in neighbors(current, walls):
            if neighbor not in closed_set:
                new_cost = cost + 1
                new_moves = moves + 1
                if (
                    neighbor not in open_set
                    or new_cost < open_set[open_set.index(neighbor)][0]
                ):
                    heapq.heappush(open_set, (new_cost, new_moves, neighbor))
                    parent[neighbor] = current

        # Add a new wall after each step
        if walls:
            new_wall = walls.pop(0)
            closed_set.add(new_wall)

    return None  # No path found


def can_construct_string(design, components):
    """
    Determines if a design string can be constructed from a word bank.

    Args:
        design: The design string to construct.
        components: A list of words that can be used to construct the design.

    Returns:
        True if the design string can be constructed, False otherwise.
    """

    table = [False] * (len(design) + 1)
    table[0] = True

    for i in range(len(design) + 1):
        if table[i]:
            for word in components:
                if word == design[i : i + len(word)]:
                    table[i + len(word)] = True

    return table[len(design)]


def parse_connections(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        connections = [tuple(line.strip().split("-")) for line in file]
    return connections


def build_connection_dict(connections):
    """
    Builds a dictionary of connections from a list of tuples.
    """
    connection_dict = {}
    for source, target in connections:
        if source not in connection_dict:
            connection_dict[source] = []
        connection_dict[source].append(target)

        if target not in connection_dict:
            connection_dict[target] = []
        connection_dict[target].append(source)
    return connection_dict


import operator


def generic_calculate(data_list):
    """
    Calculates the result of two numbers based on an operator indicator.

    Args:
        data_list (list): A list in the format [num1, num2, operator_indicator].
                          Example: ['10', '20', '*']

    Returns:
        int or float: The result of the operation.
    """
    # Define the mapping of string symbols to actual Python functions
    # operator.add is equivalent to num1 + num2
    # operator.mul is equivalent to num1 * num2
    op_map = {"+": operator.add, "*": operator.mul}

    # 1. Extract and convert numbers (assuming they are strings initially)
    num1 = float(data_list[0])  # Use float to handle both integers and decimals
    num2 = float(data_list[1])

    # 2. Extract the operator indicator
    indicator = data_list[2]

    # 3. Retrieve the corresponding function from the map
    operation_function = op_map.get(indicator)

    if operation_function:
        # 4. Execute the function with the two numbers
        result = operation_function(num1, num2)
        return result
    else:
        # Handle cases where the indicator is not recognized
        raise ValueError(f"Unknown operator indicator: {indicator}")


# # --- Examples ---
# list_add = ["10", "20", "+"]
# list_mul = ["15", "5", "*"]
# list_decimal = ["10.5", "2.5", "+"]

# print(f"Calculation for {list_add}: {generic_calculate(list_add)}")
# print(f"Calculation for {list_mul}: {generic_calculate(list_mul)}")
# print(f"Calculation for {list_decimal}: {generic_calculate(list_decimal)}")


def distance_3d(p1, p2):
    """Calculates the Euclidean distance between two 3D points."""
    return math.dist(p1, p2)


# def build_shortest_path_network(points):
#     """Builds a shortest path network (like a minimum spanning tree) from a list of 3D points."""
#     import networkx as nx

#     G = nx.Graph()

#     # Add all points as nodes
#     for idx, point in enumerate(points):
#         G.add_node(idx, pos=point)

#     # Add edges with weights based on Euclidean distance
#     for i in range(len(points)):
#         for j in range(i + 1, len(points)):
#             dist = distance_3d(points[i], points[j])
#             G.add_edge(i, j, weight=dist)

#     # Compute the minimum spanning tree
#     mst = nx.minimum_spanning_tree(G, weight="weight")
#     return mst


# def build_distance_matrix(points):
#     """Builds a distance matrix for a list of 3D points."""
#     n = len(points)
#     dist_matrix = [[0.0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 dist_matrix[i][j] = distance_3d(points[i], points[j])
#             else:
#                 dist_matrix[i][j] = 0.0

#     return dist_matrix
