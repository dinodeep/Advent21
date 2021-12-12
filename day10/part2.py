

def parseinput(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "") for line in lines]
    return lines


def finderror(line):
    stack = []

    # search for errors
    for c in line:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        elif stack[-1] == "(" and c == ")":
            stack = stack[:-1]
        elif stack[-1] == "[" and c == "]":
            stack = stack[:-1]
        elif stack[-1] == "{" and c == "}":
            stack = stack[:-1]
        elif stack[-1] == "<" and c == ">":
            stack = stack[:-1]
        else:
            return c, None

    # reverse the leftover unfinished characters to create completion
    reverseMap = {"(": ")", "[": "]", "{": "}", "<": ">"}
    completion = []
    for c in stack[::-1]:
        completion.append(reverseMap[c])

    return None, completion


def charToVal(c):
    valMap = {")": 1, "]": 2, "}": 3, ">": 4}
    return valMap[c]


def completionToPoints(completion):
    score = 0
    for c in completion:
        score *= 5
        score += charToVal(c)
    return score


def main():
    lines = parseinput("hardinput.txt")
    completionPoints = []

    for line in lines:
        errorChar, completion = finderror(line)
        if errorChar is None:
            points = completionToPoints(completion)
            completionPoints.append(points)

    completionPoints = sorted(completionPoints)
    return completionPoints[len(completionPoints) // 2]


result = main()
print(result)
