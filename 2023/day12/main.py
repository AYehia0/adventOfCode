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


def part2(lines):
    pass


def main():
    print("Ans 1: ", part1(data))
    print("Ans 2: ", part2(data))


if __name__ == "__main__":
    main()
