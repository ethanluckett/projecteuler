# sorta cheating and not really an interesting solution

def problem48():
    total = 0
    for i in range(1, 1001):
        total += i**i

    return str(total)[-10:]


if __name__ == '__main__':
    solution = problem48()
    print(solution)
    assert solution == '9110846700'
