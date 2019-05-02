
total = 0
for i in range(10000):
    s = str(i + int(str(i)[::-1]))
    for _ in range(49):
        if s == s[::-1]:
            break
        s = str(int(s) + int(s[::-1]))

    if s != s[::-1]:
        total += 1

print(total)