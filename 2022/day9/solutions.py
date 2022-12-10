import math

with open("input.txt") as df:
    moves = df.read().splitlines()


def move_tail(h_pos, t_pos):
    """Return the pos of the tail based on the head pos"""

    # print(f"D:{math.sqrt((h_pos[0]-t_pos[0])**2 + (h_pos[1]-t_pos[1])**2)}")
    dis = math.sqrt((h_pos[0]-t_pos[0])**2 + (h_pos[1]-t_pos[1])**2)

    if dis <= math.sqrt(2):
        return t_pos

    # check along X axis
    if abs(h_pos[0] - t_pos[0]) >= 1 and h_pos[1] == t_pos[1]:
        dir = 1 if h_pos[0] > t_pos[0] else -1
        return [t_pos[0] + dir, t_pos[1]]

    # check along Y axis
    if abs(h_pos[1] - t_pos[1]) >= 1 and h_pos[0] == t_pos[0]:
        dir = 1 if h_pos[1] > t_pos[1] else -1
        return [t_pos[0], t_pos[1] + dir]

    dirx = 1 if h_pos[0] - t_pos[0] > 0 else -1
    diry = 1 if h_pos[1] - t_pos[1] > 0 else -1

    return [t_pos[0] + dirx, t_pos[1] + diry]


def simulate_moves_1(moves):
    """
    - The final position.
    - Count the number of moves the tail made uniquly.

    [R 4]
    s(x=0, y=0)
        1- H(1, 0), T(0, 0)
        2- H(2, 0), T(1, 0) VALID
        3- H(3, 0), T(2, 0) VALID
        4- H(4, 0), T(3, 0) VALID --- END

        Total moves for T : 3

    """
    visited = set()
    h_pos, t_pos = [0, 0], [0, 0]
    for move in moves:
        dir, steps = move.split(" ")

        for _ in range(int(steps)):
            if dir == "R":
                h_pos[0] += 1
            if dir == "L":
                h_pos[0] -= 1
            if dir == "U":
                h_pos[1] += 1
            if dir == "D":
                h_pos[1] -= 1

            # move tail
            t_pos = move_tail(h_pos, t_pos)
            visited.add(tuple(t_pos))

    return visited


def simulate_moves_2(moves):
    """
    - The final position.
    - Count the number of moves the tail made uniquly.

    [R 4]
    s(x=0, y=0)
        1- H(1, 0), T(0, 0)
        2- H(2, 0), T(1, 0) VALID
        3- H(3, 0), T(2, 0) VALID
        4- H(4, 0), T(3, 0) VALID --- END

        Total moves for T : 3

    """
    rope = [[0, 0] for _ in range(10)]
    visited = set()
    h_pos, t_pos = [0, 0], [0, 0]
    for move in moves:
        dir, steps = move.split(" ")

        for _ in range(int(steps)):
            if dir == "R":
                rope[0][0] += 1
            if dir == "L":
                rope[0][0] -= 1
            if dir == "U":
                rope[0][1] += 1
            if dir == "D":
                rope[0][1] -= 1

            # move tail
            for i in range(9):
                rope[i + 1] = move_tail(rope[i], rope[i + 1])
                visited.add(tuple(rope[-1]))

    return visited


def main():
    ans1 = simulate_moves_1(moves)
    ans2 = simulate_moves_2(moves)
    print(f"Part 1 : {len(ans1)}")
    print(f"Part 2 : {len(ans2)}")


if __name__ == "__main__":
    main()
