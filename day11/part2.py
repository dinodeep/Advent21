

def parseinput(file):

    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "") for line in lines]
        octogrid = [[int(c) for c in line] for line in lines]

    return octogrid


def printgrid(grid):
    for row in grid:
        print(row)


def getSurroundingPoints(x, y, n, m):
    points = []

    prevX = 0 <= x - 1
    nextX = x + 1 < n
    prevY = 0 <= y - 1
    nextY = y + 1 < n

    if prevX:
        points.append((x - 1, y))
    if nextX:
        points.append((x + 1, y))
    if prevY:
        points.append((x, y - 1))
    if nextY:
        points.append((x, y + 1))
    if prevX and prevY:
        points.append((x - 1, y - 1))
    if prevX and nextY:
        points.append((x - 1, y + 1))
    if nextX and prevY:
        points.append((x + 1, y - 1))
    if nextX and nextY:
        points.append((x + 1, y + 1))

    return points


def updategrid(octogrid):

    n = len(octogrid)
    m = len(octogrid[1])
    flashingOctos = []

    # increase each octopus energy level by 1
    for i in range(n):
        for j in range(m):
            octogrid[i][j] += 1
            if octogrid[i][j] >= 10:
                flashingOctos.append((i, j))

    # increase surrounding octos until no more newly flashing
    while len(flashingOctos) > 0:
        x, y = flashingOctos[0]
        flashingOctos = flashingOctos[1:]
        points = getSurroundingPoints(x, y, n, m)
        for i, j in points:
            octogrid[i][j] += 1
            if octogrid[i][j] == 10:
                flashingOctos.append((i, j))

    # set all flashed octos to 0
    allFlashed = True
    for i in range(n):
        for j in range(m):
            if octogrid[i][j] >= 10:
                octogrid[i][j] = 0
            else:
                allFlashed = False

    return octogrid, allFlashed


def main():
    octogrid = parseinput("hardinput.txt")
    step = 0
    allFlashed = False

    while not allFlashed:
        octogrid, allFlashed = updategrid(octogrid)
        step += 1

    return step


result = main()
print(result)
