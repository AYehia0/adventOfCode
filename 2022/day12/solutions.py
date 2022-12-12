import string
from collections import deque

map_rules = string.ascii_lowercase

with open("input.txt") as df:
    data = df.read().splitlines()


def calc_shortest_path_1(grid):

    grid = [list(line) for line in grid]

    # findin the start pos and end pos
    def find_targets(grid):
        """Find the S(start), E(end) and convert them to az"""
        start, end = (0, 0), (0, 0)
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == "S":
                    start = (i, j)
                    grid[i][j] = "a"
                if item == "E":
                    end = (i, j)
                    grid[i][j] = "z"

        return start, end

    def BFS(grid, start, end):
        queue, visited = deque(), set(start)
        queue.append((0, start))

        while queue:
            # pop a node from the queue
            cost, pos = queue.popleft()
            y, x = pos

            # check the neibours nodes
            # all directions
            for dy, dx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                # check boundries
                if dx < 0 or dy < 0 or dx >= len(grid[0]) or dy >= len(grid):
                    continue

                # check if visited before
                if (dy, dx) in visited:
                    continue

                # check if possible to move
                if map_rules.find(grid[dy][dx])-map_rules.find(grid[y][x]) > 1:
                    continue

                if (dy, dx) == end:
                    return cost + 1

                # update the queue and mark as visited
                visited.add((dy, dx))
                queue.append((cost + 1, (dy, dx)))

    start, end = find_targets(grid)
    path = BFS(grid, start, end)

    return path


def calc_shortest_path_2(grid):
    """
    Same as part 1 but moving from the end to the start
    to find the shortest between z --> a (multiple a's)
    """

    grid = [list(line) for line in grid]

    # findin the start pos and end pos
    def find_targets(grid):
        """Find the S(start), E(end) and convert them to az"""
        start, end = (0, 0), (0, 0)
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == "S":
                    start = (i, j)
                    grid[i][j] = "a"
                if item == "E":
                    end = (i, j)
                    grid[i][j] = "z"

        return start, end

    def BFS(grid, start, end):
        queue, visited = deque(), set(start)
        queue.append((0, end))

        while queue:
            # pop a node from the queue
            cost, pos = queue.popleft()
            y, x = pos

            # check the neibours nodes
            # all directions
            for dy, dx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                # check boundries
                if dx < 0 or dy < 0 or dx >= len(grid[0]) or dy >= len(grid):
                    continue

                # check if visited before
                if (dy, dx) in visited:
                    continue

                # check if possible to move
                # reverse since we're tracking from z to a
                if map_rules.find(grid[dy][dx])-map_rules.find(grid[y][x]) < -1:
                    continue

                if grid[dy][dx] == "a":
                    return cost + 1

                # update the queue and mark as visited
                visited.add((dy, dx))
                queue.append((cost + 1, (dy, dx)))

    start, end = find_targets(grid)
    path = BFS(grid, start, end)

    return path


def main():
    ans1 = calc_shortest_path_1(data)
    ans2 = calc_shortest_path_2(data)
    print(f"Part 1 : {ans1}")
    print(f"Part 2 : {ans2}")


if __name__ == "__main__":
    main()
