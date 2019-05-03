import math

def get_primes(limit):
    # sieve of eratosthenes
    primes = set(range(2, limit))
    for i in range(int(math.sqrt(limit))):
        if i in primes:
            for j in range(i**2, limit, i):
                primes.discard(j)
    return primes


def problem50():
    primes = get_primes(1000000)
    primes_lst = sorted(primes)
    max_length = 0
    max_p = 0

    for i, p in enumerate(primes_lst):
        for length in range(max_length, len(primes) - i):
            prime_sum = sum(primes_lst[i:i+length])

            # sum is too large, try next starting p
            if prime_sum > 1000000:
                break

            if prime_sum in primes and length > max_length:
                max_length = length
                max_p = prime_sum

    return max_p


if __name__ == '__main__':
    solution = problem50()
    print(solution)
    assert solution == 997651
