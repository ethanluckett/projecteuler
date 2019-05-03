import itertools
import math


def isprime(p):
    for i in range(2, int(math.sqrt(p))):
        if p % i == 0:
            return False
    return True


def problem41():
    max_p = 0
    for i in range(1, 10):
        for perm in itertools.permutations(map(str, range(1, i+1))):
            p = int(''.join(perm))
            if isprime(p) and p > max_p:
                max_p = p

    return max_p


if __name__ == '__main__':
    solution = problem41()
    print(solution)
    assert solution == 7652413
