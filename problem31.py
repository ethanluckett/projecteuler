

coins = [1, 2, 5, 10, 20, 50, 100, 200]
combinations = {}

def ways_to_get_x(x):
    if x <= 0:
        return ()
    elif x == 1:
        return set([(1,)])
    elif x in combinations:
        return combinations[x]
    else:
        choices = set()
        for c in coins:
            choices.update(tuple(sorted(w + (c, ))) for w in ways_to_get_x(x - c))
        if x in coins:
            choices.add((x,))
        combinations[x] = choices
        return choices

print(len(ways_to_get_x(200)))
# print(combinations)

# this is so inefficient but whatever, it works :c
