def parse_stacks(inp):
    parsed_list = {}
    rows = inp.split("\n")[:-1]
    for row in rows[::-1]:
        for stack_num, crate in enumerate(row[1::4], 1):
            if crate != " ":
                if stack_num in parsed_list:
                    parsed_list[stack_num].append(crate)
                else:
                    parsed_list[stack_num] = [crate]
    return parsed_list


def parse_commands(inp):
    commands_list = []
    commands = inp.split("\n")
    # move num_stacks from x to y
    for command in commands:
        s = command.replace("move", "").replace("from", "").replace("to", "")
        commands_list.append(list(map(int, s.split())))

    return commands_list


with open("input.txt") as df:
    data = df.read().split("\n\n")
    stacks = data[0]
    moves = data[1].strip()

    # save the current stacks to list
    ans1 = ""
    ans2 = ""
    stack1 = parse_stacks(stacks)
    stack2 = parse_stacks(stacks)
    commands = parse_commands(moves)

    for command in commands:
        crates, from_x, to_y = command

        # part 2
        crates_remove = stack2[from_x][-1*crates:]
        stack2[to_y] += crates_remove
        del stack2[from_x][-1*crates:]

        # part 1
        for _ in range(crates):
            crates_remove = stack1[from_x].pop()
            stack1[to_y].append(crates_remove)

    for i, j in zip(stack1.values(), stack2.values()):
        ans1 += i[-1]
        ans2 += j[-1]
    print(f"Part 1 : {ans1}")
    print(f"Part 2 : {ans2}")
