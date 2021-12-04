# reading from a file
with open('input.txt', 'r') as file_:
    records = file_.read().splitlines()

    bits = [[record[i] for record in records] for i in range(len(records[0]))]
    
    most_bit = ""
    least_bit = ""

    for bit in bits:
        most_bit += max(bit, key=bit.count)

    # inverting the bits
    
    least_bit = "".join('1' if x == '0' else '0' for x in most_bit)

    print(int(most_bit, 2)*int(least_bit, 2))
