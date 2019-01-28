import puzzleBoard
import math
import heapq
import copy

class Player(object):

    def __init__(self):
        self.numMoves = 0

    def boardSolver(self, board, hMode):

        if (hMode == 0):

            board.h1Val = board.calch1()

            count = 0

            minQueue = []

            initial = [board.h1Val + board.numMoves, count , board]

            heapq.heappush(minQueue , initial)

            visited = set()

            while ( minQueue):

                currBoard = heapq.heappop(minQueue)

                visited.add(tuple(currBoard[2].boardState))



                # If thse heuristic is zero then it is at goal
                
                if (currBoard[2].calch1() == 0):
                    print (currBoard[2].numMoves)
                    return currBoard

                # self.numMoves += 1

                # Grabs for where the zero and returns list of possible moves
                blankIndex = currBoard[2].boardState.index(0)
                availMoves = currBoard[2].getMoves(blankIndex)

                for move in availMoves:
                    tempBoard = copy.deepcopy(currBoard[2])

                    tempBoard.doMove(blankIndex, move)

                    tempBoard.numMoves += 1

                    # Check if move has been done before?
                    
                    if (tuple(tempBoard.boardState) not in visited):
                        tempBoard.h1Val = tempBoard.calch1()

                        count += 1

                        nextNode = [tempBoard.h1Val + tempBoard.numMoves, count , tempBoard]
                        heapq.heappush(minQueue , nextNode)                    


def genRandProblems(numBoards):
    generatedProblems = []
    for x in range(numBoards):
        temp = puzzleBoard.Board(0, [0, 1, 2, 3, 4, 5, 6, 7, 8])
        generatedProblems.append(temp)

    # print(generatedProblems[1].boardState)

    # global generatedProblems
    # generatedProblems = list()
    i = 0

    while (i < numBoards):
        # board.createDict()
        # board = board.simMoves()
        toAdd = generatedProblems[i].simMoves()
        # toAdd = board.boardState()

        # print(toAdd)
        # print("________________________________")

        # board = Board(-1, toAdd)
        generatedProblems[i].boardState = toAdd[:]
        # generatedProblems = generatedProblems.append(toAdd)
        i += 1

        # print ("asldkfjalsdkjfl")

        # for bleh in generatedProblems:
        #     print(bleh.boardState);

    return generatedProblems


def main():
    # print("Test")

    # problemList generatedProblems

    # board = puzzleBoard.Board(-1, [1,0,2,3,4,5,6,7,8] )
    # board.createDict()

    problemSet =  genRandProblems(1200)

    player = Player()

    for board in problemSet:
        player.boardSolver(board, 0)



    # print(len(problemSet))


if __name__ == "__main__":
    main()
