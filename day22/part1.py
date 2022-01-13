import numpy as np
from numpy.lib.arraysetops import isin


def parseinput(file):
    with open(file, "r") as f:
        lines = f.readlines()

    lines = [l.replace("\n", "") for l in lines]

    actions = [l.split(" ") for l in lines]
    actions = [(1, region) if v == "on" else (0, region) for v, region in actions]

    rebootSteps = []

    def intIncr(s):
        return int(s) + 50

    for v, region in actions:
        dims = [list(map(intIncr, dim[2:].split(".."))) for dim in region.split(",")]
        rebootSteps.append((v, dims))

    return rebootSteps


def isInRange(region):
    xlo, xhi = region[0]
    ylo, yhi = region[1]
    zlo, zhi = region[2]

    dims = [xlo, xhi, ylo, yhi, zlo, zhi]
    inRange = [0 <= d < 102 for d in dims]

    return all(inRange)


def reboot(grid, steps):

    # for each step -- update the grid if in range
    for value, region in steps:
        if isInRange(region):
            xlo, xhi = region[0]
            ylo, yhi = region[1]
            zlo, zhi = region[2]

            grid[xlo:xhi+1, ylo:yhi+1, zlo:zhi+1] = value

    return grid


def main():
    rebootSteps = parseinput("hardinput.txt")

    # initialize grid and perform rebootSteps
    grid = np.zeros((102, 102, 102), dtype=np.int8)
    grid = reboot(grid, rebootSteps)

    return np.count_nonzero(grid)


result = main()
print(result)
