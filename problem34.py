import math

nums = filter(lambda i: i == sum(math.factorial(int(x)) for x in str(i)), range(3, 10000000))

print(sum(nums))