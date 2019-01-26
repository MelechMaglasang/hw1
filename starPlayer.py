import puzzleBoard
import math
import heapq
import copy


class myHeap(object):
    def __init__(self, initial=None, key=lambda x:x):
       self.key = key
       if initial:
           self._data = [(key(item), item) for item in initial]
           heapq.heapify(self._data)
       else:
           self._data = []

    def push(self, item):
       heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
       return heapq.heappop(self._data)[1]
    def isEmpty(self):
        if (len(self._data) == 0):
            return True
        else:
            return False

class Player(object):

    def __init__(self):
        self.numMoves = 0



    def boardSolver(self, board, hMode):

        if (hMode == 0):

            board.h1Val = board.calch1()

            minQueue = myHeap()

            initial = [board.h1Val + self.numMoves, board]

            minQueue.push(initial)

            while (minQueue.isEmpty() == False):
                currBoard = minQueue.pop()

                #If thse heuristic is zero then it is at goal
                if (board.calch1 == 0):
                    return currBoard

                self.numMoves += 1

                #Grabs for where the zero and returns list of possible moves
                blankIndex = currBoard[1].boardState.index(0)
                availMoves = currBoard[1].getMoves(blankIndex)

                for move in availMoves:
                    tempBoard = copy.deepcopy(currBoard[1])

                    tempBoard.doMove(blankIndex, move)

                    # Check if move has been done before?

                    tempBoard.h1Val = tempBoard.calch1()

                    nextNode = [tempBoard.h1Val + self.numMoves, tempBoard]
                    minQueue.push(nextNode)





       

        


        return


def genRandProblems(numBoards):
    generatedProblems = []
    for x in range(numBoards):
        temp = puzzleBoard.Board(-1, [0,1,2,3,4,5,6,7,8])
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
        i+=1

        # print ("asldkfjalsdkjfl")

        # for bleh in generatedProblems:
        #     print(bleh.boardState);

    return generatedProblems



def main():
    # print("Test")

    # problemList generatedProblems

    # board = puzzleBoard.Board(-1, [0,1,2,3,4,5,6,7,8] )
    # board.createDict()
    
    # problemSet =  genRandProblems(1200)

    player = Player()

    player.boardSolver(genRandProblems(1)[0], 0)

    # print(len(problemSet))


   

if __name__ == "__main__":
    main()

