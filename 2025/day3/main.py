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

def part2(banks):
    k = 12
    ans = 0
    for bank in banks:
        stack = []
        n = len(bank)
        print(bank)
        for i, ch in enumerate(bank):
            """
            234234234234278 answer: 434234234278
            ['2']
            ['3']
            ['4']
            ['4', '2']
            ['4', '3']
            ['4', '3', '4']
            ['4', '3', '4', '2']
            ['4', '3', '4', '2', '3']
            ['4', '3', '4', '2', '3', '4']
            ['4', '3', '4', '2', '3', '4', '2']
            ['4', '3', '4', '2', '3', '4', '2', '3']
            ['4', '3', '4', '2', '3', '4', '2', '3', '4']
            ['4', '3', '4', '2', '3', '4', '2', '3', '4', '2']
            ['4', '3', '4', '2', '3', '4', '2', '3', '4', '2', '7']
            ['4', '3', '4', '2', '3', '4', '2', '3', '4', '2', '7', '8']
            """
            while stack and stack[-1] < ch and len(stack) - 1 + (n - i) >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(ch)
            print(stack)
        ans += int(''.join(stack[:k]))
    return ans

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
