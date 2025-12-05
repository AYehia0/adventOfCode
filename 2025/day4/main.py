with open("input.txt") as df:
    data = list(map(list, df.read().strip().splitlines()))


"""
    u
  l   r
    d
"""
def part1(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s = 0
            l = grid[i][j-1] if j > 0 else None
            if l == '@':
                s += 1
            r = grid[i][j+1] if j < len(grid[0]) - 1 else None
            if r == '@':
                s += 1
            d = grid[i+1][j] if i < len(grid) - 1 else None
            if d == '@':
                s += 1
            u = grid[i-1][j] if i > 0 else None
            if u == '@':
                s += 1

            # adjecents
            lu = grid[i-1][j-1] if i > 0 and j > 0 else None
            if lu == '@':
                s += 1
            ur = grid[i-1][j+1] if i > 0 and j < len(grid[0]) - 1 else None
            if ur == '@':
                s += 1
            rd = grid[i+1][j+1] if i < len(grid) - 1 and j < len(grid[0]) - 1 else None
            if rd == '@':
                s += 1
            ld = grid[i+1][j-1] if i < len(grid) - 1 and j > 0 else None
            if ld == '@':
                s += 1

            if grid[i][j] == '@' and s < 4:
                ans += 1

    return ans


def remove(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s = 0
            l = grid[i][j-1] if j > 0 else None
            if l == '@':
                s += 1
            r = grid[i][j+1] if j < len(grid[0]) - 1 else None
            if r == '@':
                s += 1
            d = grid[i+1][j] if i < len(grid) - 1 else None
            if d == '@':
                s += 1
            u = grid[i-1][j] if i > 0 else None
            if u == '@':
                s += 1

            # adjecents
            lu = grid[i-1][j-1] if i > 0 and j > 0 else None
            if lu == '@':
                s += 1
            ur = grid[i-1][j+1] if i > 0 and j < len(grid[0]) - 1 else None
            if ur == '@':
                s += 1
            rd = grid[i+1][j+1] if i < len(grid) - 1 and j < len(grid[0]) - 1 else None
            if rd == '@':
                s += 1
            ld = grid[i+1][j-1] if i < len(grid) - 1 and j > 0 else None
            if ld == '@':
                s += 1

            if grid[i][j] == '@' and s < 4:
                ans += 1
                grid[i][j] = '.'

    return ans, grid
    
def part2(grid):
    total = 0
    removed, grid = remove(grid)
    total += removed

    while removed > 0:
        removed, grid = remove(grid)
        total += removed

    return total

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
