with open("input_ex.txt") as df:
    data = df.read().split("\n\n")


def calc_monkey_score(monkeys):
    """
    A monkey that starts a round with no items could end up inspecting
    and throwing many items by the time its turn comes around
    """
    rounds = 10000
    items = [[] for _ in range(len(monkeys))]
    inspects = [0 for _ in range(len(monkeys))]
    # Adding all the items first to avoid re-sorting or whatever idk
    for ind, monkey in enumerate(monkeys):
        monkey = monkey.split("\n")
        items[ind] += list(map(int, monkey[1].split(":")[-1].split(",")))

    for round in range(rounds):
        for ind, monkey in enumerate(monkeys):
            monkey = monkey.split("\n")
            eq = monkey[2].split(":")[-1].split("=")[-1]
            test_div = int(monkey[3].split("by")[-1])
            if_true = int(monkey[4][-1])
            if_false = int(monkey[5][-1])

            for item in items[ind]:
                # the worry level
                old = item
                new = eval(eq) // 3
                monkey_throw = if_false if new % test_div else if_true
                items[monkey_throw].append(new)
                inspects[ind] += 1
            items[ind] = []

    inspects = sorted(inspects, reverse=True)
    return inspects[0] * inspects[1]


def main():
    ans1 = calc_monkey_score(data)
    print(f"Part 1 : {ans1}")


if __name__ == "__main__":
    main()
