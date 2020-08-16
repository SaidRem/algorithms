# Random walk is a mathematical object, known as a stochastic or random process,
# that describes a path that consists of a succession of random steps on some
# mathematical steps such as the integers.
"""
What is the longest random walk you can take
so that on average you will end up 4 blocks
or fewer from home?
"""
import random


def random_walk(n):
    """ Returns coordinates after n block random walk. """
    x, y = 0, 0
    for _ in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (-1, 0), (1, 0)])
        x += dx
        y += dy
    return x, y


if __name__ == '__main__':
    number_of_walks = 20_000
    for walk_length in range(1, 31):
        no_transport = 0        # Number of walks 4 or fewer blocks from home
        for i in range(number_of_walks):
            (x, y) = random_walk(walk_length)
            distance = abs(x) + abs(y)
            if distance <= 4:
                no_transport += 1
        no_transport_percentage = float(no_transport) / number_of_walks
        print(f'Walk size = {walk_length} // %'
              f'of no transport = {100*no_transport_percentage}')
