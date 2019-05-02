import math

i = 285
next_tn = 0
while next_tn == 0:
    i += 1
    tn = i * (i + 1) // 2

    pent = (math.sqrt(24*tn + 1) + 1) / 6
    hexa = (math.sqrt(8*tn + 1) + 1) / 4 
    if pent == int(pent) and hexa == int(hexa):
        print(tn)
        break
