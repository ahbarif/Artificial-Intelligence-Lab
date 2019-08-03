# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def generatePath(source, destination, parent):  

    # This method generates the path from source to destination using parent array

    paths = []

    while destination != source:
        par = parent[destination][0]
        paths.append(parent[destination][1])
        destination = parent[destination][0]

    paths.reverse()

    return paths


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    source = problem.getStartState()
    stack = util.Stack()
    visited = [source]
    parent = {}
    stack.push(source)

    while not stack.isEmpty():
        top = stack.pop()
        visited.append(top)

        if problem.isGoalState(top):
            destination = top
            break;

        neighbours = problem.getSuccessors(top)

        for adjacent in neighbours:
            vertex = adjacent[0]
            nextStep = adjacent[1]

            if vertex not in visited:
                stack.push(vertex)
                parent[vertex] = (top, nextStep)

    return generatePath(source, destination, parent)    

    util.raiseNotDefined()


def breadthFirstSearch(problem):
  #  """Search the shallowest nodes in the search tree first."""
  #  "*** YOUR CODE HERE ***"

    source = problem.getStartState()
    queue = [source]
    parent = {}
    parent[source] = (source, [])
    visited = [source]

    while len(queue)>0:
        top = queue.pop(0)
        if problem.isGoalState(top):
            destination = top
            break;

        neighbours = problem.getSuccessors(top)

        for adjacent in neighbours:
            vertex = adjacent[0]
            nextStep = adjacent[1]

            if vertex not in visited:
                queue.append(vertex)
                visited.append(vertex)
                parent[vertex] = (top, nextStep)

    return generatePath(source, destination, parent)
   

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    source = problem.getStartState()
    priorityQueue = util.PriorityQueue()
    parent = {}
    visited = {}

    parent[source] = (source, [])
    visited[source] = 1
    priorityQueue.push(source, 0);

    while not priorityQueue.isEmpty():
        top = priorityQueue.pop()

        if problem.isGoalState(top):
            destination = top
            break;

        neighbours = problem.getSuccessors(top)

        for adjacent in neighbours:
            vertex = adjacent[0]
            nextStep = adjacent[1]
            cost = adjacent[2]

            if vertex not in visited.keys():
                visited[vertex] = visited[top] + cost
                priorityQueue.push(vertex, visited[vertex])
                parent[vertex] = (top, nextStep)

            elif visited[top] + cost < visited[vertex]:
                visited[vertex] = visited[top] + cost
                priorityQueue.push(vertex, visited[vertex])
                parent[vertex] = (top, nextStep)

    return generatePath(source, destination, parent)

    util.raiseNotDefined()


def depthLimitedSearch(problem, maxDepth): 

    # Depth limited search for IDS

    stack = util.Stack()
    visited = [problem.getStartState()]
    parent = {}
    source = problem.getStartState()
    sourceTuple = (problem.getStartState(), 0)
    stack.push(sourceTuple)

    while not stack.isEmpty():
        top, currentDepth = stack.pop()
        visited.append(top)

        if problem.isGoalState(top):
            return (True, parent, top)


        if currentDepth<maxDepth:
            neighbours = problem.getSuccessors(top)

            for adjacent in neighbours:
                vertex = adjacent[0]
                nextStep = adjacent[1]

                if vertex not in visited:
                    stack.push((vertex, currentDepth+1))
                    parent[vertex] = (top, nextStep)

    return (False, parent, source)


def iterativeDeepeningSearch(problem):

    depthLimit = 0;

    solutionFound = False

    while solutionFound is False:
        
        flag, parent, destination = depthLimitedSearch(problem, depthLimit)
        
        solutionFound = flag
        
        depthLimit = depthLimit + 1
    

    return generatePath(problem.getStartState(), destination, parent)

    util.raiseNotDefined()




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    source = problem.getStartState()
    priorityQueue = util.PriorityQueue()
    parent = {}
    visited = {}

    parent[source] = (source, [])
    visited[source] = 1
    priorityQueue.push(source, 0+heuristic(source, problem));

    while not priorityQueue.isEmpty():
        top = priorityQueue.pop()

        if problem.isGoalState(top):
            destination = top
            break;

        neighbours = problem.getSuccessors(top)

        for adjacent in neighbours:
            vertex = adjacent[0]
            nextStep = adjacent[1]
            cost = adjacent[2]

            if vertex not in visited.keys():
                visited[vertex] = visited[top] + cost
                priorityQueue.push(vertex, visited[vertex] + heuristic(vertex, problem))
                parent[vertex] = (top, nextStep)

            elif visited[top] + cost < visited[vertex]:
                visited[vertex] = visited[top] + cost
                priorityQueue.push(vertex, visited[vertex] + heuristic(vertex, problem))
                parent[vertex] = (top, nextStep)

    return generatePath(source, destination, parent)


    util.raiseNotDefined()


def bestFirstSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    source = problem.getStartState()
    priorityQueue = util.PriorityQueue()
    parent = {}
    visited = {}

    parent[source] = (source, [])
    visited[source] = 1
    priorityQueue.push(source, heuristic(source, problem));

    while not priorityQueue.isEmpty():
        top = priorityQueue.pop()

        if problem.isGoalState(top):
            destination = top
            break;

        neighbours = problem.getSuccessors(top)

        for adjacent in neighbours:
            vertex = adjacent[0]
            nextStep = adjacent[1]

            if vertex not in visited.keys():
                visited[vertex] = heuristic(vertex, problem)
                priorityQueue.push(vertex, visited[vertex])
                parent[vertex] = (top, nextStep)

    return generatePath(source, destination, parent)


    util.raiseNotDefined()




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
