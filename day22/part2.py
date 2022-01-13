

def parseinput(file):
    with open(file, "r") as f:
        lines = f.readlines()

    lines = [l.replace("\n", "") for l in lines]

    actions = [l.split(" ") for l in lines]
    actions = [(1, region) if v == "on" else (0, region) for v, region in actions]

    rebootSteps = []

    for v, region in actions:
        dims = [list(map(int, dim[2:].split(".."))) for dim in region.split(",")]
        rebootSteps.append([v] + dims[0] + dims[1] + dims[2])

    return rebootSteps


def getIntersection(region1, region2):

    value = -region2[0]
    xlo, xhi = max(region1[1], region2[1]), min(region1[2], region2[2])
    ylo, yhi = max(region1[3], region2[3]), min(region1[4], region2[4])
    zlo, zhi = max(region1[5], region2[5]), min(region1[6], region2[6])

    if xhi < xlo or yhi < ylo or zhi < zlo:
        return None
    else:
        return [value, xlo, xhi, ylo, yhi, zlo, zhi]


def getCuboids(rebootSteps):

    cuboids = []
    idx = 0
    for rebootCuboid in rebootSteps:
        newCuboids = []
        for cuboid in cuboids:

            # get intersection and add its negative value
            intersection = getIntersection(rebootCuboid, cuboid)
            if intersection:
                newCuboids.append(intersection)

        # if on, add the region to cuboids
        if rebootCuboid[0] == 1:
            cuboids.append(rebootCuboid)

        cuboids += newCuboids

        idx += 1

    return cuboids


def getOnVolume(cuboids):
    volume = 0
    for cuboid in cuboids:
        volume += cuboid[0] * (cuboid[2] - cuboid[1] + 1) * (cuboid[4] - cuboid[3] + 1) * (cuboid[6] - cuboid[5] + 1)
    return volume


def main():
    rebootSteps = parseinput("hardinput.txt")

    cuboids = getCuboids(rebootSteps)

    volume = getOnVolume(cuboids)

    return volume


result = main()
print(result)
