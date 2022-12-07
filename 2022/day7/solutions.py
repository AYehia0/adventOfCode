from os import path
from collections import defaultdict


# find all of the directories with a total size of at most 100000,
# then calculate the sum of their total sizes.
def parse_commands(commands):
    dirs = {}
    sizes = {}
    for command in commands:
        type, name, *dir = command.split()

        # parse a command
        if type == "$" and name == "cd":
            curr_path = dir[0]
            if curr_path == "/":
                curr_dir = curr_path
            else:
                curr_dir = path.normpath(path.join(curr_dir, curr_path))

            if curr_dir not in dirs:
                dirs[curr_dir] = []
                sizes[curr_dir] = 0
        # actual files and dirs
        elif type != "$":
            if type != "dir":
                # Number size
                sizes[curr_dir] += int(type)
            else:
                dirs[curr_dir].append(path.normpath(path.join(curr_dir, name)))

    return dirs, sizes


def calculate_sum(dir):
    size = sizes[dir]
    for curr_dir in dirs[dir]:
        if curr_dir in dirs:
            size += calculate_sum(curr_dir)

    return size


def solution_from_reddit():
    """
    All credits goes to ViliamPucik.
    https://www.reddit.com/r/adventofcode/comments/zesk40/comment/iz8gh76/
    """

    with open("input_ex.txt") as df:
        log = map(str.split, df.read().strip().split("\n"))

    paths, dirs = [], defaultdict(int)

    for line in log:
        cmd, name, *size = line
        if cmd == "$" and name == "cd":
            if size[0] == "..":
                paths.pop()
            else:
                paths.append(size[0])
        elif cmd != "$" and cmd != "dir":
            for i in range(len(paths)):
                dirs["/".join(paths[:i+1])] += int(cmd)

    print(sum(size for size in dirs.values() if size <= 100000))
    required = 30000000 - (70000000 - dirs["/"])

    print(min(size for size in dirs.values() if size >= required))


with open("input_ex.txt") as df:
    commands = df.read().strip().split("\n")
    dirs, sizes = parse_commands(commands)
    max_space = 70000000
    free_space = 30000000
    reserved_space = calculate_sum("/")
    ans1 = 0
    ans2 = reserved_space
    for s in dirs:
        tmp = calculate_sum(s)
        if tmp <= 100000:
            ans1 += tmp

    print(f"Part 1 : {min(calculate_sum(size)for size in sizes if calculate_sum(size) >= free_space - (max_space - reserved_space))}")
    print(f"Part 2 : {sum(calculate_sum(size)for size in sizes if calculate_sum(size) <= 100000)}")
