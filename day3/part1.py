
def toDec(binary):
    result = 0
    posVal = 1
    for digit in binary[::-1]:
        result += digit * posVal
        posVal *= 2
    return result


with open("input1.txt", "r") as f:
    # get line and parse them
    lines = f.readlines()
    for i in range(len(lines) - 1):
        lines[i] = lines[i][:-1]

binaryGamma = []
binaryEpsilon = []
for j in range(len(lines[0])):
    count0 = 0
    count1 = 0
    for i in range(len(lines)):
        if lines[i][j] == "0":
            count0 += 1
        else:
            count1 += 1
    binaryGamma.append(0 if count0 > count1 else 1)
    binaryEpsilon.append(1 if count0 > count1 else 0)

print(toDec(binaryGamma) * toDec(binaryEpsilon))
