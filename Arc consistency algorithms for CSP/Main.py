from AC_3 import AC_3
from GraphGenerator import *
from AC_1 import *
from AC_2 import *
from AC_4 import *
from matplotlib import pyplot

def function_domSize_vs_time():

    domSize = []

    timeAC = [[], [], [], []]

    csp = CSP()
    ac1 = AC_1()
    ac2 = AC_2()
    ac3 = AC_3()
    ac4 = AC_4()


    for p in range(30, 101, 5):

            n = 40

            avgTime = [0, 0, 0, 0]
            iter = 20
            for j in range(0, iter):
                    csp.generateProblem(n, p, p, 30)


                    avgTime[0] += ac1.AC1(deepcopy(csp))[0]
                    avgTime[1] += ac2.AC2(deepcopy(csp))[0]
                    avgTime[2] += ac3.AC3(deepcopy(csp))[0]
                    avgTime[3] += ac4.AC4(deepcopy(csp))[0]


            domSize.append(p)

            for i in range(0, 4):
                timeAC[i].append(avgTime[i]/iter)


    pyplot.plot(domSize, timeAC[0], color='g', label='AC1')
    pyplot.plot(domSize, timeAC[1], color='r', label='AC2')
    pyplot.plot(domSize, timeAC[2], color='b', label='AC3')
    pyplot.plot(domSize, timeAC[3], color='y', label='AC4')

    for i in range(0, 4):
        print("")
        for data in timeAC[i]:
            print(data)

    pyplot.xlabel('Domain Size')
    pyplot.ylabel('Average CPU time (msec)')
    pyplot.title('Performance Analysis of Arc Consistency Algorithm\nNodes = 40, desnsity = 0.30')
    pyplot.legend(loc='upper left')


    pyplot.savefig('domain_vs_time.png')
    pyplot.show()

def function_density_vs_time():

    density = []

    timeAC = [[], [], [], []]

    csp = CSP()
    ac1 = AC_1()
    ac2 = AC_2()
    ac3 = AC_3()
    ac4 = AC_4()


    for p in range(10, 60, 2):

            n = 40
            avgTime = [0, 0, 0, 0]
            iter = 20
            for j in range(0, iter):
                    csp.generateProblem(n, 40, 40, p)

                    avgTime[0] += ac1.AC1(deepcopy(csp))[0]
                    avgTime[1] += ac2.AC2(deepcopy(csp))[0]
                    avgTime[2] += ac3.AC3(deepcopy(csp))[0]
                    avgTime[3] += ac4.AC4(deepcopy(csp))[0]

            density.append(p/100.0)

            for i in range(0, 4):
                timeAC[i].append(avgTime[i]/iter)

    pyplot.plot(density, timeAC[0], color='g', label='AC1')
    pyplot.plot(density, timeAC[1], color='r', label='AC2')
    pyplot.plot(density, timeAC[2], color='b', label='AC3')
    pyplot.plot(density, timeAC[3], color='y', label='AC4')

    for i in range(0, 4):
        print("")
        for data in timeAC[i]:
            print(data)

    pyplot.xlabel('Density')
    pyplot.ylabel('Average CPU time (msec)')
    pyplot.title('Performance Analysis of Arc Consistency Algorithm\nDomain size = 30, number of nodes = 40')
    pyplot.legend(loc='upper left')


    pyplot.savefig('density_vs_time.png')
    pyplot.show()


def function_node_vs_time():

    numberOfNodes = []

    timeAC = [[], [], [], []]

    csp = CSP()
    ac1 = AC_1()
    ac2 = AC_2()
    ac3 = AC_3()
    ac4 = AC_4()


    for n in range(10, 110, 3):

            avgTime = [0, 0, 0, 0]
            iter = 20
            for j in range(0, iter):
                    csp.generateProblem(n, 30, 30, 40)

                    avgTime[0] += ac1.AC1(deepcopy(csp))[0]
                    avgTime[1] += ac2.AC2(deepcopy(csp))[0]
                    avgTime[2] += ac3.AC3(deepcopy(csp))[0]
                    avgTime[3] += ac4.AC4(deepcopy(csp))[0]


            numberOfNodes.append(n)

            for i in range(0, 4):
                timeAC[i].append(avgTime[i]/iter)


    pyplot.plot(numberOfNodes, timeAC[0], color='g', label='AC1')
    pyplot.plot(numberOfNodes, timeAC[1], color='r', label='AC2')
    pyplot.plot(numberOfNodes, timeAC[2], color='b', label='AC3')
    pyplot.plot(numberOfNodes, timeAC[3], color='y', label='AC4')

    for i in range(0, 4):
        print("")
        for data in timeAC[i]:
            print(data)

    pyplot.xlabel('Number of nodes')
    pyplot.ylabel('Average CPU time (msec)')
    pyplot.title('Performance Analysis of Arc Consistency Algorithm\nDomain size = 30, Edge probability = 0.40' )
    pyplot.legend(loc='upper left')
    pyplot.savefig('node_vs_time.png')

    pyplot.show()


if __name__ == '__main__':


    function_node_vs_time()
  #   function_domSize_vs_time()
  #   function_density_vs_time()