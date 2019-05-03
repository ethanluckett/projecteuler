import math


def problem33():
    num_total = 1
    den_total = 1

    for den in range(10, 100):
        for num in range(10, den):
            quotient = num/den

            if den % 10 == 0:
                continue

            if (num % 10) / (den % 10) == quotient and num // 10 == den // 10 or \
            (num % 10) / (den // 10) == quotient and num // 10 == den % 10 or \
            (num // 10) / (den % 10) == quotient and num % 10 == den // 10 or \
            (num // 10) / (den // 10) == quotient and num % 10 == den % 10:
                num_total *= num
                den_total *= den

    return den_total / math.gcd(num_total, den_total)


if __name__ == '__main__':
    solution = problem33()
    print(solution)
    assert solution == 100
