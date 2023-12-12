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

    # dfs
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

    # furthest point is the length of the loop/2
    return len(seen)//2

def part2(lines):
    ans = 0
    return ans

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
