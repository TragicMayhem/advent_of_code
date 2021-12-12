import random

num_iterations = 10000


print("\nA dice roll", num_iterations)

dice_rolls_counts = [0, 0, 0, 0, 0, 0, 0]
for i in range(num_iterations):
    roll = random.randint(1, 6)
    dice_rolls_counts[roll] += 1
else:
    print(dice_rolls_counts[1:])

print("Total number of rolls:", sum(dice_rolls_counts))