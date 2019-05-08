def ways_to_get_x(coins, mat, x, last_coin):
    if x == 0 or x == 1:
        return x

    if (x, last_coin) in mat:
        return mat[(x, last_coin)]

    # built the "list" of coins in ascending order of value
    # e.g. 5 = 1+2+2 not 2+1+2, etc.
    # this prevents doubly counting the combinations of one "1" and two "2"s
    # filter out coins that are too large or are larger than the last coin we "added"
    total = 0
    for c in filter(lambda c: c >= last_coin and c <= x, coins):
        res = ways_to_get_x(coins, mat, x - c, c)
        total += res

    mat[(x, last_coin)] = total

    return total


def problem31():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    # count the number of ways to have 1 more than 200, but restrict the last coin to '1'
    return ways_to_get_x(coins, {}, 201, 1)


if __name__ == '__main__':
    solution = problem31()
    print(solution)
    assert solution == 73682
