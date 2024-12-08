def convert_to_numbers(list_of_lists):
    """Converts a list of list of strings into a list of list of integers.

    Args:
        list_of_lists: A list of list of strings.

    Returns:
        A list of list of numbers.
    """
    return [[int(s) for s in inner_list] for inner_list in list_of_lists]


def get_points_between(point1, point2, fixed_coordinate=0):
    """
    Generates a list of points between two given points, fixing either the x or y coordinate.

    Args:
        point1 (tuple): The starting point.
        point2 (tuple): The ending point.
        fixed_coordinate (int, optional): The index of the coordinate to fix (0 for row, 1 for col). Defaults to 0.

    Returns:
        list: A list of points between the two input points.
    """

    print(point1, point2, fixed_coordinate)

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2:
        fixed_coordinate = 0
    elif y1 == y2:
        fixed_coordinate = 1
    else:
        return []

    # Ensure the points are in the correct order based on the fixed coordinate
    if fixed_coordinate == 0:  # Fix x-coordinate
        return [(x, y1) for x in range(min(x1, x2) + 1, max(x1, x2))]
    else:  # Fix y-coordinate
        return [(x1, y) for y in range(min(y1, y2) + 1, max(y1, y2))]


def get_points_between2(point1, point2):
    """Generates a list of points between two given points, taking the shortest path.

    Args:
        point1 (tuple): The starting point.
        point2 (tuple): The ending point.

    Returns:
        list: A list of points between the two input points.
    """

    x1, y1 = point1
    x2, y2 = point2

    # Determine the direction of movement
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the number of steps in each direction
    steps = max(abs(dx), abs(dy))

    # Generate points along the shortest path
    points = []
    for i in range(1, steps + 1):
        new_x = x1 + i * dx // steps
        new_y = y1 + i * dy // steps
        points.append((new_x, new_y))

    return points


# def distance(x1, y1, x2, y2):
#     """Calculates the distance between two points.

#     Args:
#     x1: The x-coordinate of the first point.
#     y1: The y-coordinate of the first point.
#     x2: The x-coordinate of the second point.
#     y2: The y-coordinate of the second point.

#     Returns:
#     The distance between the two points.
#     """
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# def find_new_points(x1, y1, x2, y2):
#     """Finds two new points on the line between the given points, such
#     that the distance from the first point to the new point is double
#     the distance from the second point to the new point.

#     Args:
#     x1: The x-coordinate of the first point.
#     y1: The y-coordinate of the first point.
#     x2: The x-coordinate of the second point.
#     y2: The y-coordinate of the second point.

#     Returns: A tuple containing the coordinates of the two new points.
#     """
#     # Use Tuple for points or unpack (*pt1, *pt2) on the argument list
#     # x1, y1 = point1
#     # x2, y2 = point2

#     # Calculate the distance between the two points
#     d = distance(x1, y1, x2, y2)

#     # Calculate the direction vector from point 1 to point 2
#     dx = x2 - x1
#     dy = y2 - y1

#     # Calculate the unit vector in the direction of the line
#     u = (dx / d, dy / d)  # Calculate the coordinates of the new points

#     new_point1 = (int(x1 + 2 * d * u[0]), int(y1 + 2 * d * u[1]))
#     new_point2 = (int(x1 - d * u[0]), int(y1 - d * u[1]))

#     return new_point1, new_point2


# def manhattan_distance(x1, y1, x2, y2):
#     """Calculates the Manhattan distance between two points on a grid.

#     Args:
#       point1: A tuple representing the coordinates of the first point (x1, y1).
#       point2: A tuple representing the coordinates of the second point (x2, y2).

#     Returns:
#       The Manhattan distance between the two points.
#     """
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)

#     return dx + dy


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


from itertools import product


def generate_combinations(tuples_list):
    """Generates all possible combinations from a list of tuples.

    Args:
      tuples_list: A list of tuples, where each tuple represents a set of choices.

    Returns:
      A list of tuples, each representing a combination of choices.
    """

    return list(product(*tuples_list))


def filter_in_range(tuples_list, height, width):
    """Filters a list of tuples to keep only those within the specified height and width.

    Args:
      tuples_list: A list of tuples, where each tuple represents a point (x, y).
      height: The maximum height of the grid.
      width: The maximum width of the grid.

    Returns:
      A list of tuples that are within the specified height and width.
    """

    return [(x, y) for x, y in tuples_list if 0 <= x < width and 0 <= y < height]


def manhattan_distance(point1, point2):
    """Calculates the Manhattan distance between two points on a grid.

    Args:
      point1: A tuple representing the coordinates of the first point (x1, y1).
      point2: A tuple representing the coordinates of the second point (x2, y2).

    Returns:
      The Manhattan distance between the two points.
    """

    x1, y1 = point1
    x2, y2 = point2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    return dx + dy


# CORRECT
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
