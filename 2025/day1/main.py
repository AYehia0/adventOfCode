with open("input.txt") as df:
    data = df.read().strip().splitlines()

def part1(lines):
    curr = 50
    max = 100
    password = 0
    for line in lines:
        dir, dist = line[0], int(line[1:])
        if dir == 'L':
            curr = (curr - dist) % max
            if curr < 0:
                curr = max + curr
        else:
            curr = (curr + dist) % max
            if curr > max:
                curr = curr - max
        if curr == 0:
            password += 1

    return password

    
def part2(lines):
    pass

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
