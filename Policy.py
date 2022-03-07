from cmath import inf
import random


class Policy:
    def __init__(self, epsilon = 1) -> None:
        self.epsilon = epsilon

    def getAction(self, state):
        #Probability 1-e select greedy action
        if((random.random()-self.epsilon) > 0):
            return self.selectGreedy(state)
        else:
            return self.selectRandom(state)
            
    def selectRandom(self, state):
        move = random.choice(state.getAvailableActions())
        return move

    def selectGreedy(self, state):
        action_values = state.getActionValues()
        max_value = max(action_values)
        index = random.choice([i for i in range(len(action_values)) if action_values[i] == max_value])
        move = (state.getAvailableActions()[index])
        return move