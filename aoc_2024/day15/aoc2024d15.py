# https://adventofcode.com/2024/day/15

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 1465523
test_file1 = script_path / "test1_sm.txt"  # 2028
test_file2 = script_path / "test2_lg.txt"  # 10092


MOVES = {
    "^": (-1, 0),  # Up
    "v": (1, 0),  # Down
    "<": (0, -1),  # Left
    ">": (0, 1),  # Right
}


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n\n")

    walls = set()
    boxes = set()
    instructions = []
    robot_position = None

    rows = lst[0].split("\n")
    for row_index, row in enumerate(rows):
        for col_index, char in enumerate(row):
            if char == "#":
                walls.add((row_index, col_index))
            elif char == "O":
                boxes.add((row_index, col_index))
            elif char == "@":
                robot_position = (row_index, col_index)

    instructions = list(lst[1].replace("\n", ""))

    return (walls, boxes, robot_position, instructions)


def process_moves(walls, boxes, robot_position, instructions):
    """Processes a list of instructions for the robot using coordinates and vectors.

    Args:
        walls: A list of tuples representing the coordinates of the walls.
        boxes: A list of tuples representing the coordinates of the boxes.
        robot_position: A tuple representing the initial coordinates of the robot.
        instructions: A string of directions/instructions.

    Returns:
        A tuple containing the final position of the robot and the updated list of boxes.
    """

    for instruction in instructions:
        dx, dy = MOVES[instruction]

        new_robot_position = (
            robot_position[0] + dx,
            robot_position[1] + dy,
        )

        if new_robot_position in walls:
            # If a wall then stay where robot is
            continue

        if new_robot_position not in boxes:
            # If the next position is empty, we can move there
            robot_position = new_robot_position
            continue

        # Means a box is in the space where the robot wants to move to.

        movable_boxes = []

        bx, by = new_robot_position
        box_position = (bx, by)

        boxes_to_move = True

        while boxes_to_move:

            if box_position in boxes:
                # New possible box position, if in boxes, then need to move, so add to list
                movable_boxes.append(box_position)
                box_position = (box_position[0] + dx, box_position[1] + dy)
                continue

            boxes_to_move = False

        # Have a list of boxes that could be moveable

        if box_position in walls:
            # If the last box added to the list is wall then just continue, cant move anything
            continue

        # Remove all the old positions, as they can move now following checks
        for b in movable_boxes:
            boxes.discard(b)

        # :'( Have to add the new positions based on the delta AFTER removing all the old ones,
        # or you get discard/remove confusion!
        for b in movable_boxes:
            bx, by = b
            boxes.add((bx + dx, by + dy))
        # Finally robot can move
        robot_position = new_robot_position

    return robot_position, boxes


def part1(data):
    """Solve part 1"""

    walls, boxes, robot_position, instructions = data

    print(walls)
    print(boxes)
    print(robot_position)
    print(instructions)

    final_robot, final_boxes = process_moves(walls, boxes, robot_position, instructions)

    print(final_robot)
    print(final_boxes)

    tot = [100 * r + c for r, c in final_boxes]
    print(tot)

    return sum(tot)


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

    tests = solve(test_file1, run="Test1")
    tests = solve(test_file2, run="Test2")

    print()
    solutions = solve(soln_file)
