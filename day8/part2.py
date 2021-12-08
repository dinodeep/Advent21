

def parseinput():
    with open("hardinput.txt", "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "").split(" | ") for line in lines]
        lines = [(patterns.split(" "), digits.split(" ")) for patterns, digits in lines]

    return lines


def decodeDigits(patterns, digits):
    counts = {size: [] for size in [2, 3, 4, 5, 6, 7]}
    for pattern in patterns:
        counts[len(pattern)].append(pattern)

    oneSigs = counts[2][0]
    fourSigs = counts[4][0]

    value = ""
    for digit in digits:
        if len(digit) == 2:
            value += "1"
        elif len(digit) == 3:
            value += "7"
        elif len(digit) == 4:
            value += "4"
        elif len(digit) == 5:
            if oneSigs[0] in digit and oneSigs[1] in digit:
                value += "3"
            elif len([1 for c in fourSigs if c in digit]) >= 3:
                value += "5"
            else:
                value += "2"
        elif len(digit) == 6:
            if not (oneSigs[0] in digit and oneSigs[1] in digit):
                value += "6"
            elif len([1 for c in fourSigs if c in digit]) == 4:
                value += "9"
            else:
                value += "0"
        elif len(digit) == 7:
            value += "8"

    return int(value)


def main():
    data = parseinput()
    result = 0
    for patterns, digits in data:
        value = decodeDigits(patterns, digits)
        result += value
    return result


result = main()
print(result)
