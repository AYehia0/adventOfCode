from collections import Counter, defaultdict
from functools import cmp_to_key

with open("input.txt") as df:
    data = df.readlines()

card_order1 = "AKQJT98765432"
card_order2 = "AKQT98765432J"

def cal_rank1(cards, mm):
    # ranks : AAAAA, AA8AA, 23332, TTT98, 23432, AA234, 23456

    for card in cards:
        m = Counter(card)
        s = sorted(m.values())
        if s == [5]:
            mm[card] = 6
        elif s == [1, 4]:
            mm[card] = 5
        elif s == [2, 3]:
            mm[card] = 4
        elif s == [1, 1, 3]:
            mm[card] = 3
        elif s == [1, 2, 2]:
            mm[card] = 2
        elif s == [1, 1, 1, 2]:
            mm[card] = 1
        else:
            mm[card] = 0

    return mm

def cal_rank2(cards, mm):
    # ranks : AAAAA, AA8AA, 23332, TTT98, 23432, AA234, 23456

    for card in cards:
        counts = defaultdict(int)

        js = 0
        for a in card:
            if a == "J":
                js += 1
            else:
                counts[a] += 1

        s = sorted(counts.values())

        # if exist one J with all same
        if js >= 5 or s[-1] + js >= 5:
            mm[card] = 6
        elif js >= 4 or s[-1] + js >= 4:
            mm[card] = 5
        # full house
        elif s[-1] + js >= 3:
            rm_js = s[-1] + js - 3
            if len(s) >= 2 and s[-2] + rm_js >= 2 or rm_js >= 2:
                mm[card] = 4
            else:
                mm[card] = 3

        elif s[-1] + js >= 2:
            rm_js = s[-1] + js - 2
            if len(s) >= 2 and s[-2] + rm_js >= 2 or rm_js >= 2:
                mm[card] = 2
            else:
                mm[card] = 1
        else:
            mm[card] = 0

    return mm

def compare(card1, card2, mm, card_order):
    if mm[card1] == mm[card2]:
        if card1 == card2:
            return 0
        for i, j in zip(card1, card2):
            if card_order.index(i) > card_order.index(j):
                return -1
            if card_order.index(i) < card_order.index(j):
                return 1
        return -1
    if mm[card1] > mm[card2]:
        return 1
    return -1

def part1(lines):
    ans = 0
    mm = {}
    tmp = {}
    cards = []
    for line in lines:
        hand, bid = line.strip().split(" ")
        cards.append(hand)
        mm[hand] = 0
        tmp[hand] = int(bid)
    mm = cal_rank1(cards, mm)
    sorted_mm = sorted(mm.keys(), key=cmp_to_key(lambda x, y: compare(x, y, mm, card_order1)))
    for ind, s in enumerate(sorted_mm):
        ans += tmp[s] * (ind + 1)
    return ans

def part2(lines):
    ans = 0
    mm = {}
    tmp = {}
    cards = []
    for line in lines:
        hand, bid = line.strip().split(" ")
        cards.append(hand)
        mm[hand] = 0
        tmp[hand] = int(bid)
    mm = cal_rank2(cards, mm)
    sorted_mm = sorted(mm.keys(), key=cmp_to_key(lambda x, y: compare(x, y, mm, card_order2)))
    for ind, s in enumerate(sorted_mm):
        ans += tmp[s] * (ind + 1)
    return ans

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
