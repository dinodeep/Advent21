
def parseinput():
    with open("testcase.txt", "r") as f:
        lines = f.readlines()

        data = []
        for line in lines:
            p1, p2 = line.split(" -> ")
            x1, y1 = p1.split(",")
            x2, y2 = p2.split(",")

            data.append([(int(x1), int(y1)), (int(x2), int(y2))])

    return data


def createboard(lines):
    xcoords = []
    ycoords = []
    for p1, p2 in lines:
        xcoords += [p1[0], p2[0]]
        ycoords += [p1[1], p2[1]]
    maxX = max(xcoords) + 1
    maxY = max(ycoords) + 1

    board = []
    for i in range(maxX):
        board.append([0] * maxY)
    return board


def updateboard(board, line):
    p1, p2 = line

    if p1[0] == p2[0]:
        # horizontal
        s = min(p1[1], p2[1])
        e = max(p1[1], p2[1])
        for i in range(s, e+1):
            board[p1[0]][i] += 1
    elif p1[1] == p2[1]:
        # vertical
        s = min(p1[0], p2[0])
        e = max(p1[0], p2[0])
        for i in range(s, e+1):
            board[i][p1[1]] += 1
    elif p1[0] - p1[1] == p2[0] - p2[1]:
        # top left to bottom right diagonal
        steps = abs(p1[0] - p2[0])
        if p1[0] < p2[0]:
            for i in range(steps + 1):
                board[p1[0] + i][p1[1] + i] += 1
        else:
            for i in range(steps + 1):
                board[p2[0] + i][p2[1] + i] += 1
    elif p1[0] + p1[1] == p2[0] + p2[1]:
        # bottom right to top left diagonal
        steps = abs(p1[0] - p2[0])
        if p1[0] < p2[0]:
            for i in range(steps + 1):
                board[p1[0] + i][p1[1] - i] += 1
        else:
            for i in range(steps + 1):
                board[p2[0] + i][p2[1] - i] += 1

    return board


def printboard(board):
    for row in board:
        print(row)


def main():
    lines = parseinput()
    board = createboard(lines)

    for line in lines:
        board = updateboard(board, line)

    count = len([n for row in board for n in row if n >= 2])
    return count


result = main()
print(result)
