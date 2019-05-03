import math


def problem42():
    with open('problem42.txt') as f:
        strip_quotes = lambda w: w[1:-1]
        word_value = lambda w: sum(ord(c) - 64 for c in w)
        word_vals = list(map(word_value, map(strip_quotes, f.read().split(','))))

    max_word_value = max(word_vals)
    max_t = int(0.5 * (math.sqrt(8*max_word_value + 1) - 1))
    t_nums = set(map(lambda x: int(0.5 * x * (x+1)), range(max_t)))

    count = 0
    for w in word_vals:
        if w in t_nums:
            count += 1

    return count


if __name__ == '__main__':
    solution = problem42()
    print(solution)
    assert solution == 162
