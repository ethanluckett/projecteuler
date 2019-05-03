import itertools


def problem43():
    primes = [2, 3, 5, 7, 11, 13, 17]

    nums = set()
    for perm in itertools.permutations('0123456789'):
        p = int(''.join(perm))
        if all(int(''.join(perm[i:i+3])) % primes[i-1] == 0 for i in range(1, 8)):
            nums.add(p)

    return sum(nums)


if __name__ == '__main__':
    solution = problem43()
    print(solution)
    assert solution == 16695334890
