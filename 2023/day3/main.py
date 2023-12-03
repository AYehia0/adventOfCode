import math

with open("input.txt") as df:
    data = df.readlines()

def scan_input(lines):
    special = {} # for special chars
    mm = {} # for holding numbers with their corresponding indexes
    for y, line in enumerate(lines):
        num = ""
        for x, ch in enumerate(line.strip()):
            if not ch.isdigit() and ch != ".":
                special[(x, y)] = ch
                if num != "":
                    mm[(x, y)] = num
                    num = ""
            elif ch.isdigit():
                num += ch
            else:
                if num != "":
                    mm[(x, y)] = num
                num = ""
        if num != "":
            mm[(x, y)] = num
    return mm, special

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def part1(data):
    mm, special = scan_input(data)
    ans = 0
    for point, num in mm.items():
        for special_ind in special:
            # check the distace from the start
            start = abs(point[0] - len(num))
            for dx in range(len(num)):
                p = (start + dx, point[1])
                d = calculate_distance(p, special_ind)
                if d <= math.sqrt(2):
                    ans += int(num)
                    break
    return ans

def part2(data):
    mm, special = scan_input(data)
    ans = 0
    for special_ind, sp_ch in special.items():
        nums = []
        for point, num in mm.items():
            # check the distace from the start
            if sp_ch != "*":
                continue

            start = abs(point[0] - len(num))
            for dx in range(len(num)):
                p = (start + dx, point[1])
                d = calculate_distance(p, special_ind)
                if d <= math.sqrt(2):
                    nums.append(int(num))
                    break

            if len(nums) == 2:
                ans += nums[0] * nums[1]
                nums = []

    return ans

def main():
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))

if __name__ == "__main__":
    main()
