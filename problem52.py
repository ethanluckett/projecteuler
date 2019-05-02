
i = 0
while True:
    i += 1
    i_digits = sorted(str(i))
    if any(i_digits != sorted(str(i*x)) for x in range(2, 7)):
        continue

    print(i)
    break