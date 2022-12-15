from collections import defaultdict

with open("input.txt") as df:
    data = [line.split("->") for line in df.read().splitlines()]

def parse_input(lines):
    points = defaultdict(list)
    for ind, line in enumerate(lines):
        for point in line:
            x, y = list(map(int, point.split(",")))
            points[ind].append((x, y))
    return points
 
def draw_rocks(points):
    # define the location of the rocks using a set
    rocks = set()
    max_depth = 0
    for _, pos in points.items():
        for p1, p2 in zip(pos, pos[1:]):
            x1, x2 = sorted([p1[0], p2[0]])
            y1, y2 = sorted([p1[1], p2[1]])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    rocks.add((x, y))
                    max_depth = max(max_depth, y + 1)

    return rocks, max_depth

def simulate_sand_blocking(lines):
    sands = 0
    points = parse_input(lines)
    blocks, max_depth = draw_rocks(points)
    drop_pos = [500, 0]
    while (500, 0) not in blocks:
        drop_pos = [500, 0]
        while True:
            # check if 
            if drop_pos[1] >= max_depth:
                break
            # drop down
            if (drop_pos[0], drop_pos[1] + 1) not in blocks:
                drop_pos[1] += 1
                continue
            # down to the left
            if (drop_pos[0] - 1, drop_pos[1] + 1) not in blocks:
                drop_pos[0] -= 1
                drop_pos[1] += 1
                continue

            # down to the right 
            if (drop_pos[0] + 1, drop_pos[1] + 1) not in blocks:
                drop_pos[0] += 1
                drop_pos[1] += 1
                continue
            break
        blocks.add(tuple(drop_pos))
        sands += 1

    return sands

def simulate_sand(lines):
    sands = 0
    points = parse_input(lines)
    blocks, max_depth = draw_rocks(points)
    while True:
        drop_pos = [500, 0]
        while True:
            # check if 
            if drop_pos[1] >= max_depth:
                return sands
            # drop down
            if (drop_pos[0], drop_pos[1] + 1) not in blocks:
                drop_pos[1] += 1
                continue
            # down to the left
            if (drop_pos[0] - 1, drop_pos[1] + 1) not in blocks:
                drop_pos[0] -= 1
                drop_pos[1] += 1
                continue

            # down to the right 
            if (drop_pos[0] + 1, drop_pos[1] + 1) not in blocks:
                drop_pos[0] += 1
                drop_pos[1] += 1
                continue
            blocks.add(tuple(drop_pos))
            sands += 1
            break

def main():
    ans1 = simulate_sand(data)
    ans2 = simulate_sand_blocking(data)
    print(f"Part 1 : {ans1}")
    print(f"Part 2 : {ans2}")

if __name__ == "__main__":
    main()
