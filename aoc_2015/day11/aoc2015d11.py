# https://adventofcode.com/2015/day/11

import time
import re

# v1 - Seems brute force combinations  (fyi printing steps slows to death)

# Alternatives to implement:
# [x] - Initial check - look left to right, if its invalid char, then increment it, scrap rest to 'a'
# [ ] - When increment if its invalid then skip it (and reset from that possition to 'a')
# [ ] - maybe put debugging and log in here rather than print to see what its doing?

input_pt1 = "hepxcrrq"  # hepxxyzz  > becomes input for part 2
input_pt2 = "hepxxyzz"  # heqaabcc

test_file = [
    "abcddffh",  # abcddffj
    "abcddfah",  # abcddfbb
    "abceefgh",  # abceefhh
    "abdeeghi",  # abdeffaa
    "abcdefgh",  # abcdffaa   From problem
    "ghijklmn",
]  # ghjaabcc   From problem << cant be aabaa


invalid_letter = ["o", "i", "l"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
group3char = list()

lower_char = ord("a")  # 97
upper_char = ord("z")  # 122


def inspect_pwd(pwd):
    """
    Inspect password for invalid characters.
    First one located, increment, and reset rest of chars to 'a'
    """
    tmp_pwd_chars = list()
    for i in range(len(pwd)):
        if pwd[i] in invalid_letter:
            tmp_pwd_chars.append(chr(ord(pwd[i]) + 1))
            tmp_pwd_chars.append("a" * (len(pwd) - i - 1))
            break
        else:
            tmp_pwd_chars.append(pwd[i])

    new_pwd = "".join(tmp_pwd_chars)
    return new_pwd


def change_pwd(pwd):
    """
    Take pwd, increment the last character (and loop until not increasing beyond 'z')
    """
    chars = [ch for ch in pwd]
    i = len(chars) - 1
    chars[i] = chr(ord(chars[i]) + 1)
    # print('\n', chars[i], ord(chars[i]), ord('z'))

    while (ord(chars[i]) > ord("z")) and i > 0:
        # print(i, chars[i])
        chars[i] = "a"
        i -= 1
        chars[i] = chr(ord(chars[i]) + 1)

    new_pwd = "".join(chars)
    return new_pwd


def pwd_valid(pwd):
    """
    Take in string and check against conditions
    As soon as one fails return False
    If passes each then final return is valid password (True)
    """
    # print("\n-----\n     Checking:", pwd)

    # If list is empty then its invalid pwd
    check1 = [chars for chars in group3char if (chars in pwd)]
    if bool(check1) == False:
        # print('\tcheck1',check1)
        return False

    # If anything in list then pwd is invalid
    check2 = [char for char in invalid_letter if (char in pwd)]
    if bool(check2) == True:
        # print('\tcheck2',check2)
        return False

    # MIGHT FAIL IF THE PATTERNS THE SAME _ TO CHECK RULE
    # If the length is <2 then not got two pairs of double-chars
    check3 = re.findall(r"(([a-z])\2)", pwd)  # e.g. [('aa', 'a'), ('cc', 'c')]
    if len(check3) < 2:
        # print('\tcheck3',len(check3), check3)
        return False

    return True


def process_password(data):
    """Solve part 1"""

    for i in range(len(alphabet) - 2):
        combi = alphabet[i : i + 3]
        check_invalid = [char for char in invalid_letter if (char in combi)]
        if not check_invalid:
            group3char.append(combi)

    limit = len(data)
    current_pwd = change_pwd(inspect_pwd(data))

    while not pwd_valid(current_pwd):
        current_pwd = change_pwd(current_pwd)

    # print('Current pwd     :', data)
    # print('Next valid pwd  :', current_pwd)
    return current_pwd


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []
    times.append(time.perf_counter())
    solution = process_password(puzzle_input)
    times.append(time.perf_counter())

    return solution, times


def runAllTests():
    print("\nTests\n")

    a, t = solve(test_file[0])
    print(f"Test1 : {a} in {t[1]-t[0]:.4f}s")

    a, t = solve(test_file[4])
    print(f"Test4 : {a} in {t[1]-t[0]:.4f}s")

    a, t = solve(test_file[5])
    print(f"Test5 : {a} in {t[1]-t[0]:.4f}s")


if __name__ == "__main__":  # print()
    runAllTests()

    sol1, times1 = solve(input_pt1)
    sol2, times2 = solve(input_pt2)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times1[1]-times1[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times2[1]-times2[0]:.4f}s")
    print(f"\nExecution total: {times2[-1]-times1[0]:.4f} seconds")
