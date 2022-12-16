import re

# where the collision happens
Y_AXIS = 10
hashtags_pos = set()
beacons_pos = set()

with open("input.txt") as df:
    data = df.read().splitlines()


def calc_distance(p1, p2):
    #  manhatten distance between (x1,y1) and (x2,y2) is |x1−x2| + |y1−y2|
    # (8, 7) and (2, 10) = |8-2| + |7-10| = 6 + 3 = 9
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_input(data):
    coords = []
    for line in data:
        nums = list(map(int, re.findall(r'-?\d+', line)))
        sensor, beacon = (nums[0], nums[1]), (nums[2], nums[3])
        coords.append([sensor, beacon, calc_distance(sensor, beacon)])
    return coords


def add_empty(sensor, dis, axis_y=Y_AXIS):
    """Add non empty around y axis"""
    x, y = sensor
    # the offset distance
    offset = dis - abs(y - axis_y)
    if offset <= 0:
        return

    low_x = x - offset
    high_x = x + offset

    for i in range(low_x, high_x + 1):
        hashtags_pos.add(i)


def collision(coords):
    """Pretty stupid (brute force solution)"""
    for coord in coords:
        sensor, beacon, dis = coord
        # add area
        add_empty(sensor, dis)

        # add the beacons to subtract later
        if beacon[1] == Y_AXIS:
            beacons_pos.add(beacon[1])

    return len(hashtags_pos - beacons_pos)


def find_distress_beacon(coords):
    """
    https://www.reddit.com/r/adventofcode/comments/zmcn64/comment/j0b90nr/?context=3

    Here's the idea:
    As there is only one missing value,
    it's going to be just outside the boundaries of at least two scanners
    (unless we're incredibly unlucky and it's right on the bounds
     of the 0-4000000 square, but it isn't!).

    The boundary of a scanner is four line segments.
    If a scanner is in position (sx,sy) and has 'radius' r,
    then we want the line segments just outside, i.e. of radius r+1.
    There will be two line segments of gradient 1:

    y = x + sy-sx+r+1
    y = x + sy-sx-r-1

    and two line segments of gradient -1:

    y = -x + sx+sy+r+1
    y = -x + sx+sy-r-1

    Determining where a line y=x+a and a line y=-x+b intersect is very easy :
    they intersect at the point ( (b-a)/2 , (a+b)/2 ).

    One of these intersection points will be the missing scanner location.
    So, we assemble a set of all the 'a' coefficients (lines of gradient 1)
    and all the 'b' coefficients (lines of gradient -1),
    then look at their intersections to see if they are the point we need.
    Given the number of scanners,
    we only need to check a couple of thousand points at most.
    """

    ans = []
    bound = 4_000_000
    neg_lines, pos_lines = [], []
    for (x, y), _, r in coords:
        pos_lines.append(x + y + r + 1)
        pos_lines.append(x + y - r - 1)
        neg_lines.append(y - x + r + 1)
        neg_lines.append(y - x - r - 1)

    # only need to check the intersections of 2 a
    # and diagonals and 2 b diagonals.
    neg_lines = {a for a in neg_lines if neg_lines.count(a) >= 2}
    pos_lines = {b for b in pos_lines if pos_lines.count(b) >= 2}

    for a in neg_lines:
        for b in pos_lines:
            p = ((b-a) // 2, (a+b) // 2)
            if all(0 < c < bound for c in p):
                if all(calc_distance(p, sc) > d for sc, _, d in coords):
                    ans.append((p[0], p[1]))
    return ans[-1]


def main():
    coords = parse_input(data)
    ans1 = collision(coords)
    x, y = find_distress_beacon(coords)
    print(x, y)
    ans2 = x * 4000000 + y

    print(f"Part 1 : {ans1}")
    print(f"Part 2 : {ans2}")


if __name__ == "__main__":
    main()
