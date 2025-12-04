with open("input.txt") as df:
    data = df.read().strip().splitlines()

def part1(banks):
    total = 0
    for bank in banks:
        j = 0
        m = -1

        for k in range(1, len(bank)):
            tens = int(bank[j])
            ones = int(bank[k])

            curr = tens * 10 + ones
            if curr > m:
                m = curr

            if ones > tens:
                j = k

        total += m

    return total

def part2(readings):
    pass

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
