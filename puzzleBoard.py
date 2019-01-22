import random

POSSIBLE_MOVES = dict()
# generatedProblems = []

class Board(object):
    parity = -1
    boardState = [0,1,2,3,4,5,6,7,8,9]

    def __init__(self, parity, boardState):
        self.parity = parity
        self.boardState = boardState

    def createDict(self):
        POSSIBLE_MOVES[0] = [1,3]
        POSSIBLE_MOVES[1] = [0,2,4]
        POSSIBLE_MOVES[2] = [1,5]
        POSSIBLE_MOVES[3] = [0,4,6]
        POSSIBLE_MOVES[4] = [1,3,5,7]
        POSSIBLE_MOVES[5] = [2,4,8]
        POSSIBLE_MOVES[6] = [3,7]
        POSSIBLE_MOVES[7] = [4,6,8]
        POSSIBLE_MOVES[8] = [5,7]
        

        
    def getMoves(self, tileIndex):
        return POSSIBLE_MOVES[tileIndex]

    # def calculateParity():
    #     return

    # def doMoves():
    #     return

    # def updateBoard(newBoard):
    #     return

    # def switchTiles(self, sourceInd, targetV):
    #     sourceInd = self.boardState.index(source)
    #     targetInd = self.boardState.index(targetVal)
    #     temp = targetInd
    #     sourceInd = 

    def simMoves(self):
        numSimMoves = random.randrange(1, 50, 1)
        print("Simulated moves:", numSimMoves)

        for i in range(numSimMoves):
            blankInd = self.boardState.index(0)
            possibleMoves = self.getMoves(blankInd)
            chosenMove = random.choice(possibleMoves)

            tempVal = self.boardState[chosenMove]
            self.boardState[chosenMove] = self.boardState[blankInd]
            self.boardState[blankInd] = tempVal
        print("New Board State:", self.boardState)
        return self.boardState

    def printBoard(self):
        for i in range (3):
            print ( str(self.boardState[0+i]) + " " + str( self.boardState[1+i]) +" "+ str(self.boardState[2+i]) )

        return

def genRandProblems(board):
    generatedProblems = []
    for x in range(5):
        temp = Board(-1, [-1,-1,-1,-1,-1,-1,-1,-1,-1])
        generatedProblems.append(temp)
    
    # print(generatedProblems[1].boardState)

    # global generatedProblems
    # generatedProblems = list()
    i = 0
    while (i < 5):
        # board.createDict()
        # board = board.simMoves()
        # toAdd = board.simMoves()
        # toAdd = board.boardState

        # print(toAdd)
        # print("________________________________")

        # board = Board(-1, toAdd)
        generatedProblems[i].boardState = board.simMoves()
        # generatedProblems = generatedProblems.append(toAdd)
        i+=1

    return generatedProblems



def main():
    # print("Test")

    # problemList generatedProblems

    board = Board(-1, [0,1,2,3,4,5,6,7,8] )
    board.createDict()
    
    problemSet =  genRandProblems(board)


    for item in problemSet:
        print(item.boardState)
        # item.printBoard()
        # print(item)
        # print("_________________________")
        continue

if __name__ == "__main__":
    main()
