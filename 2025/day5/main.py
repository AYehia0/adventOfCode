with open("input.txt") as df:
    data = df.read().strip()

def in_range(num, ranges):
    exists = False
    for r in ranges:
        a, b = map(int, r.split('-'))
        if num >= a and b >= num:
            exists = True
            break
    return exists


def part1(data):
    ans = 0
    ranges = data.split('\n\n')[0].splitlines()
    ids = map(int, data.split('\n\n')[1].splitlines())
    for id in ids:
        if in_range(id, ranges):
            ans += 1

    return ans

def part2(data):
    pass

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
