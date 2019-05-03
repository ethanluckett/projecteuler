def problem67():
    data = []

    with open('problem67.txt') as f:
        for line in f:
            data.append([int(x) for x in line.strip().split()])

    max_sum = [list(row) for row in data]

    for i, row in enumerate(data):
        if i == 0:
            continue
        for j, col in enumerate(row):
            # j is not the first or last element in row
            if j == 0:
                max_sum[i][j] += max_sum[i-1][j]
            elif j > 0 and j < len(row) - 1:
                max_sum[i][j] += max(max_sum[i-1][j], max_sum[i-1][j-1])
            else:
                max_sum[i][j] += max_sum[i-1][j-1]

    return max(max_sum[-1])


if __name__ == '__main__':
    solution = problem67()
    print(solution)
    assert solution == 997651
