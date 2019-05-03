def check(x, d):
    s = str(x)
    return x == sum(int(x)**d for x in s)


def problem30():
    total = 0
    for i in range(2, 10000000):
        if check(i, 5):
            total += i

    return total


if __name__ == '__main__':
    solution = problem30()
    print(solution)
    assert solution == 443839
