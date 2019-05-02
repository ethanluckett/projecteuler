


for den in range(10, 100):
    for num in range(10, den):
        quotient = num/den

        if den % 10 == 0:
            continue

        if (num % 10) / (den % 10) == quotient and num // 10 == den // 10 or \
           (num % 10) / (den // 10) == quotient and num // 10 == den % 10 or \
           (num // 10) / (den % 10) == quotient and num % 10 == den // 10 or \
           (num // 10) / (den // 10) == quotient and num % 10 == den % 10:
           print(num, den)


# 16 / 64
# 26 / 65
# 19 / 95
# 49 / 98

# (1/4) * (2/5) * (1/5) * (1/2) = (2/200) = (1/100)