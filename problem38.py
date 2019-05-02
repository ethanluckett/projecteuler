
def is_pandigital(x):
    str_x = str(x)
    return '0' not in str_x and len(str_x) == 9 and len(set(str_x)) == 9



max_prod = 0
for i in range(10000):
    prod = ''
    j = 1
    while len(prod) < 9:
        prod += str(i*j)
        j += 1
    if is_pandigital(prod) and int(prod) > max_prod:
        max_prod = int(prod)

print(max_prod)
