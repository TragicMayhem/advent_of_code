# https://adventofcode.com/2024/day/14

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 231019008
test_file = script_path / "test.txt"  # 0 /
test_file2 = script_path / "test2.txt"  # 12 /

#  220001760 too low

# 231019008

GRID_H = 103
GRID_W = 101


class Robot:
    def __init__(
        self,
        initial_pos,
        vector,
        grid_height=GRID_H,
        grid_width=GRID_W,
    ):
        self.initial_position = initial_pos
        self.vector = vector
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position_history = []
        self.visited_positions = set()
        self.quadrant = None

    def __repr__(self):
        return f"Robot(position={self.initial_position}, velocity={self.vector})"

    def calculate_all_positions(self, num_moves):
        x, y = self.initial_position
        dx, dy = self.vector
        self.visited_positions.add((x, y))

        for _ in range(num_moves):
            x = (x + dx) % self.grid_width
            y = (y + dy) % self.grid_height
            if (x, y) in self.visited_positions:
                # We've encountered a repeating pattern, stop the simulation
                break
            self.position_history.append((x, y))
            self.visited_positions.add((x, y))

    def calculate_final_position(self, num_moves):
        final_x = (
            self.initial_position[0] + num_moves * self.vector[0]
        ) % self.grid_width
        final_y = (
            self.initial_position[1] + num_moves * self.vector[1]
        ) % self.grid_height
        return (final_x, final_y)

    def calculate_final_quadrant(self, num_moves):
        final_x, final_y = self.calculate_final_position(num_moves)
        mid_x = self.grid_width // 2
        mid_y = self.grid_height // 2

        if final_x < mid_x and final_y < mid_y:
            self.quadrant = "top_left"
        elif final_x > mid_x and final_y < mid_y:
            self.quadrant = "top_right"
        elif final_x < mid_x and final_y > mid_y:
            self.quadrant = "bottom_left"
        elif final_x > mid_x and final_y > mid_y:
            self.quadrant = "bottom_right"

    def get_quadrant(self, num_moves):
        if self.quadrant is None:
            self.calculate_final_quadrant(num_moves)
        return self.quadrant

    def get_position_history(self):
        return self.position_history

    def get_unique_positions(self):
        return set(self.position_history)


def parse(puzzle_input, h=GRID_H, w=GRID_W):
    """Parse input"""

    robots = []
    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        for line in file:
            parts = line.strip().split(" ")
            position_str, velocity_str = parts[0], parts[1]

            x, y = map(int, position_str[2:].split(","))
            dx, dy = map(int, velocity_str[2:].split(","))
            robot = Robot((x, y), (dx, dy), h, w)
            robots.append(robot)
    return robots


# def count_robots_in_quadrants(final_positions, grid_width, grid_height):

#     quadrant_counts = {
#         "top_left": 0,
#         "top_right": 0,
#         "bottom_left": 0,
#         "bottom_right": 0,
#     }

#     mid_x = grid_width // 2
#     mid_y = grid_height // 2

#     for x, y in final_positions:
#         if x < mid_x and y < mid_y:
#             quadrant_counts["top_left"] += 1
#         elif x > mid_x and y < mid_y:
#             quadrant_counts["top_right"] += 1
#         elif x < mid_x and y > mid_y:
#             quadrant_counts["bottom_left"] += 1
#         elif x > mid_x and y > mid_y:
#             quadrant_counts["bottom_right"] += 1

#     return quadrant_counts


def count_robots_in_quadrants(robots, num_moves):
    quadrant_counts = {
        "top_left": 0,
        "top_right": 0,
        "bottom_left": 0,
        "bottom_right": 0,
    }

    for robot in robots:
        quadrant = robot.get_quadrant(num_moves)
        if quadrant:  # Check if quadrant is not None
            quadrant_counts[quadrant] += 1

    return quadrant_counts


# def simulate_multiple_robots(robots, num_moves):
#     """Simulates the movement of multiple robots.

#     Args:
#       robots: A list of tuples, each tuple containing (initial_x, initial_y, vector_x, vector_y) for a robot.
#       num_moves: The number of moves to simulate.

#     Returns:
#       A list of lists, where each inner list contains the positions of all robots after a specific move.
#     """

#     positions_history = []
#     for _ in range(num_moves):
#         new_positions = []
#         for robot in robots:
#             x, y, dx, dy = robot
#             x = (x + dx) % 100
#             y = (y + dy) % 100
#             new_positions.append((x, y))
#         positions_history.append(new_positions)
#         robots = new_positions

#     return positions_history


def simulate_multiple_robots(robots, num_moves):
    """Simulates the movement of multiple robots.

    Args:
      robots: A list of Robot objects.
      num_moves: The number of moves to simulate.

    Returns:
      A list of lists, where each inner list contains the positions of all robots after a specific move.
    """

    positions_history = []

    for robot in robots:
        robot.calculate_all_positions(num_moves)
        positions_history.append(robot.get_position_history())

    return positions_history


def calc_multiple_robots_final(robots, num_moves):
    """Simulates the movement of multiple robots.

    Args:
      robots: A list of Robot objects.
      num_moves: The number of moves to simulate.

    Returns:
      A list of lists, where each inner list contains the positions of all robots after a specific move.
    """

    new_positions = []
    for robot in robots:
        new_positions.append(robot.calculate_final_position(num_moves))

    return new_positions


def part1(data, h, w, moves=100):
    """Solve part 1"""

    # print(data)

    # ans = simulate_multiple_robots(data, moves)
    # print(ans)
    # ans2 = calc_multiple_robots_final(data, moves)
    # print(ans2)

    quads = count_robots_in_quadrants(data, moves)

    print(quads)

    product = 1
    for count in quads.values():
        product *= count

    return product


def simulate_and_draw(robots, num_moves, grid_height, grid_width):
    for i in range(num_moves):
        for robot in robots:
            robot.move(1)

        positions = [robot.get_position_history()[-1] for robot in robots]
        draw_grid(positions, grid_height, grid_width)
        print()  # Add a newline between iterations


def draw_grid(positions, grid_height, grid_width):
    """Draws a grid with robots marked as 'x' and empty cells as '.'.

    Args:
      positions: A list of tuples, each representing a robot's position (x, y).
      grid_height: The height of the grid.
      grid_width: The width of the grid.
    """

    grid = [["." for _ in range(grid_width)] for _ in range(grid_height)]
    for x, y in positions:
        grid[y][x] = "x"

    for row in grid:
        print("".join(row))

    return 1


def part2(data, h, w, moves=100):
    """Solve part 2"""

    # simulate_and_draw(data, moves, h, w)

    return 1


def solve(puzzle_input, run="Solution", h=GRID_H, w=GRID_W, moves=100):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input, h, w)

    times.append(time.perf_counter())
    solution1 = part1(data, h, w, moves)
    times.append(time.perf_counter())
    solution2 = part2(data, h, w, moves)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(test_file, run="Test", h=7, w=11, moves=5)
    tests2 = solve(test_file2, run="Test 2", h=7, w=11)

    print()
    solutions = solve(soln_file, h=GRID_H, w=GRID_W, moves=100)
