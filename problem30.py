def problem30():
    powers = {str(x): x**5 for x in range(10)}
    total = 0
    for i in range(2, 1000000):
        if i == sum(powers[digit] for digit in str(i)):
            total += i

    return total


if __name__ == '__main__':
    solution = problem30()
    print(solution)
    assert solution == 443839
