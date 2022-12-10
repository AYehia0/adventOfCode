with open("input.txt") as df:
    instructions = df.read().splitlines()


def decode_prog(instructions):
    strength = 0
    signals = [20, 60, 100, 140, 180, 220]
    sig_map = [1]
    for instruction in instructions:
        inst, *x = instruction.split(" ")

        # addx
        if len(x) == 1:
            sig_map += [sig_map[-1], sig_map[-1]]
            # don't append to the list, it will be appended the next cycle
            sig_map[-1] = int(x[0]) + sig_map[-1]
        else:
            sig_map += [sig_map[-1]]

    for i in signals:
        print(f"{i} x {sig_map[i - 1]} = { i * sig_map[i - 1]}")
        strength += i * sig_map[i - 1]

    return sig_map, strength


def draw_screen(signal_map):
    """Draw the CRT Pixels: top to down, left to right"""

    # each 40 x is a line
    for i in range(0, len(signal_map) - 1, 40):
        for j in range(40):
            print("#" if abs(signal_map[i + j] - j) <= 1 else ".", end="")
        print()


def main():
    signal_map, ans1 = decode_prog(instructions)
    draw_screen(signal_map)

    print(f"Part 1 : {ans1}")


if __name__ == "__main__":
    main()
