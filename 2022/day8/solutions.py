with open("input.txt") as df:
    map = [list(map(int, list(item))) for item in df.read().splitlines()]
    print(map)


def is_visible(grid, location):
    x, y = location
    curr_tree = grid[x][y]
    top, down, right, left = 4*[False]

    # check the top
    for i in range(1, x + 1):
        if grid[x - i][y] >= curr_tree:
            top = True
            break

    # check the bottom
    for i in range(1, len(grid) - x):
        if grid[x + i][y] >= curr_tree:
            down = True
            break

    # check the right
    for i in range(1, len(grid[0]) - y):
        if grid[x][y + i] >= curr_tree:
            right = True
            break

    # check the left
    for i in range(1, y + 1):
        if grid[x][y - i] >= curr_tree:
            left = True
            break

    return all([top, down, right, left])


def calc_score(grid, location):
    x, y = location
    curr_tree = grid[x][y]
    top, down, right, left = 4 * [0]

    # check the top
    for i in range(1, x + 1):
        top += 1
        if grid[x - i][y] >= curr_tree:
            break

    # check the bottom
    for i in range(1, len(grid) - x):
        down += 1
        if grid[x + i][y] >= curr_tree:
            break

    # check the right
    for i in range(1, len(grid[0]) - y):
        right += 1
        if grid[x][y + i] >= curr_tree:
            break

    # check the left
    for i in range(1, y + 1):
        left += 1
        if grid[x][y - i] >= curr_tree:
            break
    return right * left * down * top


def main(grid=map):
    ans1 = 0
    best = []
    for row in range(len(grid)):
        for col in range(len(grid[0]) - 1):
            # check the boundries
            best.append(calc_score(grid, (row, col)))
            if row == 0 or row == len(grid) or col == 0 or col == len(grid[0]):
                continue

            print(map[row][col], (row, col))
            if is_visible(grid, (row, col)):
                ans1 += 1

    print(f"Part 1 : {len(grid[0])**2 - ans1}")
    print(f"Part 2 : {max(best)}")


if __name__ == "__main__":
    main()
