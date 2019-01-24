import puzzleBoard
import math


class Player(object):

    def __init__(self):
        self.hMode = 1
        self.numMoves = 0


    def getRow(self,index):

        if(index < 4):
            return 0
        elif (index < 6):
            return 1
        else:
            return 2


    def calch1(self, boardState):

        numMisplaced = 0
        for i in len(boardState):
            if (boardState[i] != i):
                numMisplaced += 1

        return numMisplaced

    def calch2(self, boardState):

        numMisplaced = 0
        for i in len(boardState):
            if (boardState[i] != i):

                #column + row
                numMisplaced += boardState[i] % 3 + math.fabs(self.getRow(boardState[i]) - i % 3 )

        return numMisplaced

