import math
import random
import networkx

class GraphGenerator:

    def generateGraph(self, n, density):
        constraintList = []
        G = networkx.erdos_renyi_graph(n, density/100.0, False)

        for item in G.edges:
            u = item[0]
            v = item[1]
            idx = random.randint(1, 5)

            if idx == 1:
                constraintList.append([u, v, 1])
                constraintList.append([v, u, 5])
            elif idx == 2:
                constraintList.append([u, v, 2])
                constraintList.append([v, u, 6])
            elif idx == 3:
                constraintList.append([u, v, 3])
                constraintList.append([v, u, 3])
            else:
                constraintList.append([u, v, 4])
                constraintList.append([v, u, 4])
        return constraintList


    def generateDomains(self, n, minDomainSize, maxDomainSize):
        D = []
        for x in range(0, n):
            domainSize = random.randint(minDomainSize, maxDomainSize)
            myDomain = random.sample(range(0, 1000), domainSize)
            D.append(myDomain)
        return D


class ConstraintChecker:
    def checkConstraint1(self, x, Dy):
        for y in Dy:
            if x > y: return True
        return False

    def checkConstraint2(self, x, Dy):
        for y in Dy:
            if 3 * x < 4 * y: return True
        return False

    def checkConstraint3(self, x, Dy):
        for y in Dy:
            if (x + y) % 10 == 0: return True
        return False

    def checkConstraint4(self, x, Dy):
        for y in Dy:
            if math.gcd(x, y) != 1: return True
        return False

    def checkConstraint5(self, x, Dy):
        for y in Dy:
            if x < y: return True
        return False

    def checkConstraint6(self, x, Dy):
        for y in Dy:
            if 4 * x > 3 * y: return True
        return False

    def checkConsistency(self, x, Dy, constraintNumber):
        if constraintNumber == 1:
            return self.checkConstraint1(x, Dy)
        elif constraintNumber == 2:
            return self.checkConstraint2(x, Dy)
        elif constraintNumber == 3:
            return self.checkConstraint3(x, Dy)
        elif constraintNumber == 4:
            return self.checkConstraint4(x, Dy)
        elif constraintNumber == 5:
            return self.checkConstraint5(x, Dy)
        elif constraintNumber == 6:
            return self.checkConstraint6(x, Dy)


class CSP:
    constraintList = []
    D = []
    def generateProblem(self, nodes, minDomainSize, maxDomainSize, density):
        generator = GraphGenerator()
        self.constraintList = generator.generateGraph(nodes, density)
        self.D = generator.generateDomains(nodes, minDomainSize, maxDomainSize)


