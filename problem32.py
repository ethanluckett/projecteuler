import itertools


def problem32():
    prods = set()
    for permutation in itertools.permutations('123456789'):
        perm = ''.join(permutation)

        a = int(perm[:1])
        b = int(perm[1:5])
        prod = a * b
        if perm[5:] == str(prod):
            # print(a, b, a*b)
            prods.add(prod)

        a = int(perm[:2])
        b = int(perm[2:5])
        prod = a * b
        if perm[5:] == str(prod):
            # print(a, b, a*b)
            prods.add(prod)

    return sum(prods)


if __name__ == '__main__':
    solution = problem32()
    print(solution)
    assert solution == 45228
