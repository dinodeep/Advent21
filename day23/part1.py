

def parseinput(file):

    with open(file, "r") as f:
        lines = f.readlines()

    lines = [l.replace("#", "").replace("\n", "").strip() for l in lines]

    return lines[1] + lines[2] + lines[3]


def getCheapestCost(start, goal):

    # create priority queue
    # create found set
    # create cost dictionary (maps states to cheapest cost)

    # while priority queue is not empty:

    # pop cost and state node off of queue

    # add it to found set

    # if goal -- return its cost

    # otherwise get all neighboring states with updated costs
    # for each neighboring state
    # if state not already found and new cost is cheaper than one that has already been found
    # add to priority queue

    pass


def makeMove(state, startIdx, endIdx, cost):
    amphipod = state[startIdx]

    if amphipod == "A":
        cost += 1
    if amphipod == "B":
        cost += 10
    if amphipod == "C":
        cost += 100
    if amphipod == "D":
        cost += 1000

    if startIdx < endIdx:
        newState = state[0:startIdx] + "." + state[startIdx+1:endIdx] + amphipod + state[endIdx+1]
    else:
        newState = state[0:endIdx] + amphipod + state[endIdx+1:startIdx] + "." + state[startIdx+1]

    return newState, cost


def getNeighbors(state, cost):
    neighbors = []

    # move amphidpods in the top row (0-10, consider moving downards for 2, 4, 6, 8)
    for i in range(11):
        if state[i] != ".":
            if 0 <= i - 1 and state[i - 1] == ".":
                # can move to the left
                neighbors.append(makeMove(state, i, i - 1, cost))
            if i + 1 <= 10 and state[i + 1] == ".":
                # can move to the right
                neighbors.append(makeMove(state, i, i + 1, cost))

            # index to move to (if possible)
            j = 10 + i // 2
            if (i == 2 or i == 4 or i == 6 or i == 8) and state[j] == ".":
                # can move down
                neighbors.append(makeMove(state, i, j, cost))

    # move amphipods in the side rooms (11-18, move up or down)
    for i in range(11, 19):
        if state[i] != ".":

            # make up moves (check if leaving room)
            if (i == 11 or i == 12 or i == 13 or i == 14):
                j = (i - 10) * 2
                if state[j] == ".":
                    # can leave side room
                    neighbors.append(makeMove(state, i, j, cost))
            else:
                if state[i - 4] == ".":
                    neighbors.append(makeMove(state, i, i - 4, cost))

            # make down moves
            if i + 4 <= 18 and state[i + 4] == ".":
                neighbors.append(makeMove(state, i, i + 4, cost))

    return neighbors


def main():

    # 0-10 = top row
    # 11-14 = first row of side rooms
    # 15-18 = second row of side rooms
    # Goal: ". . . . . . . . . . . A B C D A B C D"

    start = parseinput("easyinput.txt")

    goal = "...........ABCDABCD"

    cost = getCheapestCost(start, goal)
    return cost


result = main()
print(result)
