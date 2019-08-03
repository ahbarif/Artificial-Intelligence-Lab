import numpy
import time
import collections
from copy import deepcopy

from GraphGenerator import ConstraintChecker

class AC_2:

    checker = ConstraintChecker()

    def revise(self, X, Y, constraint, csp):
        isRevised = False
        Dx = deepcopy(csp.D[X])
        for x in Dx:
            if self.checker.checkConsistency(x, csp.D[Y], constraint) == False:
                csp.D[X].remove(x)
                isRevised = True
        return isRevised

    def __contains__(self, list, ele):
        for item in list:
            if ele == item: return True
        return False

    def AC2(self, csp):

        n = len(csp.D)
        adjMatrix = numpy.random.randint(1, size=(n, n))
        for edge in csp.constraintList:
            i, j, k = edge
            adjMatrix[i][j] = k

        startTime = time.time()  # AC2 algorithm starts here

        solutionExists = True
        queue = collections.deque()
        queue2 = collections.deque()


        for i in range(0, n):

            for edge in csp.constraintList:
                u, v, w = edge
                if u == i and v < i:
                    queue.append([u, v])
                elif v == i and u < i:
                    queue2.append([u, v])

            while len(queue) != 0:
                while len(queue) != 0:
                    k, m = queue.popleft()

                    revised = self.revise(k, m, adjMatrix[k][m], csp)

                    if revised == True:
                        if len(csp.D[k]) == 0:
                            solutionExists = False
                            queue2.clear()
                            break

                        for u, v, w in csp.constraintList:
                            if u == k and v <= i and v != m:
                                newEdge = [v, u]
                                if self.__contains__(queue2, newEdge) == False:
                                    queue2.append(newEdge)

                queue = deepcopy(queue2)
                queue2.clear()

        endTime = time.time()

        elapsed = (endTime - startTime) * 1000

        return [elapsed, solutionExists, csp.D]
