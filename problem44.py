import math

k = 1
lowest_D = 1e100
while k != -1:
    k += 1
    pk = k * (3*k - 1) // 2

    diff = pk - lowest_D
    if diff > 0:
        inverse = int(math.ceil((math.sqrt(24*diff + 1) + 1) / 6))
    else:
        inverse = 0

    start = max(1, inverse)
    if start == k:
        break

    for j in range(start, k):
        pj = j * (3*j - 1) // 2
        s = (math.sqrt(24*(pj+pk) + 1) + 1) / 6
        d = (math.sqrt(24*(pk-pj) + 1) + 1) / 6
        if s == int(s) and d == int(d) and pk-pj < lowest_D:
            lowest_D = pk-pj

print(lowest_D)
