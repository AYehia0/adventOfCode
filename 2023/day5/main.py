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

def part2(lines):
    ans = 0

    return ans

def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))

if __name__ == "__main__":
    main()
    """

    seed_to_soid = parse_section(data[1])
    soil_to_fert = parse_section(data[2])
    fert_to_water = parse_section(data[3])
    water_to_light = parse_section(data[4])
    light_to_temp = parse_section(data[5])
    temp_to_hum = parse_section(data[6])
    hum_to_location = parse_section(data[7])


    """
