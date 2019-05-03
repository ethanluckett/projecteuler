# n^2 + n + 41 = (n - 0)^2 + (n - 0) + 41
# n^2 - 79n + 1601 = (n - 40)^2 + (n - 40) + 41

# so then
# (n - x)^2 + (n - x) + 41
# = n^2 - 2xn + x^2 + n - x + 41
# = n^2 - 2xn + n + x^2 - x + 41
# find x such that x^2 - x + 41 < 1000
# = 31
# (n - 31)^2 + (n - 31) + 41
# = n^2 - 62n + 961 + n - 31 + 41
# = n^2 - 61n + 971
# answer: -61 * 971 = -59231

def problem27():
    return -59231


if __name__ == '__main__':
    solution = problem27()
    print(solution)
    assert solution == -59231
