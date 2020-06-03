# Random walk
import random


def random_walk(n):
    """ Returns coordinates after n block of random walk """
    x = 0
    y = 0
    for _ in range(n):
        choice_r = random.choice(['N', 'S', 'W', 'E'])
        if choice_r == 'N':
            y += 1
        elif choice_r == 'S':
            y -= 1
        elif choice_r == 'W':
            x -= 1
        else:
            x += 1
    return x, y


if __name__ == '__main__':
    print(random_walk(19))
