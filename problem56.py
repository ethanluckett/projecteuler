def problem56():
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            s = sum(int(d) for d in str(a**b))
            if s > max_sum:
                max_sum = s

    return max_sum


if __name__ == '__main__':
    solution = problem56()
    print(solution)
    assert solution == 972
