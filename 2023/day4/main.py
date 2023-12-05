from collections import defaultdict

with open("input.txt") as df:
    data = df.readlines()

def part1(lines):
    ans = 0
    for line in lines:
        line = line.strip()
        _, nums = line.split(": ")
        winning, got = nums.split(" | ")
        winning = [int(i) for i in winning.split(" ") if i != ""]
        got = [int(i) for i in got.split(" ") if i != ""]

        # 4 cards
        profit = 0
        for c in got:
            if c in winning:
                profit += 1

        if profit > 0:
            ans += 2**(profit - 1)

    return ans

def part2(lines):

    played = defaultdict(lambda : 1)
    for card_num, line in enumerate(lines):
        line = line.strip()
        _, nums = line.split(": ")
        winning, got = nums.split(" | ")
        winning = [int(i) for i in winning.split(" ") if i != ""]
        got = [int(i) for i in got.split(" ") if i != ""]

        m = played[card_num]
        profit = 0
        for c in got:
            if c in winning:
                profit += 1

        for p in range(profit):
            played[card_num + 1 + p] += m

    return sum(played.values())

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
