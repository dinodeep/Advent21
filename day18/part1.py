
# going to have to create a binary tree to represent snail numbers
class Node:
    def __init__(self, parent, left, right, depth, value):
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth
        self.value = value # only set to a value when left and rigth are None


def displaySnailnum(snailnum: Node, top=True):
    if snailnum.left == None and snailnum.right == None:
        print(snailnum.value, end="")
    else:
        print("[", end="")
        displaySnailnum(snailnum.left, top=False)
        print(",", end="")
        displaySnailnum(snailnum.right, top=False)
        print("]", end="")

    # for end line
    if top:
        print()


def incrDepth(snailnum: Node):
    if snailnum != None:
        snailnum.depth += 1
        incrDepth(snailnum.left)
        incrDepth(snailnum.right)


def line2snailnum(line, parent=None, depth=0):

    if line[0].isdigit():
        # parse single number -- base case
        return Node(parent, None, None, depth, int(line[0])), 1

    node = Node(parent, None, None, depth, None)
    if line[0] == "[":
        # parse pair -- recursive case
        # use # of characters used to track start and ends of left and rigth children
        leftChild, leftUsed = line2snailnum(line[1:], parent=node, depth=depth + 1)
        rightChild, rightUsed = line2snailnum(line[leftUsed + 2:], parent=node, depth=depth + 1)

        node.left = leftChild
        node.right = rightChild

        # add 3 for the [,] characters
        return node, leftUsed + rightUsed + 3


def parseinput(file):

    with open(file, "r") as f:
        lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]

    snailnums = []
    # for each line construct the snail number
    for line in lines:
        snailnum, _ = line2snailnum(line, None, 0)
        snailnums.append(snailnum)

    # first line is start num, rest are the nums to add
    return snailnums[0], snailnums[1:]


def getExplodingPair(sn: Node):
    # base cases -- if end node or regular number
    if sn == None or (sn.left == None and sn.right == None):
        return None

    # get the exploding pairs of the left and right children
    leftPair = getExplodingPair(sn.left)
    rightPair = getExplodingPair(sn.right)

    # return the leftmost pair
    if leftPair != None:
        return leftPair
    elif sn.left != None and sn.right != None and sn.depth == 4:
        return sn
    else:
        return rightPair


def getSplittingNum(sn: Node):
    # base cases
    if sn == None:
        return None

    # get splitting nums for the left and right
    leftNum = getSplittingNum(sn.left)
    rightNum = getSplittingNum(sn.right)

    # return the leftmost
    if leftNum != None:
        return leftNum
    elif (sn.left == None and sn.right == None and sn.value >= 10):
        return sn
    else:
        return rightNum


def shiftvalue(node: Node, value, toLeft):
    # try to find an upper parent s.t. it has a left/right path
    while node != None:
        parent = node.parent
        if toLeft and parent != None and parent.right == node:
            break
        elif not toLeft and parent != None and parent.left == node:
            break
        node = parent

    # check if could not find such parent
    if node == None:
        return

    # go down left child's rightmost path to reach a regular number
    # or down right child's leftmost path
    if toLeft:
        node = parent.left
    else:
        node = parent.right
    while not (node.left == None and node.right == None and node.value != None):
        if toLeft:
            node = node.right
        else:
            node = node.left

    # increment the node value
    node.value += value

    return


def explode(node: Node):
    if node == None or node.left == None or node.right == None:
        print("Error -- passed illegal node to explode")

    # sift left value to left
    shiftvalue(node, node.left.value, True)

    # sift right value to rigth
    shiftvalue(node, node.right.value, False)

    # replace current node with 0 value
    node.left = None
    node.right = None
    node.value = 0

    return


def split(node: Node):
    if node == None or node.left != None or node.right != None or node.value < 10:
        print("Error -- passed illegal node to split")

    lval = node.value // 2
    rval = lval + node.value % 2
    newdepth = node.depth + 1

    # create the splitting nodes
    leftNode = Node(node, None, None, newdepth, lval)
    rightNode = Node(node, None, None, newdepth, rval)

    # update the parent node
    node.value = None
    node.left = leftNode
    node.right = rightNode


def addSnailnums(sn1: Node, sn2: Node):
    # increase depths of children
    incrDepth(sn1)
    incrDepth(sn2)

    # construct new parent node and connect together
    parent = Node(None, sn1, sn2, 0, None)
    sn1.parent = parent
    sn2.parent = parent

    explodePair = getExplodingPair(parent)
    splitNum = getSplittingNum(parent)

    # while is reducible
    while explodePair != None or splitNum != None:

        # explode first
        if explodePair != None:
            explode(explodePair)
        # then split
        elif splitNum != None:
            split(splitNum)

        # check for further reductions
        explodePair = getExplodingPair(parent)
        splitNum = getSplittingNum(parent)

    return parent


def getMagnitude(sn):
    if sn == None:
        print("Error -- magnitude algorithm should not reach None Node -- misshaped number representation")

    # base case -- regular number
    if sn.left == None and sn.right == None and sn.value != None:
        return sn.value

    # recursive case -- pair number
    return 3 * getMagnitude(sn.left) + 2 * getMagnitude(sn.right)


def main():

    startnum, addnums = parseinput("hardinput.txt")

    accNum = startnum
    for num in addnums:
        accNum = addSnailnums(accNum, num)

    return getMagnitude(accNum)


result = main()
print(result)
