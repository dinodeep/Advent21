

def parseinput(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "") for line in lines]
    return lines


def finderror(line):
    stack = []

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
            return c

    return None


def errorCharToVal(c):
    valMap = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return valMap[c]


def main():
    lines = parseinput("hardinput.txt")

    errors = []
    for line in lines:
        errorChar = finderror(line)
        if errorChar is not None:
            value = errorCharToVal(finderror(line))
            errors.append(value)

    return sum(errors)


result = main()
print(result)
