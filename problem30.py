

def check(x, d):
    s = str(x)
    return x == sum(int(x)**d for x in s)

total = 0
for i in range(2, 10000000):
    if check(i, 5):
        print(i)
        total += i

print('total: {}'.format(total))