from collections import Counter


def parseinput(file):

    with open(file, "r") as f:
        lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]
    split = lines.index("")

    points = lines[:split]
    folds = lines[split + 1:]

    points = [tuple(map(int, point.split(","))) for point in points]
    folds = [fold.split(" ")[-1] for fold in folds]

    n = max([point[0] for point in points]) + 1
    m = max([point[1] for point in points]) + 1

    board = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in points:
        board[x][y] = 1

    return board, folds


def printboard(board):
    for row in board:
        print(row)
    print()


def rot90cw(board):
    n = len(board)
    m = len(board[0])

    newboard = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            newboard[i][j] = board[n - 1 - j][i]

    return newboard


def horizfold(board, idx):
    n = len(board)
    m = len(board[0])

    # out of range fold
    if idx < 0 or n <= idx:
        return board

    board[idx] = [2] * m

    # fold occurs on some row in the board
    # for each dot in portion of board below fold, move it up if it fits
    for i in range(idx + 1, n):
        for j in range(m):
            dist = i - idx
            if board[i][j] == 1 and 0 <= idx - dist:
                board[idx - dist][j] = 1

    # return board before fold
    newboard = [board[i] for i in range(idx)]
    return newboard


def foldboard(board, fold):

    dim = fold[0]
    idx = int(fold.split("=")[-1])

    if dim == "x":
        newboard = horizfold(board, idx)
    else:
        board = rot90cw(board)
        newboard = horizfold(board, idx)
        newboard = rot90cw(rot90cw(rot90cw(newboard)))

    return newboard


def main():
    board, folds = parseinput("hardinput.txt")

    board = foldboard(board, folds[0])

    return len([1 for row in board for num in row if num == 1])


result = main()
print(result)
