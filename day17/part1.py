
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


def findHighestVelocities(xlo, xhi, ylo, yhi):

    bestVelocities = None

    # fix possible x and y velocities and check if they hit
    for yvel in range(xhi):
        for xvel in range(xhi):
            if hitsRegion(xvel, yvel, xlo, xhi, ylo, yhi):
                # keep track of highest y velocity
                bestVelocities = (xvel, yvel)

    # return the pair with the highesty velocity along with its x val
    return bestVelocities


def main():
    xlo, xhi, ylo, yhi = parseinput("hardinput.txt")
    xvel, yvel = findHighestVelocities(xlo, xhi, ylo, yhi)

    # max y-height is sum i from i=1 to i=yvel
    return ((yvel + 1) * yvel) // 2


result = main()
print(result)
