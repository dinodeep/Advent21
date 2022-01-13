

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
