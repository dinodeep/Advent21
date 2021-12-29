import numpy as np
from numpy.core.function_base import add_newdoc


def printImg(img):
    for row in img:
        print(row)
    print()


def parseinput(file):

    with open(file, "r") as f:
        lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]

    # parse the algorithm and input image
    # translate to 1s and 0s for easy number conversions
    algoMap = ["1" if c == "#" else "0" for c in lines[0]]
    inputImg = [["1" if c == "#" else "0" for c in line] for line in lines[2:]]

    return algoMap, inputImg


def addLayers(inputImg, pad):
    inputArr = np.array(inputImg)
    inputArr = np.pad(inputArr, pad, constant_values="0")
    return inputArr.tolist()


def convertPixel(x, y, inputImg, algoMap):
    binStr = ""
    for i in range(-1, 2):
        for j in range(-1, 2):
            binStr += inputImg[x + i][y + j]
    idx = int(binStr, 2)
    return algoMap[idx]


def enhance(inputImg, algoMap):
    m, n = len(inputImg), len(inputImg[0])

    # iterate through and convert necessary pixels
    outputImg = []
    for x in range(1, m - 1):
        outputRow = []
        for y in range(1, n - 1):
            # each (x, y) pair will have a 3x3 grid surrounding it
            outputRow.append(convertPixel(x, y, inputImg, algoMap))
        outputImg.append(outputRow)

    return outputImg


def main():

    algoMap, inputImg = parseinput("hardinput.txt")

    # add five layers of "infiniteness" to be able to gain effect of the infinity on the signal
    inputImg = addLayers(inputImg, 101)

    # enhance the image twice
    img = inputImg
    for _ in range(50):
        img = enhance(img, algoMap)

    return len([1 for row in img for c in row if c == "1"])


result = main()
print(result)
