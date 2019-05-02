import math

def get_primes(limit):
    # sieve of eratosthenes
    primes = set(range(2, limit))
    for i in range(int(math.sqrt(limit))):
        if i in primes:
            for j in range(i**2, limit, i):
                primes.discard(j)
    return primes


# are p1, p2, p3 permutations of each other?
def are_permutations(p1, p2, p3):
    p1 = sorted(str(p1))
    p2 = sorted(str(p2))
    p3 = sorted(str(p3))
    return p1 == p2 == p3


primes = list(filter(lambda p: p > 1000, get_primes(10000)))


for i, p in enumerate(primes[:-2]):
    p1 = p
    for j in range(i+1, len(primes)-1):
        p2 = primes[j]
        p3 = p2 + (p2 - p1) # p3 - p2 == p2 - p1
        
        # we have 3 primes with a 
        if p3 in primes and are_permutations(p1, p2, p3):
            print(''.join(map(str, (p1, p2, p3))))