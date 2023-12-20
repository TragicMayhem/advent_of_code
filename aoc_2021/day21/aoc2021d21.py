# https://adventofcode.com/2021/day/x

import pathlib
import time
import itertools as its
from collections import Counter
import functools

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 571032     / 49975322685009
test_file = script_path / "test.txt"  # 739785 / 444356092776315

player_stats = {}


target_score_part1 = 1000
target_score_part2 = 21


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        p1_starts = file.readline().rstrip()[-1:]
        p2_starts = file.readline().rstrip()[-1:]

        player_stats["1"] = {
            "id": "Player 1",
            "start": int(p1_starts),
            "pos": int(p1_starts),
            "score": 0,
            "rollcount": 0,
            "moves": [],
            "positions": [],
            "rolls": [],
        }

        player_stats["2"] = {
            "id": "Player 2",
            "start": int(p2_starts),
            "pos": int(p2_starts),
            "score": 0,
            "rollcount": 0,
            "moves": [],
            "positions": [],
            "rolls": [],
        }

    return 1


def next_roll(number_rolls=1000):
    number = 0
    for n in range(1, number_rolls, 3):
        yield n + n + 1 + n + 2
        # yield (n, n+1, n+2)


def part1(data):
    """Solve part 1"""
    roll_count = 0

    current_player = "1"

    while (
        player_stats["1"]["score"] < target_score_part1
        and player_stats["2"]["score"] < target_score_part1
    ):
        for roll_score in next_roll():
            roll_count += 3

            # print('P',player_stats[current_player], 'roll', roll_score)

            # print('roll_score',roll_score)
            move = roll_score % 10 if roll_score > 10 else roll_score
            # print("move",move)

            tmp = player_stats[current_player]["pos"] + move
            new_pos = (
                (player_stats[current_player]["pos"] + move) % 10 if tmp > 10 else tmp
            )

            player_stats[current_player]["pos"] = new_pos
            player_stats[current_player]["score"] += player_stats[current_player]["pos"]
            # player_stats[current_player]['rolls'].append(roll_score)
            # player_stats[current_player]['positions'].append(new_pos)
            # player_stats[current_player]['moves'].append(move)

            if player_stats["1"]["score"] >= target_score_part1:
                break

            if player_stats["2"]["score"] >= target_score_part1:
                break

            current_player = "2" if current_player == "1" else "1"

        # print(player_stats['1'])
        # print(player_stats['2'])
        # print('roll count', roll_count)

        lowest_score = min(player_stats["1"]["score"], player_stats["2"]["score"])
        answer = lowest_score * roll_count

    return answer


###  PART 2 ###

# combi = its.product([1,2,3],[1,2,3],[1,2,3])
combi = its.product([1, 2, 3], repeat=3)  # this is a generator
combi_list = list(combi)  # creates list of the combinations

dice_rolls_combis = [
    sum(d) for d in combi_list
]  # This sums the totals, because thats the way game rolls (3 dice rolls is the move)

universe_dice_rolls = list(
    Counter(dice_rolls_combis).items()
)  # this counts the numbers universes with the same totals, so these can be used in calc wins
# print(universe_dice_rolls)  # [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)] actually static list

# first try 18900 21141 - too low, not calculating the actual universe combinations!! research and adjust code from others
# the numbers passed are the same for both next and other.  this is wrong.


# @functools.lru_cache(maxsize=None)
@functools.lru_cache(maxsize=None)
def check_for_win(
    next_player_pos, other_player_pos, next_player_score, other_player_score
):
    """
    next_player* is the current position and score for the player whos turn it is NEXT
    other_player*  is the other players position and score.

    This will calculate the next players new position and score (copying code from Part 1)
    if this player wins, then the totals for that player are increased
    if not (no winner yet), then this is called with the players SWITCHED to then process other player as next
    """
    # Set to zero, on first call they havent won yet.
    next_player_total_wins = 0
    other_player_total_wins = 0

    # print("Checking...",next_player_pos, other_player_pos, next_player_score, other_player_score)

    # 1. check the sums and position IN THIS UNIVERSE  (omg was overwriting the position without thinking interdimensional)

    # for roll_score in dice_rolls_combis:
    for roll_score, universe_count in universe_dice_rolls:
        tmp_move = next_player_pos + roll_score
        next_player_tmp_pos = tmp_move % 10 if tmp_move > 10 else tmp_move
        next_player_tmp_score = next_player_score + next_player_tmp_pos

        # print("before", "pos", next_player_pos, "score", next_player_score)
        # print("after  roll score", roll_score, "move", tmp_move, "next pos", next_player_tmp_pos, "next score", next_player_tmp_score)

        # 2. check for winner (player next)
        if next_player_tmp_score >= target_score_part2:
            # print("win", next_player_tmp_score)
            # next_player_total_wins += 1   ###  universes!!
            next_player_total_wins += universe_count  # if wins with score, this player will win in the universes (count) too
        else:
            # Carry on down the rabbit hole, and recurse switching the players round (so that other player rolls dice)
            # Remember other hasn't changed, so pass through in the next positions, then pass on next with new score and position (as they just played)
            other_player_tmp_wins, next_player_tmp_wins = check_for_win(
                other_player_pos,
                next_player_tmp_pos,
                other_player_score,
                next_player_tmp_score,
            )

            # here will have returned from recursive call.  That call will return two numbers, the wins per player, in the universe
            # that it was working out.  as you go through the recursion the totals for the universes get multiplied. Each combination makes
            # another set of possibilities (brain aches).  So using the simple counts of universe combinations for the dice rolls you can
            # multiple the universe win totals by the number of times that combinations would happen (as would get the same result)
            next_player_total_wins += next_player_tmp_wins * universe_count
            other_player_total_wins += other_player_tmp_wins * universe_count

        # 3. add up the new win

    # print("first player", next_player_score, "second player", other_player_score)
    return next_player_total_wins, other_player_total_wins


def part2(pos1, pos2):
    """Solve part 2"""

    # calculate all the ways the disc can roll (1,2,3)   (itertools product)
    # the sum of each of them is the roll total for a players go  (sum each of the above - list comprehension)

    # how to process many universes???
    # *NEW* the numbers must be repeated so need to count the repetitions   (Found:  Counter)

    # now need to do recursion.... what to return? whats the lowest level that can return to then sum?
    #   how to store.
    #   how to flip-flop between players
    #   is there an easier way to work out position/score (from part 1 to repeat?)
    #   through recursion need to keep total scores for p1 and p2 or cant be sure of winner or comparison

    #   idea after reading some hints:
    #      so recurse using positions and scores, send all the data and then flip them if no-one won before calling again.

    a, b = check_for_win(pos1, pos2, 0, 0)
    # print(a,b)

    return max(a, b)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(2, 10)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    test_solution2 = part2(4, 8)
    return test_solution1, test_solution2


def runAllTests():
    print("Tests")
    a, b = runTest(test_file)
    print(f"Test1.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":  # print()
    runAllTests()

    solutions = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
