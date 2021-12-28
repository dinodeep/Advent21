
import re


def parseinput(file):
    with open(file, "r") as f:
        line = f.readline()

    numbers = re.findall(r'-?\d+', line)
    return list(map(int, numbers))


def isInRegion(x, y, xlo, xhi, ylo, yhi):
    return xlo <= x <= xhi and ylo <= y <= yhi


def hitsRegion(xvel, yvel, xlo, xhi, ylo, yhi):
    x, y = 0, 0

    while True:
        # update position
        x += xvel
        y += yvel

        # update velocities
        xvel = xvel - 1 if xvel > 0 else 0
        yvel -= 1

        # check if in box, if true, then return true
        if isInRegion(x, y, xlo, xhi, ylo, yhi):
            return True

        # check if infitely past box, if so then break
        if x > xhi or y < ylo:
            break

    # trajectory does not hit box
    return False


def findAllVelocities(xlo, xhi, ylo, yhi):

    fittingVelocities = set()

    # fix possible x and y velocities and check if they hit
    for yvel in range(-xhi, xhi + 1):
        for xvel in range(xhi + 1):
            if hitsRegion(xvel, yvel, xlo, xhi, ylo, yhi):
                fittingVelocities.add((xvel, yvel))

    return fittingVelocities


def main():
    xlo, xhi, ylo, yhi = parseinput("hardinput.txt")
    fittingVelocities = findAllVelocities(xlo, xhi, ylo, yhi)

    return len(fittingVelocities)


result = main()
print(result)
