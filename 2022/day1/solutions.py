# read the data sample
with open("input.txt") as df:
    cals = []
    elf_cals = df.read().split("\n")

    sum_elf = 0
    for elf in elf_cals:
        if elf == "":
            cals.append(sum_elf)
            sum_elf = 0
        else:
            sum_elf += int(elf)

    tops = sorted(cals, reverse=True)
    print(f"Part 1 solution :  {tops[0]}")
    print(f"Part 2 solution :  {sum(tops[:3])}")
