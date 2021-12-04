# reading from a file

def part1():
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

def part2():
    with open('input.txt', 'r') as file_:
        records = file_.read().splitlines()
        #records = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

        # oxygen generator rating
        def gen(func, records, inp): 
            for i in range(len(records[0])):
    
                bits = [record[i] for record in records] 
    
                cut_off = func(bits, key=bits.count)
    
                if len(bits) != 2:
                # cutting from the records
                    records = [record for record in records if record[i] == str(cut_off)]
                else:
                    records = [record for record in records if record[i] == inp]
    
            return records[0]

        ox = gen(max, records, '1')
        co = gen(min, records, '0')
        print(int(ox, 2)*int(co, 2))

part2()
