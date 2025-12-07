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
    raw_ranges = data.split('\n\n')[0].splitlines()
    intervals = []
    for r in raw_ranges:
        a, b = map(int, r.split('-'))
        intervals.append((a, b))

    intervals.sort()

    merged = []
    cur_start, cur_end = intervals[0]

    for a, b in intervals[1:]:
        if a <= cur_end:
            cur_end = max(cur_end, b)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = a, b

    merged.append((cur_start, cur_end))

    ans = 0
    for a, b in merged:
        ans += (b - a + 1)

    return ans

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
