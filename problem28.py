
N = 1001
total = 1

for i in range(3, N+1, 2):
    # top right diagonal
    total += i**2

    # top left diagonal
    total += i**2 - i + 1

    # bottom left diagonal
    total += (i-1)**2 + 1

    # bottom right diagonal
    total += (i-1)**2 - i + 2

print(total)
