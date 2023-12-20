import pathlib
import re
from typing import final
import ast
from itertools import permutations

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 3488 / 4583
test_file2 = script_path / "test2.txt"  # 3488 / 3805
test_file3 = script_path / "test3.txt"  # 4140 / 3993


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lines = file.read().replace(" ", "").split("\n")
        # print(lines)
    return lines


##### PATTERNS #####
two_digits_pattern = re.compile("(\d{2})")
find_digit = re.compile(r"(\d+)")
find_last_digit = re.compile(r"(\d+)(?!.*\d)")
find_digit_pair = re.compile(r"(\d+)[, ]+(\d+)")


def make_new_split(big_number):
    ln = big_number // 2
    rn = big_number - ln
    new = "[" + str(ln) + "," + str(rn) + "]"
    return new


def explode_node(data_in, current_pos):
    # need to find number left (or start of string)
    # need to find number right
    # add and replace those numbers at those positions
    # replace this one with 0

    pair = find_digit_pair.search(data_in[current_pos:])
    if pair:
        num_explode_to_left, num_explode_to_right = pair.groups()
        start, end = pair.span()
    # print("  exploding at pos",current_pos, 'nums', num_explode_to_left, num_explode_to_right, 'pos',start,end)

    to_the_left = data_in[:current_pos]
    to_the_right = data_in[current_pos + end :]

    next_left_num_pos = find_last_digit.search(to_the_left)
    next_right_num_pos = find_digit.search(to_the_right)

    if next_left_num_pos:
        start, end = next_left_num_pos.span()
        new_number = int(to_the_left[start:end]) + int(num_explode_to_left)
        new_left = re.sub(find_last_digit, str(new_number), to_the_left, count=1)[:-1]
    else:
        # cant find a number to the left, so need to keep it and remove bracket!
        new_left = to_the_left[:-1]

    if next_right_num_pos:
        start, end = next_right_num_pos.span()
        new_number = int(to_the_right[start:end]) + int(num_explode_to_right)
        new_right = re.sub(find_digit, str(new_number), to_the_right, count=1)[1:]
    else:
        # cant find number to the right so need to keep string and remove first bracket
        new_right = to_the_right[1:]

    # print('  new left:', new_left,' new right:',new_right)
    data_out = new_left + "0" + new_right
    return data_out


def collapse_next(data_in):
    depth = 0

    # I think you do explodes first. then splits. I think.  hard to tell if always do leftmost change first?!?!
    for current_pos in range(len(data_in)):
        if data_in[current_pos] == "[":
            depth += 1
        elif data_in[current_pos] == "]":
            depth -= 1
        elif depth == 5:
            # If it goes 5 deep, then need to explode and this will stop this loop and re-start
            return explode_node(data_in, current_pos)

    # Here means there are no more explosions. so now to check for big numbers and replace.
    big_numbers = two_digits_pattern.search(data_in)

    if big_numbers:
        # print('  splitting',big_numbers.group(0))
        return re.sub(
            two_digits_pattern,
            make_new_split(int(big_numbers.group(0))),
            data_in,
            count=1,
        )

    return False


def reduce_input(data_in):
    answer = data_in.pop(0)  # Get initial answer as first element

    for i, elem in enumerate(data_in):
        answer = "[" + answer + "," + elem + "]"

        while True:  # and c < 25:
            # print('\nprocess', answer)
            tmp_answer = collapse_next(answer)
            # print(tmp_answer)

            if tmp_answer == False:
                break
            else:
                answer = tmp_answer

    # print()
    # print('final reduction')
    # print(answer)
    return answer


def calc_mag(reduced_data):
    if isinstance(reduced_data, list):
        left = reduced_data[0]
        right = reduced_data[1]

        return 3 * calc_mag(left) + 2 * calc_mag(right)
    else:
        return reduced_data


print("<" * 25, "TEST", ">" * 25)

input_data = parse(test_file3)
print(input_data)
print()
final_reduction = reduce_input(input_data)
final_list = ast.literal_eval(final_reduction)

# print(final_list)
mag = calc_mag(final_list)
print(mag)

print("-" * 50)

t1 = ["[[[5,[2,8]],4],[5,[[9,9],0]]]", "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]"]
t2 = [
    "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
    "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
]
t_fr = reduce_input(t2)
print(t_fr)
print(calc_mag(ast.literal_eval(t_fr)))

print("<" * 25, "INPUT", ">" * 25)

input_data = parse(soln_file)
# print(input_data)

final_reduction_perms = []
possible_magnitudes = []
perms = []
results = []

for p in permutations(input_data, 2):  # All permutations of 2 fish numbers
    perms.append(p)
    fr = reduce_input(list(p))
    final_reduction_perms.append(fr)
    mag = calc_mag(ast.literal_eval(fr))
    possible_magnitudes.append(mag)
    results.append([p, fr, mag])

# print(perms)
print("_" * 50)
# print(perms[0])
# print(perms[1])
# print(len(perms))

# for p in perms:
#     fr = reduce_input(list(p))
#     final_reduction_perms.append(fr)
#     mag = calc_mag(ast.literal_eval(fr))
#     possible_magnitudes.append(mag)
#     results.append([fr,mag])

# print(results)
print()
# print(final_reduction_perms[0])
# print(final_reduction_perms[1])
print(len(final_reduction_perms))

possible_magnitudes.sort(reverse=True)
# print(possible_magnitudes)
print(possible_magnitudes[0:2])


print("########## AD HOC ###########")
test1 = "[[1, 2], [[1, 2], 3], [9, [8, 7]], [[1, 9], [8, 5]], [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]]"
test2 = "[[1, 2], [[1, 12], 3], [9, [8, 7]], [[1, 19], [8, 15]], [[[[1, 2], [13, 4]], [[5, 6], [7, 8]]], 9]]"

# print(test2)
# tmp = find_digit_pair.search(test2)
# if tmp:
#     print(tmp.span())
#     print(tmp.group(0))
#     print(tmp.groups())


# print(test2)
# output = test2
# big_numbers = two_digits_pattern.search(output)

# while big_numbers:
#     print('\n',big_numbers.span())
#     start, end = big_numbers.span()
#     print('s',start,'e', end,'n', big_numbers.group(0))
#     # print(remaining[start:end])

#     output = re.sub(r'(\d{2})', make_new_split(int(big_numbers.group(0))), output, count=1)
#     print('  o:', output)
#     big_numbers = two_digits_pattern.search(output)

# print(test2)
# print(output)

# # big_numbers = two_digits_pattern.search(test2)
# # print(big_numbers.span())

# find_digits = re.compile(r'(\d+)')

# # print(find_digits.findall(test1))
# # print(find_digits.findall(test1)[::-1])
# next_left_num_pos = find_digits.findall('[[1, 2], [[1, 2], 3], [9, [8, 7]], [[1,')
# print(next_left_num_pos)
# tmp= find_last_digit.search('[[1, 2], [[1, 2], 3], [9, [8, 7]], [[1,')
# if tmp:
#     print(tmp.group(0))
#     print(tmp.span())
