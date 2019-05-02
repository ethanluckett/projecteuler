import math

def get_primes():
    limit = 1000000
    # sieve of eratosthenes
    primes = set(range(2, limit))
    for i in range(int(math.sqrt(limit))):
        if i in primes:
            for j in range(i**2, limit, i):
                primes.discard(j)
    return primes


def distinct_prime_factors(primes, n):
    factors = set()
    while n != 1:
        for p in primes:
            if p > n:
                break
            if n % p == 0:
                factors.add(p)
                n /= p
    return factors


primes = get_primes()


i = 10
lst = [0, 0, 0, 0]
while lst != [4, 4, 4, 4]:
    lst = lst[1:] + [len(distinct_prime_factors(primes, i))]
    i += 1

print(i-4) # i-3 since the lst is [i-4, i-3, i-2, i-1]
