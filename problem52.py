def problem52():
    i = 0
    while True:
        i += 1
        i_digits = sorted(str(i))
        if any(i_digits != sorted(str(i*x)) for x in range(2, 7)):
            continue

        return i


if __name__ == '__main__':
    solution = problem52()
    print(solution)
    assert solution == 142857
