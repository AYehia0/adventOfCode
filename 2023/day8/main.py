with open("input.txt") as df:
    data = df.read().split("\n\n")

def part1(lines):
    insts = lines[0].strip()
    mm = {}
    for line in lines[1].strip().split("\n"):
        line = line.split(" = ")
        right = line[-1]
        mm[line[0]] = {
            "L": right.split(", ")[0][1:],
            "R": right.split(", ")[1][:-1],
        }

    found = False
    ans = 0
    start = mm["AAA"]
    while not found:
        for inst in insts:
            # go that location
            start = start[inst]

            if start == "ZZZ":
                found = True

            start = mm[start]
            ans += 1

    return ans

def part2(lines):
    insts = lines[0].strip()
    mm = {}
    starting = []
    endings = []
    for line in lines[1].strip().split("\n"):
        line = line.split(" = ")
        right = line[-1]
        left = line[0]

        # finding starting nodes
        if left.endswith("A"):
            starting.append(left)

        if left.endswith("Z"):
            endings.append(left)

        mm[left] = {
            "L": right.split(", ")[0][1:],
            "R": right.split(", ")[1][:-1],
        }
    print(starting, endings)

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
