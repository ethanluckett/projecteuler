import math

limit = 1000000
# sieve of eratosthenes
primes = set(range(2, limit))
for i in range(int(math.sqrt(limit))):
    if i in primes:
        for j in range(i**2, limit, i):
            primes.discard(j)


twice_squares = list(map(lambda x: 2 * x**2, range(1, int(math.sqrt(limit)))))

for i in range(6, limit):
    if i not in primes and i % 2 == 1 and not any(i - sq in primes for sq in twice_squares):
        print(i)
        break