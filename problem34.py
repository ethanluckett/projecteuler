import math


def problem34():
    nums = filter(lambda i: i == sum(math.factorial(int(x)) for x in str(i)), range(3, 10000000))
    return sum(nums)


if __name__ == '__main__':
    solution = problem34()
    print(solution)
    assert solution == 40730
