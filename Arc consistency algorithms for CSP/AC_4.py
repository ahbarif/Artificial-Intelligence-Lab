import collections, math, time
from copy import deepcopy

class AC_4:

    def isConsistent(self, x, y, cid):
        if cid == 1:
            return x > y
        elif cid == 2:
            return 3 * x < 4 * y
        elif cid == 2:
            return x != y
        elif cid == 3:
            return (x + y) % 10 == 0
        elif cid == 4:
            return math.gcd(x, y) != 1
        elif cid == 5:
            return x < y
        elif cid == 6:
            return 4 * x > 3 * y

    def AC4(self, csp):

        solutionExists = True
        counter = {}
        S = {}
        M = {}
        queue = collections.deque()
        n = len(csp.D)

        startTime = time.time()

        for i, j, k in csp.constraintList:
            for ai in csp.D[i]:
                    counter[(i, ai, j)] = 0

        for vj in range(0, n):
            for aj in csp.D[vj]:
                S[(vj, aj)] = []
                M[(vj, aj)] = True

        for vi, vj, k in csp.constraintList:

            Di = deepcopy(csp.D[vi])

            for ai in Di:
                total = 0
                for aj in csp.D[vj]:
                    if self.isConsistent(ai, aj, k) == True:
                        total += 1
                        S[(vj, aj)].append([vi, ai])

                if total == 0:
                    csp.D[vi].remove(ai)

                    M[(vi, ai)] = False
                    if len(csp.D[vi]) == 0:
                        return [(time.time() - startTime) * 1000, False, csp.D]
                    queue.append([vi, ai])

                else:
                    counter[(vi, ai, vj)] = total


        while len(queue) > 0:
            vj, aj = queue.popleft()

            for vi, ai in S[(vj, aj)]:
                    if M[vi, ai] == 0: continue
                    counter[(vi, ai, vj)] -= 1
                    if counter[(vi, ai, vj)] == 0 and M[(vi, ai)] == True:

                        csp.D[vi].remove(ai)
                        M[(vi, ai)] = False

                        if len(csp.D[vi]) == 0:
                            return [(time.time() - startTime) * 1000, False, csp.D]

                        queue.append([vi, ai])


        endTime = time.time()

        elapsed = (endTime - startTime)*1000

        return [elapsed, solutionExists, csp.D]
