import numpy
from copy import deepcopy
import time

def isConflicting(x1, y1, x2, y2):

  if x1 == x2:
    return True
  elif y1 == y2:
    return True
  else:
    if abs(x1-x2) == abs(y1-y2):
      return True
    else:
      return False


def generateRandomGraph(n):

  queenPos = numpy.random.randint(n, size=n)
  return queenPos

def findConflictVariables(queenPos):
  conflictVariables = []
  vis = {}
  n = len(queenPos)
  for i in range(0, n):
    for j in range(i + 1, n):
      if isConflicting(i, queenPos[i], j, queenPos[j]) == True:
        vis[i] = 1
        vis[j] = 1

  for i in range(0, n):
     if i in vis.keys():
      conflictVariables.append(i)
  return conflictVariables

def findTotalConflicts(X, queenPos):
    # {x, i} th cell e boshabo for i = 0 to 8
    n = len(queenPos)
    availablePos = []
    for i in range(0, n):
        conflictsForthisCell = 0
        for j in range(0, n):
            if j == X:
                continue
            if(isConflicting(X, i, j, queenPos[j])):
                conflictsForthisCell += 1


        availablePos.append(conflictsForthisCell)

    return  availablePos

def printBoardFromPosition(queenPos):
    board = []
    n = len(queenPos)
    for i in range(0, n):
        idx = queenPos[i]
        temp = []
        for j in range(0, n):
            if j == idx:
                temp.append(1)
            else:
                temp.append(0)
        board.append(temp)

    for row in board:
        print(row)

def minConflict(board, maxSteps):

    found = False
    stepCount = 0
    queenPos = deepcopy(board)
    n = len(queenPos)

    for loop in range(0, maxSteps):
     #   print("loop = " , loop)
        conflictVariables = findConflictVariables(queenPos)

        if len(conflictVariables) == 0:
            found = True
            stepCount = loop
            break

        sz = len(conflictVariables)
        idx = numpy.random.randint(sz, size=1)

        X = conflictVariables[idx[0]]
        currentPos = queenPos[X]
        noOfConflicts = n
        newPos = -1

        possibleValues = findTotalConflicts(X, queenPos)

        for i in range(0, len(possibleValues)):
            if possibleValues[i] < noOfConflicts and i != currentPos:
                noOfConflicts = possibleValues[i]
                newPos = i

        if newPos == -1:
            newPos = currentPos

        queenPos[X] = newPos

    return [found, stepCount, queenPos]

def nQueenUtil(n):

    queenPos = generateRandomGraph(n)

    print("Number of Queen: ", n)
    print("Initial Board: ")
    printBoardFromPosition(queenPos)
    print("")

    maxSteps = 10000
    startTime = time.time()
    flag, stepCount, finalPosition = minConflict(queenPos, maxSteps)
    endTime = time.time()

    timeDiff = endTime - startTime
    if(flag == False):
        print("Solution not found")
    else:
        print("Solution found")
        print("Final Board: ")
        printBoardFromPosition(finalPosition)
        print("")
        print("Total number of intermediate steps: ", stepCount+1)
        print("Total Time: ", timeDiff)
        print("")


if __name__ == '__main__':
  #  list = generateGraph(5, 70) #nodes and density



    nQueenUtil(8)
    nQueenUtil(10)
    nQueenUtil(12)
    # n = 0
    # while n <100:
    #     n += 20
    #     nQueenUtil(n)
    #




