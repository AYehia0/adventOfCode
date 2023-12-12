with open("input.txt") as df:
    data = df.read().strip().splitlines()


def find_dist_factor(lines, expand_factor):
    ans = 0

    galaxies = [(r, c) for r, row in enumerate(lines) for c, ch in enumerate(row) if ch == "#"]

    empty_row = [r for r, row in enumerate(lines) if all(ch == "." for ch in row)]
    empty_col = [c for c, col in enumerate(zip(*lines)) if all(ch == "." for ch in col)]

    for i, (r1, c1) in enumerate(galaxies):
        for (r2, c2) in galaxies[:i]:

            # count with scale for rows ans cols
            for r in range(min(r1, r2), max(r1, r2)):
                ans += expand_factor if r in empty_row else 1

            for c in range(min(c1, c2), max(c1, c2)):
                ans += expand_factor if c in empty_col else 1
    return ans

def part1(lines):
    return find_dist_factor(lines, 2)

def part2(lines):
    return find_dist_factor(lines, 1000000)

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
