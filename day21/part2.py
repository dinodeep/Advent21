

from typing import Counter


def parseinput(file):
    with open(file, "r") as f:
        lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]
    pos1, pos2 = [int(line.split(" ")[-1]) for line in lines]

    return pos1, pos2


def getGameStates():
    # game state = (pos1, score1, pos2, score2)
    # scores range from 0 to 21
    # positions range from 1 to 10
    # (0,0) (1,0) (0,1) (2,0) (1,1) (0,2) (3,0)

    gameStates = []
    # simulate ordered pairs of scores -- order does matter want scores s.t. earlier scores occur only before later scores
    for totalscore in range(42):
        for i in range(totalscore + 1):
            # simulate pairs of positions -- order doesn't matter
            for pos1 in range(1, 11):
                for pos2 in range(1, 11):
                    gameStates.append((pos1, totalscore - i, pos2, i))

    return gameStates


def makeMoves(currState, universeCount):
    pos1, score1, pos2, score2 = currState
    currCount = universeCount[currState]

    wins1, wins2 = 0, 0

    # make states where player 1 moves (creating all new universes -- could be optimized)
    newStates1 = []
    for roll1 in range(1, 4):
        for roll2 in range(1, 4):
            for roll3 in range(1, 4):
                m1 = roll1 + roll2 + roll3
                newPos1 = ((pos1 + m1 - 1) % 10) + 1
                newScore1 = score1 + newPos1
                newStates1.append((newPos1, newScore1, pos2, score2))

    # update counts for terminating 1 moves
    nonTerminatingStates = []
    for state in newStates1:
        _, newScore1, _, _ = state
        if newScore1 >= 21:
            wins1 += currCount
        else:
            nonTerminatingStates.append(state)

    # for each non terminating 1 moves -- make 2 moves
    newStates2 = []
    for state in nonTerminatingStates:
        newPos1, newScore1, pos2, score2 = state
        for roll1 in range(1, 4):
            for roll2 in range(1, 4):
                for roll3 in range(1, 4):
                    m2 = roll1 + roll2 + roll3
                    newPos2 = ((pos2 + m2 - 1) % 10) + 1
                    newScore2 = score2 + newPos2
                    newStates2.append((newPos1, newScore1, newPos2, newScore2))

    # update counts for terminating 2 moves
    for state in newStates2:
        _, _, _, newScore2 = state
        if newScore2 >= 21:
            wins2 += currCount
        else:
            # update counts for non-terminating 1 and 2 moves
            universeCount[state] += currCount

    universeCount[currState] = 0

    return universeCount, wins1, wins2


def printCounts(universeCount):
    for state, count in universeCount.items():
        if count > 0:
            print(f"{state}->{count}")
    print()


def simulateAllGames(pos1, pos2):
    # game state = (pos1, score1, pos2, score2)
    # enumerate all possible game states (tuples of player 1 and 2 positions and scores)
    # game states must be ordered such that previous game states always occur before later game states
    gameStates = getGameStates()

    # create a dictionary with all game states and how many universes of them exist (state -> count map)
    universeCount = {state: 0 for state in gameStates}

    # set the starting game state to one count
    startState = (pos1, 0, pos2, 0)
    universeCount[startState] = 1
    # printCounts(universeCount)

    # initialize statistics of all games
    wins1 = 0
    wins2 = 0

    # enumerate through all ordered game states
    # for each game state occurring k times, simulate player 1 rolling quantum die and add those counts to new states
    for currState in gameStates:
        if universeCount[currState] > 0:
            # input(f"Expanding current state: {currState}->{universeCount[currState]}")
            universeCount, newWins1, newWins2 = makeMoves(currState, universeCount)
            wins1 += newWins1
            wins2 += newWins2

    # return wins
    return wins1, wins2


def main():
    pos1, pos2 = parseinput("hardinput.txt")

    wins1, wins2 = simulateAllGames(pos1, pos2)

    return wins1 if wins1 > wins2 else wins2


result = main()
print(result)
