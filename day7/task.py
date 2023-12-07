from collections import Counter
import functools

cardsNum = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0
}

power = {
    "FiveKind": 1,
    "FourKind": 2,
    "FullHouse": 3,
    "ThreeKind": 4,
    "TwoPairs": 5,
    "OnePair": 6,
    "HighCard": 7
}

def rank_lists(lists):
    sorted_lists = sorted(lists, key=lambda x: tuple(x))
    ranking = {tuple(l): i + 1 for i, l in enumerate(sorted_lists)}
    return ranking

def getTotalBid(bid, rank):
    return bid * rank

def getRank(cards):
    count = Counter(cards)
    if 5 in count.values():
        return power["FiveKind"]
    elif 4 in count.values():
        return power["FourKind"]
    elif 3 in count.values() and 2 in count.values():
        return power["FullHouse"]
    elif 3 in count.values():
        return power["ThreeKind"]
    elif list(count.values()).count(2) == 2:
        return power["TwoPairs"]
    elif 2 in count.values():
        return power["OnePair"]
    else:
        return power["HighCard"]

def getTotalBidSum(bidWithRank):
    total_sum = 0
    for bid, rank in bidWithRank.items():
        total_sum += getTotalBid(int(bid), rank)
    return total_sum

def updateRank(cardSet):
    l = []
    if len(cardSet) > 0:
        for card in cardSet:
            l.append([cardsNum[x] for x in card])
        print(rank_lists(l))

def get_hand_type(cards_hand):
    card_counts = Counter(cards_hand)
    kind_counts = tuple(sorted([card_counts[c] for c in card_counts], reverse=True))
    hand_types = ((1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,))
    return hand_types.index(kind_counts) + 1

def get_compare_hands_func(card_values="23456789TJQKA"):
    def card_strength(card):
        try:
            return card_values.index(card)
        except ValueError:
            return float('inf')

    def compare_two_hands(hand_1, hand_2):
        compare_result = 0
        hand1_strength = [card_strength(c) for c in hand_1[0]]
        hand2_strength = [card_strength(c) for c in hand_2[0]]
        for i in range(len(hand_1[0])):
            if hand1_strength < hand2_strength:
                compare_result = -1
                break
        return compare_result

    return compare_two_hands

def get_best_joker_hand(cards_hand):
    temp_hand = cards_hand.replace("J", "")
    cards = Counter(temp_hand)
    best_replacement = sorted([(value, cards[value]) for value in cards],
                               key=lambda t: (-t[1], -("J23456789TQKA".index(t[0]))))[0][0]
    return cards_hand.replace("J", best_replacement)

def process_hands_bids(hands_bids_list, extra_steps=False):
    if extra_steps:
        card_values = "J23456789TQKA"
    else:
        card_values = "23456789TJQKA"

    hands_by_type = dict()
    for hand_type_number in [str(n) for n in range(1, 8)]:
        hands_by_type[hand_type_number] = list()

    for line in hands_bids_list:
        # Split the line into hands and bid
        hands, bid = line.split()
        hand_bid = (hands, int(bid))

        hand_cards = hand_bid[0]
        if extra_steps:
            jokers = hand_cards.count("J")
            if 0 < jokers < 5:
                hand_cards = get_best_joker_hand(hand_cards)
        key = str(get_hand_type(hand_cards))
        hands_by_type[key].append(hand_bid)

    compare_hands_func = get_compare_hands_func(card_values)

    rank = 0
    result = 0
    for key in hands_by_type:
        sorted_hands = sorted(hands_by_type[key],
                              key=functools.cmp_to_key(compare_hands_func))
        for _, bid in sorted_hands:
            rank += 1
            result += (bid * rank)

    print(result)

if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f]

    process_hands_bids(data)
    process_hands_bids(data, True)
