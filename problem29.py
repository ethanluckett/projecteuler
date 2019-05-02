

terms = set()

for i in range(2, 101):
    for j in range(2, 101):
        terms.add(i**j)

print(len(terms))