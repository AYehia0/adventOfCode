import math

with open("input.txt") as df:
    data = df.read().split("\n\n")

def parse_section(section):
    """parses the paragraph and returns needed data as dict"""
    lines = section.strip().split("\n")[1:]
    mm = []
    for line in lines:
        nums = [int(i) for i in line.split(" ") if i != ""]
        dest_range_start = nums[0]
        source_range_start = nums[1]
        range_len = nums[-1]
        mm.append([dest_range_start, source_range_start, range_len])
    return mm

def part1(data):
    seeds = [int(i) for i in data[0].split(": ")[-1].split(" ") if i != ""]
    ans = math.inf
    # calculate the location for each seen and append to the ans then find the min of ans
    for seed in seeds:
        tmp = seed
        for level in data[1:]:
            for [dest, src, length] in parse_section(level):
                if (src <= tmp and tmp <= src + length - 1):
                    diff = tmp - src
                    tmp = dest + diff
                    break
        ans = min(ans, tmp)

    return ans

def part2(data):
    inputs = [int(i) for i in data[0].split(": ")[-1].split(" ") if i != ""]
    seed_ranges = []
    for i in range(0, len(inputs), 2):
        seed_ranges.append([inputs[i], inputs[i] + inputs[i+1]])

    for level in data[1:]:
        ranges = []
        for parsed in parse_section(level):
            ranges.append(parsed)

        new = []
        while seed_ranges:
            start, end = seed_ranges.pop()
            for dest, src, length in ranges:

                # dest: start of range, src + length: end of range
                # check for overlaps
                # finding the start of the overlap : the rightmost of the overlap max(starts), end will be the min(ends)
                overlap_start = max(start, src)
                overlap_end = min(end, src + length)
                if overlap_start < overlap_end:
                    new.append([overlap_start - src + dest, overlap_end - src + dest])
                    if overlap_start > start:
                        seed_ranges.append([start, overlap_start])
                    if end > overlap_end:
                        seed_ranges.append([overlap_end, end])
                    break
            else:
                new.append([start, end])

        seed_ranges = new

    return min(seed_ranges)[0]

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
