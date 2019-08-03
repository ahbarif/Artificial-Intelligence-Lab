# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.actions = util.Counter()
        
        for loop in range(0, iterations):
            temp_values = util.Counter()
            temp_actions = util.Counter()

            for state in self.mdp.getStates():

                if self.mdp.isTerminal(state) == True: continue
                
                actionList = mdp.getPossibleActions(state)

                if len(actionList) == 0: continue

                ret = self.getQValue(state, actionList[0])
                optimal_action = actionList[0]

                for action in actionList:
                    val = self.getQValue(state, action)
                    if val > ret:
                      ret = val
                      optimal_action = action
                temp_values[state] = ret                 
                temp_actions[state] = optimal_action
                
            self.values = temp_values     
            self.actions = temp_actions


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
   

        qValue = 0
        transitionList = self.mdp.getTransitionStatesAndProbs(state, action);
        for transition in transitionList:

            probability = transition[1]
            reward = self.mdp.getReward(state, action, transition[0]);
            utility = self.getValue(transition[0])
            var = reward + self.discount * probability * utility;
            qValue += var
        return qValue


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        if state in self.actions.keys():
          return self.actions[state]
        else: return None

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
