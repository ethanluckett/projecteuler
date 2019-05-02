

def repeat_len(x):
    # set of quotients and remainders
    qrs = set()
    quotient = -1
    remainder = 0
    dividend = 1
    divisor = x
    i = 0
    # iterate until we hit a duplicate
    while (quotient, remainder) not in qrs:
        if quotient != -1:
            qrs.add((quotient, remainder))
        if dividend < divisor:
            dividend *= 10
        quotient = dividend / divisor
        remainder = dividend % divisor
        dividend = remainder
    return len(qrs)


max_d = 0
max_len = 0
for d in range(1, 1000):
    l = repeat_len(d)
    if l > max_len:
        max_len = l
        max_d = d

print('{} repeats after {} digits'.format(max_d, max_len))