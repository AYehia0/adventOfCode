def part1():

    cost = {
            ")" : 3,
            "]" : 57,
            "}" : 1197,
            ">" : 25137
        }

    with open('input.txt') as file_:
        lines = [line.strip('\n') for line in file_.readlines()]

        # discard corrupted lines
        #incomplete_lines = discard_corrupted(lines)
        incomplete = set()
        for line in lines:
            stack = []
            for pren in line:
                if pren == "{" or pren == "[" or pren == "(" or pren == "<":
                    stack.append(pren)
                    continue
                if (pren == "}" and stack[-1] == "{") or (pren == "]" and stack[-1] == "[") or (pren == ")" and stack[-1] == "(") or (pren == ">" and stack[-1] == "<"):
                    stack.pop()
                else:
                    incomplete.add(line)


        costs = 0
        for incomp_line in incomplete:
            stack = []
            for pren in incomp_line:
                if pren == "{" or pren == "[" or pren == "(" or pren == "<":
                    stack.append(pren)
                    continue
                if (pren == "}" and stack[-1] == "{") or (pren == "]" and stack[-1] == "[") or (pren == ")" and stack[-1] == "(") or (pren == ">" and stack[-1] == "<"):
                    stack.pop()
                else:
                    costs += cost[pren]
                    break
        print(costs)

def part2():

    cost = {
            "(" : 1,
            "[" : 2,
            "{" : 3,
            "<" : 4 
        }

    with open('input.txt') as file_:
        lines = [line.strip('\n') for line in file_.readlines()]

        # discard corrupted lines
        #incomplete_lines = discard_corrupted(lines)
        incomplete = set()
        scores = []
        for line in lines:
            stack = []
            for pren in line:
                if pren == "{" or pren == "[" or pren == "(" or pren == "<":
                    stack.append(pren)
                    continue
                if (pren == "}" and stack[-1] == "{") or (pren == "]" and stack[-1] == "[") or (pren == ")" and stack[-1] == "(") or (pren == ">" and stack[-1] == "<"):
                    stack.pop()
                else:
                    incomplete.add(line)

            score = 0
            if line not in incomplete:
                for ch in stack[::-1]:
                    score = score * 5 + cost[ch]
                scores.append(score)
        
        print(sorted(scores)[len(scores)//2])
part2()
