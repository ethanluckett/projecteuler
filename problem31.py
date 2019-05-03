def ways_to_get_x(coins, combs, x):
    if x <= 0:
        return ()
    elif x == 1:
        return set([(1,)])
    elif x in combs:
        return combs[x]
    else:
        choices = set()
        for c in coins:
            choices.update(tuple(sorted(w + (c, ))) for w in ways_to_get_x(coins, combs, x - c))
        if x in coins:
            choices.add((x,))
        combs[x] = choices
        return choices


def problem31():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    combs = {}
    return len(ways_to_get_x(coins, combs, 200))


if __name__ == '__main__':
    solution = problem31()
    print(solution)
    assert solution == 73682
