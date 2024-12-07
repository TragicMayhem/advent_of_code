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
