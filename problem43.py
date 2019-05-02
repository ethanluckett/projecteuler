import itertools


primes = [2, 3, 5, 7, 11, 13, 17]

nums = set()
for perm in itertools.permutations('0123456789'):
    p = int(''.join(perm))
    if all(int(''.join(perm[i:i+3])) % primes[i-1] == 0 for i in range(1, 8)):
        print(p)
        nums.add(p)

print(sum(nums))