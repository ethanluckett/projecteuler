from scipy.special import comb


def problem53():
    greater_than_1m = 0

    for c in range(1, 101):
        for r in range(0, c+1):
            if comb(c, r) > 1000000:
                greater_than_1m += 1

    return greater_than_1m


if __name__ == '__main__':
    solution = problem53()
    print(solution)
    assert solution == 4075