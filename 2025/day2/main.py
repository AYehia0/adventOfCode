with open("input.txt") as df:
    data = df.read().strip().split(",")

def is_valid(num):
    mid = len(num) // 2
    return num[0:mid] != num[mid:]

def is_valid_part2(num: str) -> bool:
    return not (num in (num + num)[1:-1])

def part1(readings):
    ans = 0
    for reading in readings:
        id1, id2 = list(map(int, reading.split("-")))
        for i in range(id1, id2+1, 1):
            if not is_valid(str(i)):
                ans += i
    return ans

def part2(readings):
    ans = 0
    for reading in readings:
        id1, id2 = list(map(int, reading.split("-")))
        for i in range(id1, id2+1, 1):
            if not is_valid_part2(str(i)):
                ans += i
    return ans

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
