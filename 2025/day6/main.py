from operator import mul
from functools import reduce

with open("input.txt") as df:
    lines = df.read().splitlines()
    data2 = [line.strip("\n") for line in lines]
    data = [line.strip().split() for line in lines]

def part1(data):
    ans = 0
    cols = list(zip(*data))
    for col in cols:
        op = col[-1]
        nums = map(int, col[:-1])
        if op == '*':
            ans += reduce(mul, [n for n in nums])
        if op == '+':
            ans += sum([n for n in nums])

    return ans

def part2(data):
    ans = 0
    cols = list(zip(*data))
    groups = []
    curr = []
    for col in cols[::-1]:
        if set(col) == {" "}:
            groups.append(curr)
            curr = []
        else:
            curr.append(col)
    groups.append(curr)
    for group in groups:
        ans += eval(group[-1][-1].join("".join(a[:-1]) for a in group))
    return ans

def main():
    print("Ans 1:", part1(data))
    print("Ans 2:", part2(data2))

if __name__ == "__main__":
    main()
