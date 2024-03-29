def is_truncatable(primes, p):
    if p <= 7:
        return False
    pl = str(p)
    pr = str(p)
    while pl != '':
        if int(pl) not in primes or int(pr) not in primes:
            return False
        pl = pl[1:]
        pr = pr[:-1]
    return True


def problem37():
    # sieve of eratosthenes
    primes = set(range(2, 1000000))
    for i in range(1000):
        if i in primes:
            for j in range(i**2, 1000000, i):
                primes.discard(j)

    truncatable_primes = list(filter(lambda p: is_truncatable(primes, p), primes))
    return sum(truncatable_primes)


if __name__ == '__main__':
    solution = problem37()
    print(solution)
    assert solution == 748317
