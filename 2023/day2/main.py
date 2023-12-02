import re
from collections import defaultdict
from functools import reduce
import operator

with open("input.txt") as df:
    data = df.readlines()

def part1(lines):
    # red, green, blue
    configs = [12, 13, 14]

    ans = 0
    
    for line in lines:
        parts = line.split(":")
        
        game_id = int(parts[0].replace("Game ", ""))
        
        # Create a dictionary for sets
        sets = defaultdict(int)
        
        inner_loop_broken = False

        # Iterate over parts to count occurrences of colors
        for part in parts[1].split(";"):
            set_tmp = part.strip().split(",")
            for s in set_tmp:
                c, color = s.strip().split(" ")
                sets[color.strip()] = int(c)
                
                # Check if the counts are greater than or equal to the configurations
                if sets["red"] > configs[0] or sets["green"] > configs[1] or sets["blue"] > configs[2]:
                    inner_loop_broken = True
                    break
            
                sets = defaultdict(int)
            if inner_loop_broken:
                break
        # If the loop completes without breaking, add the game_id
        else:
            ans += game_id


def part2(lines):
    ans = 0
    max_counts = defaultdict(int)
    for line in lines:
        parts = line.split(":")
        
        for part in parts[1].split(";"):
            set_tmp = part.strip().split(",")
            for s in set_tmp:
                c, color = s.strip().split(" ")
                max_counts[color.strip()] = max(max_counts[color.strip()], int(c))
                
            # find the max of each color
        ans += reduce(operator.mul, max_counts.values(), 1)
        max_counts = defaultdict(int)
    print(ans)

def main():
    # part1(data)
    part2(data)

if __name__ == "__main__":
    main()
