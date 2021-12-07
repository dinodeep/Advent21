
def toDec(binary):
    result = 0
    posVal = 1
    for digit in binary[::-1]:
        result += int(digit) * posVal
        posVal *= 2
    return result


def filter(numbers, col, useMax):
    count0 = 0
    count1 = 0
    for i in range(len(numbers)):
        if numbers[i][col] == "0":
            count0 += 1
        else:
            count1 += 1
    if useMax:
        chosenOne = 1 if count1 >= count0 else 0
    else:
        chosenOne = 0 if count0 <= count1 else 1
    return [num for num in numbers if int(num[col]) == chosenOne]


with open("input2.txt", "r") as f:
    # get line and parse them
    lines = f.readlines()
    for i in range(len(lines) - 1):
        lines[i] = lines[i][:-1]

# get oxygen number
oxynumbers = lines
for col in range(len(lines[0])):
    oxynumbers = filter(oxynumbers, col, True)
    if len(oxynumbers) == 1:
        break

# get co2 number
coonumbers = lines
for col in range(len(lines[0])):
    coonumbers = filter(coonumbers, col, False)
    if len(coonumbers) == 1:
        break

# return multiple of the two
print(toDec(oxynumbers[0]) * toDec(coonumbers[0]))
