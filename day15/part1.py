import heapq


def getNeighbors(i, j, n, m):
    neighbors = []

    if 0 <= i - 1:
        neighbors.append((i - 1, j))
    if 0 <= j - 1:
        neighbors.append((i, j - 1))
    if i + 1 < n:
        neighbors.append((i + 1, j))
    if j + 1 < m:
        neighbors.append((i, j + 1))

    return neighbors


def parseinput(file):

    with open(file, "r") as f:
        lines = f.readlines()

    # parse numbers into grid of numbers
    lines = [line.replace("\n", "") for line in lines]
    grid = [list(map(int, list(line))) for line in lines]

    # construct costs dictionary
    n = len(grid)
    m = len(grid[0])
    costs = {}

    for i in range(n):
        for j in range(m):
            costs[(i, j)] = grid[i][j]

    # construct graph as adjacency list
    adjlist = {}
    for i in range(n):
        for j in range(m):
            adjlist[(i, j)] = getNeighbors(i, j, n, m)

    return adjlist, costs, n, m


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# can improve by doing A* search with Manhattan cost heuristic


def cheapestPathCost(adjlist, costs, start, end):
    visited = {p: False for p in adjlist.keys()}

    startNode = (manhattan(start, end), start)
    heap = []
    heapq.heappush(heap, startNode)

    while True:
        if len(heap) == 0:
            return None

        # pop current best solution
        currcost, currpoint = heapq.heappop(heap)
        visited[currpoint] = True

        # if goal then return
        if currpoint == end:
            return currcost

        # otherwise get all children, create new nodes and add to queue
        for neighbor in adjlist[currpoint]:
            if not visited[neighbor]:
                newcost = currcost - manhattan(currpoint, end) + manhattan(neighbor, end) + costs[neighbor]
                newNode = (newcost, neighbor)
                heapq.heappush(heap, newNode)


def main():
    adjlist, costs, n, m = parseinput("hardinput.txt")

    # perform A* search to find the cost of the cheapest path
    return cheapestPathCost(adjlist, costs, (0, 0), (n - 1, m - 1))


result = main()
print(result)
