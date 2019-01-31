import puzzleBoard
import math
import heapq
import copy
import csv


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

            # If thse heuristic is zero then it is at goal

            if (hMode == 0 and currBoard[2].calch1() == 0):

                # print ("Number of Moves:", currBoard[2].numMoves)
                # print ("Number of Nodes Generated:", nodesGenerated)
                # print ("h1 Branching Factor: ", branchingFactor(
                #     nodesGenerated, currBoard[2].numMoves))

                return [currBoard[2].numMoves, nodesGenerated, branchingFactor(nodesGenerated, currBoard[2].numMoves), "h1"]

            elif (hMode == 1 and currBoard[2].calch2() == 0):
                # print ("Number of Moves:", currBoard[2].numMoves)
                # print ("Number of Nodes Generated:", nodesGenerated)
                # print ("h2 Branching Factor: ", branchingFactor(
                #     nodesGenerated, currBoard[2].numMoves))

                return [currBoard[2].numMoves, nodesGenerated, branchingFactor(nodesGenerated, currBoard[2].numMoves), "h2"]

            elif (hMode == 2 and currBoard[2].calch3() == 0):
                # print ("Number of Moves:", currBoard[2].numMoves)
                # print ("Number of Nodes Generated:", nodesGenerated)
                # print ("h3 Branching Factor: ", branchingFactor(
                #     nodesGenerated, currBoard[2].numMoves))

                return [currBoard[2].numMoves, nodesGenerated, branchingFactor(nodesGenerated, currBoard[2].numMoves), "h3"]

            # self.numMoves += 1

            # Grabs for where the zero and returns list of possible moves
            blankIndex = currBoard[2].boardState.index(0)
            availMoves = currBoard[2].getMoves(blankIndex)

            for move in availMoves:
                tempBoard = copy.deepcopy(currBoard[2])

                tempBoard.doMove(blankIndex, move)

                tempBoard.numMoves += 1

                # nodesGenerated += 1

                # Check if move has been done before?

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
    # print("Test")

    # problemList generatedProblems

    # board = puzzleBoard.Board(0, [7, 2, 4, 5, 0, 6, 8, 3, 1])
    board = puzzleBoard.Board(0, [2, 0, 6, 1, 3, 4, 7, 5, 8])
    # board = puzzleBoard.Board(0, [0, 1, 2, 4, 3, 5, 6, 7, 8])

    # board.createDict()

    problemSet = genRandProblems(1000, 30)

    player = Player()

    board.simNumMoves(2)
    for i in problemSet:
        print (i.calch3())


    # print (board.boardState)

    # with open('Test.csv', mode='w') as h1File:
    #     test_writer = csv.writer(
    #         h1File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     for i in range(2, 10, 2):
    #         print (i)

    #         numSeen = 0
    #         while(numSeen < 100):

    #             if (i >= 20):
    #                 dSet = genRandProblems(1, -2)
    #             else:
    #                 dSet = genRandProblems(1, i)

    #             res1 = player.boardSolver(dSet[0], 0)
    #             res2 = player.boardSolver(dSet[0], 1)
    #             res3 = player.boardSolver(dSet[0], 2)

    #             if (res1[0] == i and res2[0] == i and res2[0] == i):
    #                 # Write results here?
    #                 test_writer.writerow(res1)
    #                 test_writer.writerow(res2)
    #                 test_writer.writerow(res3)

    #                 numSeen += 1

    # print (player.boardSolver(board, 2))

    # board.calch2()

    # with open('h1Test.csv', mode='w') as h1File:
    #     test_writer = csv.writer(h1File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #     for i in problemSet:
    #         # player = Player()
    #         res = player.boardSolver(i, 0)

    #         if (res[0] > 1):
    #             test_writer.writerow(res)

    # with open('h1TestHigh2.csv', mode='w') as h1File:
    #     test_writer = csv.writer(h1File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #     for i in problemSet:
    #         # player = Player()
    #         res = player.boardSolver(i, 0)

    #         if (res[0] > 1):
    #             test_writer.writerow(res)
    # print(len(problemSet))

    # test_writer.close()
if __name__ == "__main__":
    main()
