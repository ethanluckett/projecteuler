import math
# c is at most p//2
# c is at least p * (sqrt(2) / (1 + 1 + sqrt(2)))


def num_triangles(p):
    count = 0
    min_p = int(p * math.sqrt(2) / (1 + 1 + math.sqrt(2)))
    max_p = p // 2
    for c in range(min_p, max_p + 1):
        ab = p - c
        for a in range(1, ab//2):
            b = math.sqrt(c**2 - a**2)
            if b == int(b) and a + b + c == p:
                count += 1
    return count


def problem39():
    # print(num_triangles(120))
    max_p = 0
    max_n = 0
    for p in range(12, 1001):
        n = num_triangles(p)
        if n > max_n:
            max_n = n
            max_p = p

    return max_p


if __name__ == '__main__':
    solution = problem39()
    print(solution)
    assert solution == 840
