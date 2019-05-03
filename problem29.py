def problem29():
    terms = set()

    for i in range(2, 101):
        for j in range(2, 101):
            terms.add(i**j)
    return len(terms)


if __name__ == '__main__':
    solution = problem29()
    print(solution)
    assert solution == 9183
