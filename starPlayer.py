import puzzleBoard
import math


class Player(object):

    def __init__(self):
        self.numMoves = 0



    def boardSolver(self, board, mode):



        for i in range (1200):


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
        toAdd = board.simMoves()
        # toAdd = board.boardState()

        # print(toAdd)
        # print("________________________________")

        # board = Board(-1, toAdd)
        generatedProblems[i].boardState = toAdd[:]
        # generatedProblems = generatedProblems.append(toAdd)
        i+=1

        print ("asldkfjalsdkjfl")

        for bleh in generatedProblems:
            print(bleh.boardState);

    return generatedProblems



