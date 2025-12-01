# https://adventofcode.com/2024/day/14

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 231019008 / 8280
test_file = script_path / "test.txt"  # 0 / -
test_file2 = script_path / "test2.txt"  # 12 / -

#  220001760 too low

# {'top_left': 128, 'top_right': 121, 'bottom_left': 132, 'bottom_right': 113}
# Solution 1: 231019008 in 0.0019s


# pt2 is 8280 but cant see in my code

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
        self.quadrant = None
        self.current_position = self.initial_position
        self.current_position_index = 0
        self.__all_positions = None

    def __repr__(self):
        return f"Robot(position={self.initial_position}, velocity={self.vector})"

    def get_initial_position(self):
        return self.initial_position

    def get_vector(self):
        return self.vector

    def __calculate_all_positions(self):
        if self.__all_positions is None:
            visited_positions = set()
            x, y = self.initial_position
            dx, dy = self.vector
            positions = [(x, y)]

            while (x, y) not in visited_positions:
                visited_positions.add((x, y))
                x = (x + dx) % self.grid_width
                y = (y + dy) % self.grid_height
                positions.append((x, y))

            self.__all_positions = positions

    def move_one(self):
        self.__calculate_all_positions()  # Ensure positions are calculated
        self.current_position_index = (self.current_position_index + 1) % len(
            self.__all_positions
        )
        return self.__all_positions[self.current_position_index]

    def get_current_position(self):
        self.__calculate_all_positions()  # Ensure positions are calculated
        return self.__all_positions[self.current_position_index]

    def get_all_positions(self):
        self.__calculate_all_positions()  # Ensure positions are calculated
        return self.__all_positions

    def calculate_position(self, seconds):
        new_pos_x = (
            self.initial_position[0] + seconds * self.vector[0]
        ) % self.grid_width
        new_pos_y = (
            self.initial_position[1] + seconds * self.vector[1]
        ) % self.grid_height
        return (new_pos_x, new_pos_y)

    def calculate_final_quadrant(self, seconds):
        final_x, final_y = self.calculate_position(seconds)
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


def rotate_grid(grid):
    """Rotates a 2D grid 90 degrees clockwise.

    Args:
      grid: A 2D list representing the grid.

    Returns:
      The rotated grid.
    """

    n = len(grid)
    m = len(grid[0])
    rotated_grid = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            rotated_grid[j][n - i - 1] = grid[i][j]

    return rotated_grid


def draw_grid(positions, grid_height, grid_width):
    """Draws a grid with robots marked as 'x' and empty cells as '.'.

    Args:
      positions: A list of tuples, each representing a robot's position (x, y).
      grid_height: The height of the grid.
      grid_width: The width of the grid.
    """

    grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
    for x, y in positions:
        grid[y][x] += 1

        if grid[y][x] > 1:
            return 0

    # grid_str = ["".join(row) for row in grid]
    grid_str = ["".join(str(num) for num in row) for row in grid]

    for row_str in grid_str:
        # if "#####" in row_str:
        #     print(row_str)
        print(row_str)

    time.sleep(0.3)
    print()

    return 1


def part1(data, h, w, seconds=100):
    """Solve part 1"""

    quads = count_robots_in_quadrants(data, seconds)
    print(quads)

    product = 1
    for count in quads.values():
        product *= count

    return product


def part2(robots, h, w, seconds):
    """Solve part 2"""

    seconds = 10000
    limit = 5
    count = 0
    for sec in range(seconds):
        grid = [[0 for _ in range(w)] for _ in range(h)]

        for robot in robots:
            x, y = robot.get_initial_position()
            dx, dy = robot.get_vector()

            new_pos_x = (x + sec * dx) % w
            new_pos_y = (y + sec * dy) % h
            grid[new_pos_y][new_pos_x] += 1

        if not any(any(num > 1 for num in row) for row in grid):
            grid_strings = ["".join(str(num) for num in row) for row in grid]
            print(sec)
            for row_str in grid_strings:
                print(row_str)
            print()
            count += 1
            if count > limit:
                break
            time.sleep(0.3)

    return 1


def solve(puzzle_input, run="Solution", h=GRID_H, w=GRID_W, seconds=100):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input, h, w)

    times.append(time.perf_counter())
    solution1 = part1(data, h, w, seconds)
    times.append(time.perf_counter())
    solution2 = part2(data, h, w, seconds)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds\n")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    # tests = solve(test_file, run="Test", h=7, w=11, seconds=5)
    # tests2 = solve(test_file2, run="Test 2", h=7, w=11)

    print()
    solutions = solve(soln_file, h=GRID_H, w=GRID_W, seconds=100)
