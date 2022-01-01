# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/


# https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4cu5b
# "Part 2 in Python with randomness. Runs hilariously quick."

from random import shuffle
import pathlib

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 576 / 
input_test = script_path / 'input_test.txt'  # 4 distinct in 1 replacements

def parse(puzzle_input):
    """Parse input """

    replacements = []

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        chain = data.pop(-1)

        for d in data:
            if d == '': continue
            tmp = d.split(' => ')
            replacements.append((tmp[0],tmp[1]))

    return chain, replacements    

# reps = [('Al', 'ThF), ...]
# mol = "CRnCaCa..."

mol, reps = parse(input)

print("Input: Chain")   
print(mol)
print("Input: Replacements")   
print(reps)

target = mol
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(reps)

print(part2)  ## 207 