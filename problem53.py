from scipy.special import comb

greater_than_1m = 0

for c in range(1, 101):
    for r in range(0, c+1):
        if comb(c, r) > 1000000:
            greater_than_1m += 1

print(greater_than_1m)