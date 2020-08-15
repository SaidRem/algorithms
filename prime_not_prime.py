import math


def is_prime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True

p = int(input())
for i in range(p):
    x = int(input())

    s = "Prime" if (is_prime(x)) else "Not prime"
    print(s)
