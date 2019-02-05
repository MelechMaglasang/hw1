import puzzleBoard
import math
import heapq
import copy
import csv

# Player class that utlizes puzzleBoard.py to conduct A* heuristic testing for the 8-puzzle
class Player(object):

    def __init__(self):
        self.numMoves = 0

    def boardSolver(self, board, hMode):

        count = 0

        minQueue = []

        if (hMode == 0):

            board.h1Val = board.calch1()

            initial = [board.h1Val + board.numMoves, count, board]

        elif (hMode == 1):
            board.h2Val = board.calch2()

            initial = [board.h2Val + board.numMoves, count, board]

        else:
            board.h3Val = board.calch3()

            initial = [board.h3Val + board.numMoves, count, board]

        heapq.heappush(minQueue, initial)

        nodesGenerated = 1

        visited = set()

        while (minQueue):

            currBoard = heapq.heappop(minQueue)

            visited.add(tuple(currBoard[2].boardState))

            # Checks for if the goal state has been reached
            if (hMode == 0 and currBoard[2].calch1() == 0):
                return [currBoard[2].numMoves, nodesGenerated, branchingFactor(nodesGenerated, currBoard[2].numMoves), "h1"]

            elif (hMode == 1 and currBoard[2].calch2() == 0):
                return [currBoard[2].numMoves, nodesGenerated, branchingFactor(nodesGenerated, currBoard[2].numMoves), "h2"]

            elif (hMode == 2 and currBoard[2].calch3() == 0):
                return [currBoard[2].numMoves, nodesGenerated, branchingFactor(nodesGenerated, currBoard[2].numMoves), "h3"]

            # Grab data for the next set of moves
            blankIndex = currBoard[2].boardState.index(0)
            availMoves = currBoard[2].getMoves(blankIndex)

            for move in availMoves:
                tempBoard = copy.deepcopy(currBoard[2])

                tempBoard.doMove(blankIndex, move)

                tempBoard.numMoves += 1

                # Check if move has been done before

                if (tuple(tempBoard.boardState) not in visited):
                    count += 1

                    nodesGenerated += 1

                    if (hMode == 0):
                        tempBoard.h1Val = tempBoard.calch1()
                        nextNode = [tempBoard.h1Val +
                                    tempBoard.numMoves, count, tempBoard]

                    elif (hMode == 1):
                        tempBoard.h2Val = tempBoard.calch2()
                        nextNode = [tempBoard.h2Val +
                                    tempBoard.numMoves, count, tempBoard]

                    else:
                        tempBoard.h3Val = tempBoard.calch3()
                        nextNode = [tempBoard.h3Val +
                                    tempBoard.numMoves, count, tempBoard]

                    heapq.heappush(minQueue, nextNode)


def genRandProblems(numBoards, num):

    generatedProblems = []
    for x in range(numBoards):
        temp = puzzleBoard.Board(0, [0, 1, 2, 3, 4, 5, 6, 7, 8])
        generatedProblems.append(temp)

    i = 0

    while (i < numBoards):

        if (num > 0):
            toAdd = generatedProblems[i].simNumMoves(num)
        else:
            toAdd = generatedProblems[i].simMoves()

        generatedProblems[i].boardState = toAdd[:]

        i += 1

    return generatedProblems


def branchingFactor(N, d):
    N += 1

    if (d == 0):
        return 0

    initialGuess = N ** (1.0 // d)

    upperBound = initialGuess + (initialGuess)

    lowerBound = initialGuess - (initialGuess)

    while (initialGuess < upperBound and initialGuess > lowerBound):

        nGuess = 0
        for i in range(d+1):
            nGuess += initialGuess ** i

        if (nGuess <= N + 1 and nGuess >= N - 1):
            return initialGuess

        elif (nGuess > N):
            initialGuess -= (.005*initialGuess)
        elif (nGuess < N):
            initialGuess += (.005*initialGuess)

    return initialGuess


def main():

    # Declare Player
    player = Player()

    # Conducting Tests
    with open('Test.csv', mode='w') as h1File:
        test_writer = csv.writer(
            h1File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(2, 26, 2):
            print(i)

            numSeen = 0
            while(numSeen < 100):

                if (i >= 20):
                    dSet = genRandProblems(1, -2)
                else:
                    dSet = genRandProblems(1, i)

                res1 = player.boardSolver(dSet[0], 0)
                res2 = player.boardSolver(dSet[0], 1)
                res3 = player.boardSolver(dSet[0], 2)

                if (res1[0] == i and res2[0] == i and res2[0] == i):
                    # Write results here?
                    test_writer.writerow(res1)
                    test_writer.writerow(res2)
                    test_writer.writerow(res3)

                    numSeen += 1


if __name__ == "__main__":
    main()
