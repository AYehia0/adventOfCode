with open("input.txt") as df:
    data = [l.rstrip("\n") for l in df.read().splitlines()]

def split_into_problems(matrix):
    width = max(len(row) for row in matrix)
    mat = [row.ljust(width) for row in matrix]

    problems = []
    cur = []

    for col in range(width):
        column = [mat[row][col] for row in range(len(mat))]

        if all(c == ' ' for c in column):
            if cur:
                problems.append(cur)
                cur = []
        else:
            cur.append(column)

    if cur:
        problems.append(cur)

    return problems


def parse_problem(columns):
    rows = ["".join(col[i] for col in columns) for i in range(len(columns[0]))]

    op = rows[-1].strip()

    nums = [int(r.strip()) for r in rows[:-1] if r.strip()]

    return nums, op


def evaluate(nums, op):
    res = nums[0]
    for x in nums[1:]:
        if op == '*':
            res *= x
        else:
            res += x
    return res


def part1(data):
    problems = split_into_problems(data)
    total = 0

    for p in problems:
        nums, op = parse_problem(p)
        total += evaluate(nums, op)

    return total


def part2(data):
    pass


def main():
    print("Ans 1:", part1(data))
    print("Ans 2:", part2(data))

if __name__ == "__main__":
    main()
