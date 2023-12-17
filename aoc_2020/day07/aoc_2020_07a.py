import sys
import re
from pprint import pprint

print("Advent of Code 2020 - Day 7 part 1")

if sys.platform == "linux" or sys.platform == "linux2":
    dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
    dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
    dirpath = sys.path[0] + "\\\\"


# filename = 'test.txt'  # Answer = 4
filename = "input.txt"  # Answer = 179

search_bag = "shiny gold"
bag_rules = {}  # Dictionary to hold the rules processed from the input file
bag_queue = {
    search_bag
}  # Initialise the queue for later processing.  This will be added to
possible_bags = set()  # initialise as an empty set

with open(dirpath + filename, "r") as file:
    # Replaces plurals and splites the lines to separate parent from children.
    # lst will end as a list of lists (sub lists have 2 parts - 0 = parent and 1 = all chilren in one string)
    lst = file.read().split("\n")
    lst = [
        x.replace("bags", "bag").replace(".", "").split(" bag contain ") for x in lst
    ]

    # pprint(lst)

    # Loop round the sub lists (so x is a list that has parent(0) and then children(1))
    for x in lst:
        if x[1] == "no other bag":
            tmp = []
        else:
            tmp = re.findall(
                r"(\d+) ([\w ]+) bag", x[1]
            )  # RegEx to find all the patterns and groups for (num) (name) bag
            tmp = [
                (b, int(a)) for (a, b) in tmp
            ]  # Convert the groups to a list of tuples with bag name and integer quantity

        # pprint(tmp)

        bag_rules[x[0]] = (
            dict(tmp) if tmp else None
        )  # Dictionary(parent) = a sub dictionary created from the list of tuples
        # pprint(bag_rules[x[0]])

# Initial bag is the search bag so has 1 thing and therefore is True
while bag_queue:
    srch = bag_queue.pop()

    for k, v in bag_rules.items():
        if isinstance(
            v, dict
        ):  # Checks if there is a dictionary for the parent(k) - if so it contains other bags
            if (
                srch in v.keys()
            ):  # Check if the current search back is in the keys of the sub dictionary
                # Means the parent can hold current search bag which is either the target or proven to hold target (at some point)
                # Add the parent to the queue - allows loop to go around again to see what other bags might contain current bag(k)
                # Store k as a bag that could contain the target bag (directly or indirectly through sub bags)
                print(k, "can contain search bag", search_bag)
                bag_queue.add(k)
                possible_bags.add(k)


print("\nPossible bags are:")
pprint(possible_bags)
print(
    f"\n Total number of possible bags to hold '{search_bag}' is {len(possible_bags)}"
)
