from collections import Counter


def parseinput(file):

    with open(file, "r") as f:
        lines = f.readlines()

    lines = [l.replace("\n", "") for l in lines]

    polymer = lines[0]

    ruleLines = lines[2:]
    rules = {}
    for line in ruleLines:
        pair, c = line.split(" -> ")
        rules[pair] = c

    return polymer, rules


def polymerstep(polymer, rules):
    newpolymer = polymer[0]

    for i in range(len(polymer) - 1):
        pair = polymer[i] + polymer[i + 1]
        c = rules[pair]
        newpolymer += c + polymer[i + 1]

    return newpolymer


def main():
    polymer, rules = parseinput("hardinput.txt")

    for i in range(10):
        polymer = polymerstep(polymer, rules)

    counts = list(Counter(polymer).values())
    return max(counts) - min(counts)


result = main()
print(result)
