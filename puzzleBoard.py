POSSIBLE_MOVES = dict()

class Board(object):
    parity = -1
    boardState = [0,1,2,3,4,5,6,7,8,9]

    def __init__(self, parity, boardState):
        self.parity = parity
        self.boardState = boardState

def createDict(board):
    POSSIBLE_MOVES[0] = [1,3]
    POSSIBLE_MOVES[1] = [0,2,4]
    POSSIBLE_MOVES[2] = [1,5]
    POSSIBLE_MOVES[3] = [0,4,6]
    POSSIBLE_MOVES[4] = [1,3,5,7]
    POSSIBLE_MOVES[5] = [2,4,8]
    POSSIBLE_MOVES[6] = [3,7]
    POSSIBLE_MOVES[7] = [4,6,8]
    POSSIBLE_MOVES[8] = [5,7]
    

       
def getMoves(tileIndex):
    return POSSIBLE_MOVES[tileIndex]

# def calculateParity():
#     return

# def doMoves():
#     return

# def updateBoard(newBoard):
#     return
    
def simMoves(numMoves):
    return

def printBoard(board):
    return

def main():
    print("Test")

if __name__ == "__main__":
    main()
