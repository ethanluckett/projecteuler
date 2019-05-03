import pytest

# highest, 1p, 2p, 3ofakind, straight, flush, fullhouse, fourofakind, straightflush, royal
@pytest.mark.parametrize('hand,values', (
(['8C', 'TS', 'KC', '9H', '4S'], (13,  0,  0,  0,  0,  0,  0,  0,  0,  0)),
(['5C', 'AD', '5D', 'AC', '9C'], (14, 14, 14,  0,  0,  0,  0,  0,  0,  0)),
(['3H', '7H', '6S', 'KC', 'JS'], (13,  0,  0,  0,  0,  0,  0,  0,  0,  0)),
(['TH', '8H', '5C', 'QS', 'TC'], (12, 10,  0,  0,  0,  0,  0,  0,  0,  0)),
(['7C', '5H', 'KC', 'QH', 'JD'], (13,  0,  0,  0,  0,  0,  0,  0,  0,  0)),
(['5H', 'KS', '9C', '7D', '9H'], (13,  9,  0,  0,  0,  0,  0,  0,  0,  0)),
(['6H', '4H', '5C', '3H', '2H'], (6,   0,  0,  0,  6,  0,  0,  0,  0,  0)),
(['TD', '8C', '4H', '7C', 'TC'], (10, 10,  0,  0,  0,  0,  0,  0,  0,  0)),
(['7C', '9C', '6D', 'KD', '3H'], (13,  0,  0,  0,  0,  0,  0,  0,  0,  0)),
(['JC', '6S', '5H', '2H', '2D'], (11,  2,  0,  0,  0,  0,  0,  0,  0,  0)),
(['JH', '6H', '5H', '3H', '2H'], (11,  0,  0,  0,  0,  1,  0,  0,  0,  0)),
(['TD', '4C', '4H', 'TH', 'TC'], (10, 10, 10, 10,  0,  0, 10,  0,  0,  0)),
(['JC', '2S', '2C', '2H', '2D'], (11,  2,  0,  2,  0,  0,  0,  2,  0,  0)),
(['6H', '4H', '5H', '3H', '2H'], (6,   0,  0,  0,  6,  1,  0,  0,  6,  0)),
(['AH', 'KH', 'QH', 'JH', 'TH'], (14,  0,  0,  0, 14,  1,  0,  0, 14,  1))))
def test_winning_functions(hand, values):
    functions = [highest_card, one_pair, two_pair,
                 three_of_a_kind, straight, flush, full_house,
                 four_of_a_kind, straight_flush, royal_flush]

    assert tuple(fn(hand) for fn in functions) == values


def card_value(x):
    try:
        value = int(x[0])
    except ValueError:
        if x[0] == 'T':
            value = 10
        elif x[0] == 'J':
            value = 11
        elif x[0] == 'Q':
            value = 12
        elif x[0] == 'K':
            value = 13
        elif x[0] == 'A':
            value = 14
    return value


def sorted_values(hand):
    return sorted(map(card_value, hand))


def highest_card(hand):
    return sorted_values(hand)[-1]


def pairs(hand):
    values = sorted_values(hand)
    pairs = []
    for i in range(1, 5):
        if values[i] == values[i-1] and values[i] not in pairs:
            pairs.append(values[i])
    return pairs


def one_pair(hand):
    p = pairs(hand)
    return max(p) if len(p) >= 1 else 0


def two_pair(hand):
    p = pairs(hand)
    return max(p) if len(p) == 2 and p[0] != p[1] else 0


def three_of_a_kind(hand):
    values = sorted_values(hand)
    for i in range(2, 5):
        if values[i] == values[i-1] == values[i-2]:
            return values[i]
    return 0


def straight(hand):
    values = sorted_values(hand)
    for i in range(1, 5):
        if values[i] - values[i-1] != 1:
            return 0
    return values[-1]


def flush(hand):
    for i in range(1, 5):
        if hand[i][1] != hand[0][1]:
            return 0
    return 1


def full_house(hand):
    return three_of_a_kind(hand) and two_pair(hand)


def four_of_a_kind(hand):
    v = sorted_values(hand)
    if v[0] == v[1] == v[2] == v[3]:
        return v[0]
    elif v[1] == v[2] == v[3] == v[4]:
        return v[1]
    return 0


def straight_flush(hand):
    if straight(hand) and flush(hand):
        return sorted_values(hand)[-1]
    return 0


def royal_flush(hand):
    values = sorted_values(hand)
    return straight_flush(hand) and values[0] == 10


def problem54():
    hands = [(line.split()[:5], line.split()[5:]) for line in open('problem54.txt').read().strip().split('\n')]

    ranks = [royal_flush, straight_flush, four_of_a_kind, full_house, flush,
                straight, three_of_a_kind, two_pair, one_pair, highest_card]
    p1_wins = 0
    for hand in hands:
        p1_hand = tuple(fn(hand[0]) for fn in ranks)
        p2_hand = tuple(fn(hand[1]) for fn in ranks)
        for i in range(len(ranks)):
            if p1_hand > p2_hand:
                p1_wins += 1
                break

    return p1_wins


if __name__ == '__main__':
    solution = problem54()
    print(solution)
    assert solution == 376
