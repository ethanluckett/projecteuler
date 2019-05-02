import math

total = 0
for exp in range(1, 100):
	for base in range(1, 100):
		if math.ceil(exp * math.log(base) / math.log(10) + 0.00001) == exp:
			total += 1

print(total)