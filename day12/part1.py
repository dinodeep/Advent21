from collections import Counter


def parseinput(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "").split("-") for line in lines]

        # construct adjacency list
        adjList = {}
        for startNode, endNode in lines:
            if startNode not in adjList:
                adjList[startNode] = [endNode]
            else:
                adjList[startNode].append(endNode)
            if endNode not in adjList:
                adjList[endNode] = [startNode]
            else:
                adjList[endNode].append(startNode)

    return adjList


def isFeasible(currPath, neighbor):
    newpath = currPath + [neighbor]
    lowercaseNodes = [node for node in newpath if not node.isupper()]
    counts = list(Counter(lowercaseNodes).values())
    return all([count <= 1 for count in counts])


def findAllPaths(adjList):
    paths = []
    stack = [["start"]]

    while len(stack) != 0:
        path = stack[-1]
        stack = stack[:-1]

        if path[-1] == "end":
            # if a goal path, add it to all paths
            paths.append(path)
        else:
            # otherwise, try to extend path
            neighbors = adjList[path[-1]]
            for neighbor in neighbors:
                if isFeasible(path, neighbor):
                    newpath = path + [neighbor]
                    stack.append(newpath)

    return paths


def main():
    adjList = parseinput("hardinput.txt")

    paths = findAllPaths(adjList)

    return len(paths)


result = main()
print(result)
