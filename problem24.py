#import itertools
#a = itertools.permutations('0123456789', 10)
#print(''.join(list(a)[999999]))

# uses factorial radix
# https://medium.com/@aiswaryamathur/find-the-n-th-permutation-of-an-ordered-string-using-factorial-number-system-9c81e34ab0c8
s = ''.join(map(str, range(10)))
start = 999999
i = 1
fact = []
while start != 0:
    rem = start % i
    start /= i
    fact.insert(0, rem)
    i += 1

result = ''
for i in fact:
    result += s[i]
    s = s[:i] + s[i+1:]

print(result)


