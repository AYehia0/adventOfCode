with open("input.txt") as df:
    data = df.read().split("\n")[:-1]

    ans1 = 0
    ans2 = 0
    for lvl in data:

        p1, p2 = lvl.split(",")

        a1, a2 = list(map(int, p1.split("-")))
        b1, b2 = list(map(int, p2.split("-")))

        # math way
        if a1 <= b1 and b2 <= a2 or b1 <= a1 and a2 <= b2:
            ans1 += 1

        if not (a2 < b1 or a1 > b2):
            ans2 += 1
        # s1, s2 = set(range(a1, a2 + 1, 1)), set(range(b1, b2 + 1, 1))
        # if s1.issubset(s2) or s2.issubset(s1):
        #     ans1 += 1
        # if s1.intersection(s2):
        #     ans2 += 1

    print(f"Part 1 : {ans1}")
    print(f"Part 2 : {ans2}")
