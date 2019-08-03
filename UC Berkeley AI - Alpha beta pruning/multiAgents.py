# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        MAXX = float("inf")

        closestFood = MAXX
        for food in newFood.asList():
            dis = manhattanDistance(newPos, food)
            closestFood = min(closestFood, dis)
        if closestFood == MAXX: closestFood = 0

        closestGhost = MAXX
        for ghost in newGhostStates:
            dis = manhattanDistance(newPos, ghost.getPosition())
            closestGhost = min(closestGhost, dis)
        if closestGhost == MAXX: closestGhost = 0

        remaining = len(newFood.asList())

        score = closestGhost - closestFood - remaining*10

        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):

    def getAction(self, gameState):

        def minimax(gameState, agentIndex, depth):
                if gameState.isWin() or gameState.isLose() or depth == self.depth + 1:
                    return self.evaluationFunction(gameState)

                if len(gameState.getLegalActions(agentIndex)) == 0:
                     return self.evaluationFunction(gameState)

                if agentIndex == 0: # it is max agent
                    best = -(float("inf"))
                    for action in gameState.getLegalActions(agentIndex):
                        temp = minimax(gameState.generateSuccessor(agentIndex, action), agentIndex + 1, depth)
                        if temp>best:
                            best = temp
                    return best

                else:   # min agent
                    newDepth = depth
                    newIndex = agentIndex + 1

                    if agentIndex == gameState.getNumAgents()-1:
                        newDepth += 1
                        newIndex = 0

                    best = float("inf")
                    for action in gameState.getLegalActions(agentIndex):
                        temp = minimax(gameState.generateSuccessor(agentIndex, action), newIndex, newDepth)
                        if temp < best:
                            best = temp
                    return best


        bestAction = Directions.STOP
        best = -(float("inf"))

        for action in gameState.getLegalActions(0):
            temp = minimax(gameState.generateSuccessor(0, action), 1, 1)
            if temp > best:
                best = temp
                bestAction = action
        return bestAction

class AlphaBetaAgent(MultiAgentSearchAgent):

    def getAction(self, gameState):

        def minimax(gameState, agentIndex, depth, alpha, beta):
                if gameState.isWin() or gameState.isLose() or depth == self.depth + 1:     # is terminal state
                    return self.evaluationFunction(gameState)

                if len(gameState.getLegalActions(agentIndex)) == 0:
                     return self.evaluationFunction(gameState)

                if agentIndex == 0:
                    best = -(float("inf"))
                    for action in gameState.getLegalActions(agentIndex):
                        temp = minimax(gameState.generateSuccessor(agentIndex, action), agentIndex + 1, depth, alpha, beta)
                        if temp>best:
                            best = temp

                        if best > alpha:
                            alpha = best

                        if beta < alpha:
                            break
                    return best

                else:
                    newDepth = depth
                    newIndex = agentIndex + 1

                    if agentIndex == gameState.getNumAgents()-1:   # go to new max layer
                        newDepth += 1
                        newIndex = 0

                    best = float("inf")
                    for action in gameState.getLegalActions(agentIndex):
                        temp = minimax(gameState.generateSuccessor(agentIndex, action), newIndex, newDepth, alpha, beta)
                        if temp < best:
                            best = temp

                        if best < beta:
                            beta = best

                        if beta < alpha:
                            break
                    return best

        bestAction = Directions.STOP
        best = -(float("inf"))

        alpha = -(float("inf"))
        beta = float("inf")

        for action in gameState.getLegalActions(0):
            temp = minimax(gameState.generateSuccessor(0, action), 1, 1, alpha, beta)
            if temp>best:
                best = temp
                bestAction = action

            if best > alpha:
                alpha = best

            if beta <= alpha:
                break

        return bestAction


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
