with open("input.txt") as df:
    data = df.read().strip().splitlines()


# trying all the combinations with replacements
def generate_configs(config):
    if config == "":
        return [""]

    return [
        x + y
        for x in ("#." if config[0] == "?" else config[0])
        for y in generate_configs(config[1:])
    ]


def part1(lines):
    ans = 0
    for line in lines:
        conf, nums = line.split()
        nums = list(map(int, nums.split(",")))
        g = generate_configs(conf)

        for c in g:
            if nums == [len(bl) for bl in c.split(".") if bl]:
                ans += 1

    return ans


cache = {}


def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    key = (cfg, nums)

    if key in cache:
        return cache[key]

    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if (
            nums[0] <= len(cfg)
            and "." not in cfg[: nums[0]]
            and (nums[0] == len(cfg) or cfg[nums[0]] != "#")
        ):
            result += count(cfg[nums[0] + 1 :], nums[1:])

    cache[key] = result
    return result


def part2(lines):
    ans = 0
    for line in lines:
        conf, nums = line.split()
        conf = "?".join([conf] * 5)

        nums = tuple(map(int, nums.split(",")))
        nums *= 5

        ans += count(conf, nums)
    return ans


def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))


if __name__ == "__main__":
    main()
