# Random walk
import random


def random_walk(n):
    """ Returns coordinates after n block of random walk """
    x, y = 0, 0
    for _ in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (-1, 0), (1, 0)])
        x += dx
        y += dy
    return x, y


if __name__ == '__main__':
    print(random_walk(19))
