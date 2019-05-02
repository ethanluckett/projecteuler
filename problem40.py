# s = just over 1m digits
s = ''.join(str(x) for x in range(1, 185186))

d = lambda i: int(s[i-1])

total = 1
for i in range(7):
    total *= d(10**i)

print(total)