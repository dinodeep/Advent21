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
        rules[pair] = [0, c]

    for i in range(len(polymer) - 1):
        pair = polymer[i] + polymer[i + 1]
        rules[pair][0] += 1

    charCounts = Counter(polymer)

    return charCounts, rules


def polymerstep(charCounts, rules):

    newrules = {key: [0, value[1]] for key, value in rules.items()}

    for pair, info in rules.items():
        numpair, c = info

        newrules[pair[0] + c][0] += numpair
        newrules[c + pair[1]][0] += numpair

        charCounts[c] += numpair

    return charCounts, newrules


def main():
    charCounts, rules = parseinput("hardinput.txt")

    for i in range(40):
        charCounts, rules = polymerstep(charCounts, rules)

    counts = list(charCounts.values())
    return max(counts) - min(counts)


result = main()
print(result)
