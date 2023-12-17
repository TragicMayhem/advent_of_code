import sys
from pprint import pprint

print("Advent of Code 2020 - Day 6 part 1")

if sys.platform == "linux" or sys.platform == "linux2":
    dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
    dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
    dirpath = sys.path[0] + "\\\\"


filename = "test.txt"
# filename = 'input.txt'

with open(dirpath + filename, "r") as file:
    # Double new line is he seprator so this creates correct lists
    lst = file.read().split("\n\n")  # ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
    # pprint(lst)

    # Now replace \n with '' then split all strings in list.
    # This will be a list of lists (sub lists are all answers for that groups)
    lst = [x.replace("\n", "").split() for x in lst]
    # pprint(lst)

    # Need to make a list (not a list of lists)
    # Unpack lists of lists to form list of strings (answers) in each group
    # e.g. for each l in lst (this will read each sub list within the main list
    #      Then in that sublist loop through each element (one, called x)
    #      [] around this will then form list of the unpacked strings - list of answers
    # Uncomment the pprint statements to see the effect
    list_all_ans = [x for l in lst for x in l]
    # pprint(list_all_ans)

    unique_lst = []
    count = 0

    for x in list_all_ans:
        tmp = set(x)  # set forms unique answers only
        unique_lst.append(tmp)
        count += len(tmp)

print("Total: ", count)
