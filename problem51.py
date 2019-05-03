import numpy as np
from collections import Counter


#https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*np.nonzero(sieve)[0][1::]+1


import pytest
@pytest.mark.parametrize('p1,p2,max_diffs', [
    ('56113', '56003', 2),
    ('55103', '56103', 1),
    ('56003', '56113', 2),
    ('56113', '56663', 2)
])
def test_in_same_family(p1, p2, max_diffs):
    assert in_same_family(p1, p2, max_diffs)

@pytest.mark.parametrize('p1,p2,max_diffs', [
    ('50103', '51123', 2),
    ('12345', '54321', 3),
    ('25243', '55243', 2)
])
def test_not_in_same_family(p1, p2, max_diffs):
    assert not in_same_family(p1, p2, max_diffs)



# e.g.
# p1 = 56003, p2 = 56113
# or p1 == 50003, p2 = 50113
# n_diffs == 2
def in_same_family(p1, p2, n_diffs):
    if len(p1) != len(p2):
        return False
    diff_p1 = ''
    diff_p2 = ''
    counted_diffs = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            counted_diffs += 1
            if counted_diffs > n_diffs:
                return False
            if diff_p1 == '':
                diff_p1 = p1[i]
                diff_p2 = p2[i]
            elif p1[i] != diff_p1 or p2[i] != diff_p2:
                return False
    if counted_diffs != n_diffs:
        return False
    return True


# e.g. '772' has 2
def count_duplicates(p):
    counts = [0]*10
    for c in p:
        counts[int(c)] += 1
    return max(counts)


def problem51():
    primes = primesfrom3to(1000000)

    for n in range(2, 8):
        # print('n={}'.format(n))
        # 'valid' primes are primes considered for a particular n
        valid_primes = list(filter(lambda p: count_duplicates(str(p)) >= n, primes))
        valid_primes_set = set(valid_primes)
        primes_str = list(str(p) for p in valid_primes)
        for i, p in enumerate(valid_primes):
            # if we've already checked a prime in this family, skip it

            # find the duplicated digit(s)
            relatives = set()
            most_common = Counter(primes_str[i]).most_common()
            for digit, occurrences in most_common:
                if occurrences < n:
                    break
                for candidate in (primes_str[i].replace(digit, x) for x in '0123456789'):
                    if int(candidate) in valid_primes_set:
                        relatives.add(candidate)

            if len(relatives) >= 8:
                if all(in_same_family(p1, p2, n) for p1 in relatives for p2 in relatives if p1 != p2):
                    # print(p, relatives)
                    return p

            relatives = set()


if __name__ == '__main__':
    solution = problem51()
    print(solution)
    assert solution == 121313
