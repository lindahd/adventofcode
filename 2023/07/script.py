from collections import Counter
from functools import cmp_to_key

inputs = open("input").read().splitlines()

bids = {x.split()[0]: int(x.split()[1]) for x in inputs}

types = ['five', 'four', 'full', 'three', '2-pair', '1-pair', 'nada']
index_type_map = {key: i for i, key in enumerate(types)}


def find_type(hand):
    count = Counter(hand)
    if 3 in count.values():
        if 2 in count.values():
            return 'full'
        else:
            return 'three'
    elif 4 in count.values():
        return 'four'
    elif 5 in count.values():
        return 'five'
    elif 2 in count.values():
        if Counter(count.values())[2] == 2:
            return '2-pair'
        else:
            return '1-pair'
    else:
        return 'nada'


def find_best_type(hand):
    # consider Joker's
    possibles_types = {}
    for c in order:
        hand_r = hand.replace('J', c)
        possibles_types[hand_r] = find_type(hand_r)
    hands_sort = dict(sorted(possibles_types.items(), key=cmp_to_key(compare_by_type), reverse=True))
    return list(hands_sort.values())[-1]


def compare_by_hand(hand1, hand2) -> int:
    for i in range(5):
        p1 = index_card_map[hand1[i]]
        p2 = index_card_map[hand2[i]]
        if p1 != p2:
            return p1 - p2
    return 0


def compare_by_type(hand_type_1, hand_type_2):
    if index_type_map[hand_type_1[1]] == index_type_map[hand_type_2[1]]:
        return compare_by_hand(hand_type_1[0], hand_type_2[0])
    else:
        return index_type_map[hand_type_1[1]] - index_type_map[hand_type_2[1]]


def compute_day(part):
    find_function = find_type if part == 1 else find_best_type
    hands_types = {hand: find_function(hand) for hand in bids.keys()}
    hands_sort = dict(sorted(hands_types.items(), key=cmp_to_key(compare_by_type), reverse=True))
    return sum([bids[hand] * (i + 1) for i, hand in enumerate(hands_sort.keys())])


for part in [1, 2]:
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] if part == 1 \
        else ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    index_card_map = {key: i for i, key in enumerate(order)}

    print(f"result part {part}: {compute_day(part)}")
