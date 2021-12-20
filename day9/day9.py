
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


part1()
