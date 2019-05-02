
def is_circular(primes, p):
    p = str(p)
    rot = p[-1] + p[:-1]
    while rot != p:
        if int(rot) not in primes:
            return False
        rot = rot[-1] + rot[:-1]
    return True


# sieve of eratosthenes
primes = set(range(2, 1000000))
for i in range(1000):
    if i in primes:
        for j in range(i**2, 1000000, i):
            primes.discard(j)


circular_primes = list(filter(lambda p: is_circular(primes, p), primes))
print(len(circular_primes))