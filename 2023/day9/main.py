with open("input.txt") as df:
    data = df.readlines()

def part1(lines):
    ans = 0
    for line in lines:
        nums = list(map(int, line.strip().split(" ")))

        t = nums[-1]
        while any(val != 0 for val in nums[:-1]):  # Continue until all values are zeros
            tmp = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            nums = tmp[:]  # Update nums with the new values
            t += nums[-1]
        ans += t

    return ans

def part2(lines):
    ans = 0
    for line in lines:
        nums = list(map(int, line.strip().split(" ")))

        t = nums[0]
        even_odd = 0
        while any(val != 0 for val in nums[:-1]):  # Continue until all values are zeros
            tmp = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            nums = tmp[:]  # Update nums with the new values
            even_odd += 1
            if even_odd % 2 == 0:
                t += nums[0]
            else:
                t += -nums[0]
        ans += t

    return ans

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
