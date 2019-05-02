import itertools

prods = set()
for permutation in itertools.permutations('123456789'):
    perm = ''.join(permutation)
    
    a = int(perm[:1])
    b = int(perm[1:5])
    prod = a * b
    if perm[5:] == str(prod):
        print(a, b, a*b)
        prods.add(prod)

    a = int(perm[:2])
    b = int(perm[2:5])
    prod = a * b
    if perm[5:] == str(prod):
        print(a, b, a*b)
        prods.add(prod)

print('sum: {}'.format(sum(prods)))