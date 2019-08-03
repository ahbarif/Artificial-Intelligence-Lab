import time, collections
from copy import deepcopy

from GraphGenerator import ConstraintChecker

class AC_3:

    checker = ConstraintChecker()

    def revise(self, X, Y, constraint, csp):
        isRevised = False
        Dx = deepcopy(csp.D[X])
        for x in Dx:
            if self.checker.checkConsistency(x, csp.D[Y], constraint) == False:
                csp.D[X].remove(x)
                isRevised = True
        return isRevised

    def generateNeighborList(self, csp):
        n = len(csp.D)
        list = []
        for i in range(0, n): list.append([])

        for u, v, w in csp.constraintList:
            list[v].append([u, v, w])
        return list


    def AC3(self, csp):

        adjList = self.generateNeighborList(csp)

        startTime = time.time()

        solutionExists = True
        queue = collections.deque()
        M = {}

        for i, j, k in csp.constraintList:
            queue.append([i, j, k])
            M[(i, j)] = 1

        while len(queue) != 0:
            u, v, k = queue.popleft()
            M[(u, v)] = 0

            revised = self.revise(u, v, k, csp)

            if revised == True:
                if len(csp.D[u]) == 0:
                    solutionExists = False
                    break

                for i, j, k in adjList[u]:
                    if i != v:
                        newEdge = [i, j, k]
                        if M[(i, u)] == 0:
                            queue.append(newEdge)
                            M[(i, u)] = 1

        endTime = time.time()
        elapsed = (endTime - startTime) * 1000

        return [elapsed, solutionExists, csp.D]