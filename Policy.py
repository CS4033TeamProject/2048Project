from cmath import inf
from os import stat_result
import random
import copy

class Policy:
    def __init__(self, states, epsilon = 1) -> None:
        self.states = states
        self.epsilon = epsilon

    def getAction(self, state):
        #Probability 1-e select greedy action
        if((random.random()-self.epsilon) > 0):
            return self.selectGreedy(state)
        else:
            return self.selectRandom(state)
            
    def selectRandom(self, state):
        move = random.choice(state.actions)[0]
        return move

    def selectGreedy(self, state):
        maximum = -inf
        for action in state.actions:
            maximum = max(maximum,action[1])
            if maximum == action[1]: move = action[0]
        return move

    def export_policy(self) -> None:
        f = open("policy.log", "w")
        f.write(str(self.policyMap))
        f.close