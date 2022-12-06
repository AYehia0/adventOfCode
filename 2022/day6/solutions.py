def detect_packets(data, seq_num):
    for st in range(0, len(data), 1):
        if len(set(data[st:st+seq_num])) == seq_num:
            return st + seq_num


# the start of a packet : sequence of four characters that are all different.
with open("input.txt") as df:
    data = df.read().strip()

    ans1 = detect_packets(data, 4)
    ans2 = detect_packets(data, 14)

    print(f"Part 1 : {ans1}")
    print(f"Part 2 : {ans2}")
