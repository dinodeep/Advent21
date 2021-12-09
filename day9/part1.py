

def parseinput(file):

    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "") for line in lines]

    floorMap = [list(line) for line in lines]
    floorMap = [[int(num) for num in line] for line in lines]
    return floorMap


def isLowPoint(floorMap, i, j):

    n = len(floorMap)
    m = len(floorMap[0])
    pointHeight = floorMap[i][j]

    # check that all possible surrounding points are less than current one
    if i - 1 >= 0 and floorMap[i - 1][j] <= pointHeight:
        return False
    if i + 1 < n and floorMap[i + 1][j] <= pointHeight:
        return False
    if j - 1 >= 0 and floorMap[i][j - 1] <= pointHeight:
        return False
    if j + 1 < m and floorMap[i][j + 1] <= pointHeight:
        return False

    return True


def main():
    floorMap = parseinput("hardinput.txt")

    riskSum = 0
    for i in range(len(floorMap)):
        for j in range(len(floorMap[0])):
            if isLowPoint(floorMap, i, j):
                riskSum += floorMap[i][j] + 1

    return riskSum


result = main()
print(result)
