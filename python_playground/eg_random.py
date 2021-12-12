import random

# Print 10 random numbers
for i in range(10):
    print(random.random())


def my_random():
    #  Random, scale, shift, return
    return 4 * random.random() + 3


for i in range(10):
    print(my_random())

# print(help(random.uniform)
# There are other distributions - uniform, standard

# Normal Deviation needs (mean, standard deviation)
print("\nNormal Distribution examples")
for i in range(10):
    print(random.normalvariate(0, 1))

print("\nwide grouping")
for i in range(10):
    print(random.normalvariate(0, 9))

print("\nnarrow grouping")
for i in range(10):
    print(random.normalvariate(0, 0.2))

print("\nRandom Integer - Like a dice roll")
dice_rolls = []
for i in range(20):
    dice_rolls.append(random.randint(1, 6))
else:
    print(dice_rolls)

print("\nRandom choice")
outcomes = ['rock', 'paper', 'scissors']
for i in range(10):
    print(random.choice(outcomes))
