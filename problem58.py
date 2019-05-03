import numpy as np
import random


#https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*np.nonzero(sieve)[0][1::]+1


# this is like problem 28 except the spiral is flipped vertically
def problem58():
    primes = set(primesfrom3to(1000000000))

    prime = 3
    total = 5
    i = 3
    while prime/total >= 0.1:
        i += 2
        
        # top right diagonal
        if (i-1)**2 - i + 2 in primes:
            prime += 1

        # bottom left diagonal
        if i**2 - i + 1 in primes:
            prime += 1

        # top left diagonal
        if (i-1)**2 + 1 in primes:
            prime += 1

        total += 4

    return i


if __name__ == '__main__':
    solution = problem58()
    print(solution)
    assert solution == 26241
