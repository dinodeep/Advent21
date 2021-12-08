

def parseinput():
    with open("hardinput.txt", "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "").split(" | ") for line in lines]
        lines = [(patterns.split(" "), digits.split(" ")) for patterns, digits in lines]

    return lines


def main():
    data = parseinput()
    count = 0
    for patterns, digits in data:
        for digit in digits:
            if len(digit) in [2, 3, 4, 7]:
                count += 1

    return count


result = main()
print(result)
