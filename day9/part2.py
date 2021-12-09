

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


def getBasinSize(floorMap, i, j):
    # make a deep copy of the floorMap
    floorMap = [[num for num in row] for row in floorMap]
    n = len(floorMap)
    m = len(floorMap[0])

    # initialize info with first point found
    size = 0
    queue = [(i, j)]
    floorMap[i][j] = 9

    while len(queue) != 0:
        # pop off a point
        x, y = queue[0]
        queue = queue[1:]
        size += 1

        # remove point from map
        floorMap[x][y] = 9

        # create list of possible points extending basin
        newpoints = []
        if x - 1 >= 0 and floorMap[x - 1][y] < 9:
            floorMap[x - 1][y] = 9
            newpoints.append((x - 1, y))
        if x + 1 < n and floorMap[x + 1][y] < 9:
            floorMap[x + 1][y] = 9
            newpoints.append((x + 1, y))
        if y - 1 >= 0 and floorMap[x][y - 1] < 9:
            floorMap[x][y - 1] = 9
            newpoints.append((x, y - 1))
        if y + 1 < m and floorMap[x][y + 1] < 9:
            floorMap[x][y + 1] = 9
            newpoints.append((x, y + 1))

        # add points to the queue
        queue += newpoints

    return size


def main():
    floorMap = parseinput("hardinput.txt")

    basinSizes = []
    for i in range(len(floorMap)):
        for j in range(len(floorMap[0])):
            if isLowPoint(floorMap, i, j):
                basinSizes.append(getBasinSize(floorMap, i, j))

    basinSizes = sorted(basinSizes, reverse=True)
    return basinSizes[0] * basinSizes[1] * basinSizes[2]


result = main()
print(result)
