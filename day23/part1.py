import heapq


def parseinput(file):

    with open(file, "r") as f:
        lines = f.readlines()

    lines = [l.replace("#", "").replace("\n", "").strip() for l in lines]

    return lines[1] + lines[2] + lines[3]


def getHeuristic(state):
    hCost = 0

    # iterate through each position
    for i, c in enumerate(state):
        if c != ".":
            # calculate distance from i to target location
            if c == "A":
                targets = [2, 11, 15]
                mult = 1
            elif c == "B":
                targets = [4, 12, 16]
                mult = 10
            elif c == "C":
                targets = [6, 13, 17]
                mult = 100
            else: # c == "D"
                targets = [8, 14, 18]
                mult = 1000

            # horizontal distance
            if i in targets:
                horizontal = 0
                up = 0
            else:
                if i > 10:
                    # if in different side room -- get position when exiting side room
                    horizontal = abs(((i - 10) * 2) - targets[0])
                    up = 1 if i < 15 else 2
                else:
                    horizontal = abs(i - targets[0])
                    up = 0

            hCost += mult * (horizontal + up)

    if 11 - state[:11].count(".") > 4:
        hCost += 10000

    return hCost


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
        newState = state[0:startIdx] + "." + state[startIdx+1:endIdx] + amphipod + state[endIdx+1:]
    else:
        newState = state[0:endIdx] + amphipod + state[endIdx+1:startIdx] + "." + state[startIdx+1:]

    heurCost = getHeuristic(newState)
    return newState, cost, heurCost


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


def getCheapestCost(start, goal):

    # create priority queue
    # create visisted dictionary
    # create cost dictionary (maps states to cheapest cost)
    visited = set()
    bestcosts = {start: 0}

    heap = []
    heapq.heappush(heap, (getHeuristic(start), 0, start))

    iter = 0

    # while priority queue is not empty:
    while True:
        if heap.count == 0:
            return None

        # pop cost and state node off of queue and say that it has been visited
        cost, trueCost, state = heapq.heappop(heap)
        visited.add(state)

        if iter % 10000 == 0:
            print(state[:11], state[11:15], state[15:], trueCost)
        if iter % 1000000 == 0:
            input()

        # if goal -- return its cost
        if state == goal:
            return trueCost

        # iterate through all neighboring states with updated costs
        neighbors = getNeighbors(state, trueCost)
        for newState, newCost, heurCost in neighbors:
            if newState not in visited:
                # if newState not already found and new cost is cheaper than one that has already been found, add to heap
                if newState not in bestcosts or newCost < bestcosts[newState]:
                    bestcosts[newState] = newCost
                    heapq.heappush(heap, (newCost + heurCost, newCost, newState))

        iter += 1


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
