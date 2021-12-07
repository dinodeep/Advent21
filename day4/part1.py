

def parseInput():
    numbers = []
    boards = []
    with open("input1.txt", "r") as f:
        lines = f.readlines()
        numbers = list(map(int, lines[0].split(",")))
        board = []
        for line in lines[2:]:
            if len(line) > 2:
                # board row
                # make space between all numbers exactly 1
                pieces = [part for part in line.split(" ") if part != ""]
                row = list(map(int, pieces))
                board.append(row)
            else:
                # create new board
                boards.append(board)
                board = []
        boards.append(board)

    return numbers, boards


def updateBoards(boards, number):
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == number:
                    boards[i][j][k] = -1

    return boards


def findWinner(boards):
    for board in boards:
        # check if any rows have all -1s
        for row in board:
            if all([num == -1 for num in row]):
                return board

        # check if any columns have all -1s
        for j in range(len(board[0])):
            allFound = True
            for i in range(len(board)):
                if board[i][j] != -1:
                    allFound = False
            if allFound:
                return board

    return None


def getScore(board, number):
    unfoundNums = [num for row in board for num in row if num != -1]
    return number * sum(unfoundNums)


def main():

    # parse numbers and boards
    numbers, boards = parseInput()

    # for each drawn number
    for number in numbers:
        # update boards
        boards = updateBoards(boards, number)

        # check if there is a winning board
        winner = findWinner(boards)

        # calculate score of winning board using winning number
        if winner is not None:
            return getScore(winner, number)


result = main()
print(result)
