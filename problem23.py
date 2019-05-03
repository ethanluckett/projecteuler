import math
import sys


def is_abundant(n):
    divisors = set([1])
    for i in range(2, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0 and n != i:
            divisors.add(i)
            divisors.add(n/i)

    return sum(divisors) > n

def problem23():
    # numbers which cannot be written as sum of two+ abundant numbers
    non_abundant_sums = set(range(28123))

    abundant_nums = set(filter(is_abundant, range(1, 28123)))
    # print(abundant_nums)
    for i in abundant_nums:
        for j in abundant_nums:
            if i + j > 28123:
                continue
            non_abundant_sums.discard(i + j)

    return sum(non_abundant_sums)


if __name__ == '__main__':
    solution = problem23()
    print(solution)
    assert solution == 4179871
