import time
from copy import deepcopy

from GraphGenerator import ConstraintChecker

class AC_1:

    checker = ConstraintChecker()

    def revise(self, X, Y, constraint, csp):
        isRevised = False
        Dx = deepcopy(csp.D[X])
        for x in Dx:
            if self.checker.checkConsistency(x, csp.D[Y], constraint) == False:
                csp.D[X].remove(x)
                isRevised = True
        return isRevised

    def AC1(self, csp):

        startTime = time.time()

        solutionExists = True
        queue = []


        for i, j, k in csp.constraintList:
            queue.append([i, j, k])

        changed = True
        while changed == True:

            changed = False
            for u, v, w in queue:
                revised = self.revise(u, v, w, csp)

                if revised == True:
                    changed = True
                    if len(csp.D[u]) == 0:
                        solutionExists = False
                        break

        endTime = time.time()

        elapsed = (endTime - startTime) * 1000

        return [elapsed, solutionExists, csp.D]
