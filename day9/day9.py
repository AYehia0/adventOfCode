import functools

def get_adjacent(grid, i, j):
    """Returns the adjacent of an element in the list"""

    # total width and height
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    adjacents = []

    if i > 0:
        adjacents.append(grid[i-1][j])
    if i+1 < HEIGHT:
        adjacents.append(grid[i+1][j])
    if j > 0:
        adjacents.append(grid[i][j-1])
    if j+1 < WIDTH:
        adjacents.append(grid[i][j+1])

    return adjacents

def part1():
    """Creating a 2D list and checking the adjacent points"""
    with open("input.txt") as file_:

        # converting to a 2D grid of INTs
        grid = [list(map(int, list(in_line))) for in_line in [line.strip('\n') for line in file_.readlines()]]

        low_risks = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(grid[i][j], get_adjacent(grid, i, j))
                if grid[i][j] < min(get_adjacent(grid, i, j)):
                    #print(grid[i][j], get_adjacent(grid, i, j))
                    low_risks.append(grid[i][j])

        print(sum(low_risks) + len(low_risks))

def part2():
    """Creating a 2D list and checking the adjacent points"""
    with open("input.txt") as file_:

        # converting to a 2D grid of INTs
        grid = [list(map(int, list(in_line))) for in_line in [line.strip('\n') for line in file_.readlines()]]

        low_risks = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < min(get_adjacent(grid, i, j)):
                    # only the location is needed
                    low_risks.append((i,j))

        # we now have the points and since each point is a basin itself
        # we can perform BFS

        largest = []
        for low in low_risks:
            # the size of the net
            size = 0
            visited = []
            to_visit = []

            to_visit.append(low)
            while len(to_visit) != 0:

                # getting the point
                next_low = to_visit.pop(0)

                if next_low in visited:
                    continue

                # visiting the curent point
                visited.append(next_low)

                x, y = next_low

                # increase the size since each low is has a size of 1
                size += 1

                # down
                if x - 1 >= 0 and grid[x - 1][y] != 9:
                    down = (x - 1 , y)
                    if down not in visited:
                        to_visit.append(down)
                # up
                if x + 1 < len(grid) and grid[x + 1][y] != 9:
                    up = (x + 1 , y)
                    if up not in visited:
                        to_visit.append(up)

                # left
                if y - 1 >= 0 and grid[x][y - 1] != 9:
                    left = (x, y - 1)
                    if left not in visited:
                        to_visit.append(left)
                # right
                # row ?!
                if y + 1 < len(grid[0]) and grid[x][y + 1] != 9:
                    right = (x, y + 1)
                    if right not in visited:
                        to_visit.append(right)

            # appending to the largest
            largest.append(size)
        print(functools.reduce(lambda x, y: x*y, sorted(largest)[-3:]))

part2()
