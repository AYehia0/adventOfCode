from collections import deque

with open("input.txt") as df:
    data = df.read().strip().splitlines()

def part1(data):

    def add_beam(i, j):
        if (i, j) not in seen:
            beams.append((i, j))
            seen.add((i, j))
    ans = 0
    beams = deque()
    s = (-1, -1)
    for i in range(len(data)):
        for j in range(len(data[0]) - 1):
            char = data[i][j]
            if char == 'S':
                s = (i, j)
    beams.append(s)
    seen = set()

    while len(beams) > 0:
        k, l = beams.popleft()
        if data[k][l] == '.' or data[k][l] == 'S':
            if k == len(data[0]) - 1: continue
            add_beam(k + 1, l)
        if data[k][l] == '^':
            ans += 1
            add_beam(k, l + 1)
            add_beam(k, l - 1)

    return ans

def part2(data):
    pass

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
