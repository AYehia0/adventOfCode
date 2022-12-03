import string


def calculate_posval(char):
    return string.ascii_letters.index(char) + 1


with open("input.txt") as df:
    data = df.read().split("\n")
    ans1 = 0
    ans2 = 0
    group_rucks = [data[:-1][k:k + 3] for k in range(0, len(data) - 1, 3)]

    # part 1
    for ruck in data[:-1]:
        # get into 2 halvs
        com1, com2 = ruck[:len(ruck)//2], ruck[len(ruck)//2:]
        a = set(com1) & set(com2)
        ans1 += calculate_posval(a.pop())

    # part 2
    for g_ruck in group_rucks:
        com1, com2, com3 = g_ruck
        b = set(com1) & set(com2) & set(com3)
        ans2 += calculate_posval(b.pop())

    print(f"Part 1 : {ans1}")
    print(f"Part 2 : {ans2}")
