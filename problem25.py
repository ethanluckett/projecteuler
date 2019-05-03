import math


def fib(fibs, n):
    if n in fibs:
        return fibs[n]
    else:
        if n <= 2:
            fibs[n] = 1
            return 1
        else:
            result = fib(fibs, n-1) + fib(fibs, n-2)
            fibs[n] = result
            return result


def problem25():
    fibs = {}
    n = 2
    while math.log10(fib(fibs, n)) < 999:
        n += 1

    return n


if __name__ == '__main__':
    solution = problem25()
    print(solution)
    assert solution == 4782
