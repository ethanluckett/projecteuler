def problem57():
    num = 3
    den = 2
    numerator_longer = 0
    for i in range(999):
        prev_den = den
        prev_num = num
        num = prev_den * 2 + prev_num
        den = prev_num + prev_den
        if len(str(num)) > len(str(den)):
            numerator_longer += 1

    return numerator_longer


if __name__ == '__main__':
    solution = problem57()
    print(solution)
    assert solution == 153
