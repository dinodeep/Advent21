

def parseinput(file):
    with open(file, "r") as f:
        lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]
    pos1, pos2 = [int(line.split(" ")[-1]) for line in lines]

    return pos1, pos2


def getNumSteps(dieMid):
    if dieMid == 100:
        return 99 + 100 + 1
    elif dieMid == 1:
        return 100 + 1 + 2
    else:
        return 3 * dieMid


def movePlayer(initPos, dieMid):
    # mod 10 forwardSteps to avoid unnecessary circular movement
    forwardSteps = getNumSteps(dieMid) % 10
    newDieMid = ((dieMid + 2) % 100) + 1

    finalPos = ((initPos + forwardSteps - 1) % 10) + 1

    return finalPos, newDieMid


def playGame(pos1, pos2):
    score1, score2 = 0, 0
    nturns = 0
    dieMid = 2     # keep die value on its middle roll for each turn -- easier calculations

    # positions are from 1...10
    # deterministc die rolls are from 1...100

    # play game
    while True:
        # player 1 goes first
        pos1, dieMid = movePlayer(pos1, dieMid)
        score1 += pos1

        # update game stats and check for win
        nturns += 1
        if score1 >= 1000:
            return score1, score2, nturns

        # repeat for player 2
        pos2, dieMid = movePlayer(pos2, dieMid)
        score2 += pos2

        nturns += 1
        if score2 >= 1000:
            return score1, score2, nturns


def main():
    pos1, pos2 = parseinput("hardinput.txt")

    score1, score2, nturns = playGame(pos1, pos2)

    loserScore = score1 if score1 < 1000 else score2

    # number of die rolls == 3 * nturns
    return loserScore * (3 * nturns)


result = main()
print(result)
