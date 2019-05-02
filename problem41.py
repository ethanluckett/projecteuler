import itertools
import math

def isprime(p):
    for i in range(2, int(math.sqrt(p))):
        if p % i == 0:
            return False
    return True

max_p = 0
for i in range(1, 10):
    print(i)
    for perm in itertools.permutations(map(str, range(1, i+1))):
        p = int(''.join(perm))
        if isprime(p) and p > max_p:
            max_p = p

print(max_p)