from functools import cmp_to_key

DIV_PACKET = [[[2]], [[6]]]

with open("input.txt") as df:
    data = df.read().strip()
    data_p1 = data.split("\n\n")
    data_p2 = list(map(eval, data.split())) + DIV_PACKET
    
def parse(left, right):

    # The base case
    if type(left) == int: 
        if type(right) == int:
            return left - right
        else:
            return parse([left], right)
    elif type(right) == int:
        return parse(left, [right])

    for l, r in zip(left, right):
        diff = parse(l, r)
        if diff:
            return diff
    return len(left) - len(right)

def calc_indcies(data):

    indcies = []
    for ind, pairs in enumerate(data):
        l, r = map(eval, pairs.split())

        if parse(l, r) < 0:
            indcies.append(ind + 1)

    return sum(indcies)

def main():

    ans1 = calc_indcies(data_p1)
    sorted_lists = sorted(data_p2, key=cmp_to_key(parse))
    ans2 = (sorted_lists.index(DIV_PACKET[0]) + 1) * (sorted_lists.index(DIV_PACKET[1]) + 1)

    print(f"Part 1 : {ans1}")
    print(f"Part 2 : {ans2}")

if __name__ == "__main__":
    main()
