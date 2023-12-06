with open("input.txt") as df:
    data = df.readlines()

def count_winning_cases(duration, record_distance):
    count = 0
    for t in range(duration):
        # find the distance
        d = t * (duration - t)
        if d > record_distance:
            count += 1
    return count

def part1(lines):
    ans = 1

    line1 = lines[0].strip().split(":")[-1]
    line2 = lines[1].strip().split(":")[-1]

    times = [int(i) for i in line1.split(" ") if i]
    dists = [int(i) for i in line2.split(" ") if i]

    for i in range(len(times)):
        c = count_winning_cases(times[i], dists[i])
        ans *= c

    return ans


def part2(lines):
    time = int(lines[0].strip().split(":")[-1].replace(" ", ""))
    distance = int(lines[1].strip().split(":")[-1].replace(" ", ""))

    return count_winning_cases(time, distance)

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
