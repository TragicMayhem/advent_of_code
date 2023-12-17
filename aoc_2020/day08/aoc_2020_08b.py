import sys
import copy
from pprint import pprint

print("Advent of Code 2020 - Day 8 part 2")

if sys.platform == "linux" or sys.platform == "linux2":
    dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
    dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
    dirpath = sys.path[0] + "\\\\"


# filename = 'test.txt'
filename = "input.txt"


def check_soln(data_copy):
    """
    Check for a solution in the instrctions passed.
    data_copy - list of instructions ['string', integer]
    """
    pnt = acc = 0
    v = []

    # Loop until you find duplicate instruction (pointer already used) or pointer equals length of list
    while (pnt not in v) and (pnt < len(data_copy)):
        v.append(pnt)

        if data_copy[pnt][0] == "nop":
            pnt += 1

        elif data_copy[pnt][0] == "jmp":
            pnt += data_copy[pnt][1]

        elif data_copy[pnt][0] == "acc":
            acc += data_copy[pnt][1]
            pnt += 1

        # print("  pointer is now", pnt, "already visited", len(v), "accumulator =", acc)

    # When the loop ends, if pointer is at the end, correct solution so return True
    if pnt == len(data_copy):
        return (True, acc)

    return (False, acc)  ## Else not valid solution (False)


with open(dirpath + filename, "r") as file:
    lst = file.read().split("\n")
    lst = [x.split() for x in lst]
    lst = [
        [x[0], int(x[1])] for x in lst
    ]  # lst = List of lists, each sub list = [instuction,  integer]
    # pprint(lst)

    accumulator = 0
    candidates_to_change = []

    # Build list from the input of each occurance of nop or jmp
    # These are the instructions that could be at fault
    for i, x in enumerate(lst):
        if x[0] == "nop" or x[0] == "jmp":
            candidates_to_change.append([x[0], i])
    # pprint(candidates_to_change)

    # Loop through the candidates, by swapping the instruction and then testing for solution
    for i, x in enumerate(candidates_to_change):
        # Ensure its a copy not a reference to,
        # Using deepcopy because we are going to alter one of the instructions to test
        working_copy = copy.deepcopy(lst)

        if x[0] == "nop":
            working_copy[x[1]][0] = "jmp"
        else:
            working_copy[x[1]][0] = "nop"

        # Function tests for solution with the new altered instructions.
        # Returns True/False and the running total (accumulator)
        status, accumulator = check_soln(working_copy)
        print(
            "Changing",
            x,
            "the solution status =",
            status,
            " with accumulator =",
            accumulator,
        )

        # If Returned True then found solution so stop checking rest of the candidates
        if status:
            break

print("\nFinal solution status =", status, "with accumulator =", accumulator)
