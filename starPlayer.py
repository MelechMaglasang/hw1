import puzzleBoard
import math


class Player(object):

    def __init__(self):
        self.numMoves = 0



    def boardSolver(self, genProblems):

        for item in genProblems:
            # print(item.boardState)
            item.printBoard()
            # print(item)
            print("_________________________")
            continue

        


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
    
    problemSet =  genRandProblems(1200)

    player = Player()

    player.boardSolver(problemSet)

    print(len(problemSet))


   

if __name__ == "__main__":
    main()

