# part 2 only
part2 = 0

with open('input.txt') as file_:
    for line in file_.readlines():
        signals, output = line.strip().split(" | ")
        d = {
            l: set(s) for s in signals.split() if (l := len(s)) in (2, 4)
        }

        n = ""
        for o in output.split():
            l = len(o)
            if l == 2: 
                n += "1"
            elif l == 4: 
                n += "4"
            elif l == 3:
                n += "7"
            elif l == 7:
                n += "8"

            elif l == 5:
                s = set(o)
                if len(s & d[2]) == 2:
                    n += "3"
                elif len(s & d[4]) == 2:
                    n += "2"
                else:
                    n += "5"

            else: # l == 6
                s = set(o)
                if len(s & d[2]) == 1:
                    n += "6"
                elif len(s & d[4]) == 4:
                    n += "9"
                else:
                    n += "0"
    
        part2 += int(n)
    
print(part2)
