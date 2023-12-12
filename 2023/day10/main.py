from collections import deque

with open("input.txt") as df:
    data = df.readlines()

#      North
#West    0    East
#      South

# Symbol : x + yj 
directions = {
    "|": 0 + 1j,   # Upward movement (north)
    "-": 1 + 0j,   # Rightward movement (east)
    "L": 1 + 1j,   # Diagonal movement to the right and up (northeast)
    "J": -1 + 1j,  # Diagonal movement to the left and up (northwest)
    "7": -1 - 1j,  # Diagonal movement to the left and down (southwest)
    "F": 1 - 1j,   # Diagonal movement to the right and down (southeast)
    "S": 0 + 0j    # Starting position
}

def dfs(lines, start):
    seen = set()
    seen.add(start)
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        ch = lines[y][x]

        # going up: if the ch in a pipe when can go up : "|LJ"
        # and the pipe above it can go down : "|7F"
        # and that point(down) not seen before
        if y > 0 and ch in "S|LJ" and lines[y - 1][x] in "|7F" and (x, y - 1) not in seen:
            seen.add((x, y - 1))
            queue.append((x, y - 1))

        # going down
        if y < len(lines) - 1 and ch in "S|7F" and lines[y + 1][x] in "|LJ" and (x, y + 1) not in seen:
            seen.add((x, y + 1))
            queue.append((x, y + 1))

        # going left
        if x > 0 and ch in "S-J7" and lines[y][x - 1] in "-LF" and (x - 1, y) not in seen:
            seen.add((x - 1, y))
            queue.append((x - 1, y))

        # going right
        if x < len(lines[y]) - 1 and ch in "S-LF" and lines[y][x + 1] in "-J7" and (x + 1, y) not in seen:
            seen.add((x + 1, y))
            queue.append((x + 1, y))
    return seen

def part1(lines):
    start = (0, 0)
    for y, line in enumerate(lines):
        for x, pipe in enumerate(line.strip()):
            if pipe == "S":
                start = (x, y)
                break
        else:
            continue
        break

    # furthest point is the length of the loop/2
    return len(dfs(lines, start))//2

def part2(lines):
    """
    Ray casting algorithm: take a point and check the number of the crossing to left or right
        if number of crossing is odd, then it's inside
        if number of crossing is even then it's outside

    We need to check for all the crossing to be part of a loop first, using dfs/bfs
    """
    ans = 0

    start = (0, 0)
    for y, line in enumerate(lines):
        for x, pipe in enumerate(line.strip()):
            if pipe == "S":
                start = (x, y)
                break
        else:
            continue
        break

    def count_crosses(y, x):
        line = lines[y]
        count = 0
        for k in range(x):
            if (k, y) not in seen:
                continue
            count += line[k] in {"J", "L", "|"}
        return count

    seen = dfs(lines, start)

    for y, line in enumerate(lines):
        for x in range(len(lines[0])):
            if (x, y) not in seen:
                crosses = count_crosses(y, x)
                if crosses % 2 == 1:
                    ans += 1

    return ans

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
