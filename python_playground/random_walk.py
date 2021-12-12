import random


def random_walk(n):
    """Return Coordinates after 'n' block random walk
    Version 1.0"""
    x = 0
    y = 0
    for _ in range(n):
        step = random.choice(['N', 'E', 'S', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:  # W
            x -= 1

    return x, y   # () are redundant


def random_walk_2(n):
    """Return Coordinates after 'n' block random walk
    Version 2.0"""
    x, y = 0, 0
    for _ in range(n):
        # simulates the difference in x and y.
        # e.g. if N(orth) X same (0), y inc 1 (1)
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return x, y


# for i in range(25):
#     walk = random_walk_2(10)
#     print(walk, "Distance from home = ",
#           abs(walk[0]) + abs(walk[1]))

number_of_walks = 20000

for walk_length in range(1, 31):
    no_transport = 0 # Number of walks 4 or fewer blocks from home
    for w in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_pct = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, " / % of no transport = ", 100 * no_transport_pct)
