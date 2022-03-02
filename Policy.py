from cmath import inf
from os import stat_result
import random
import copy

class Policy:
    def __init__(self, states, epsilon = 1) -> None:
        self.states = states
        #[Action, Action-Value]
        self.uniform = [
            ["up",0],
            ["down",0],
            ["left",0],
            ["right",0]]
        self.policyMap = self.mapPolicyToStates(self.states, self.uniform)
        self.epsilon = epsilon
    ##TODO Fix policy updates, reduce loops
    def mapPolicyToStates(self, states, policy) -> dict:
        return dict.fromkeys(states, copy.deepcopy(policy))

    def getAction(self, state):
        self.policyMap = self.mapPolicyToStates(self.states, self.uniform)
        #Probability 1-e select greedy action
        if((random.random()-self.epsilon) > 0):
            return self.selectGreedy(state)
        else:
            return self.selectRandom(state)
            

    def selectRandom(self, state):
        move = random.choice(self.policyMap[state])[0]
        return move

    def selectGreedy(self, state):
        maximum = -inf
        for action in self.policyMap[state]:
            maximum = max(maximum,action[1])
            if maximum == action[1]: move = action[0]
        return move
    #Expected return when starting in state and following policy thereafter
    #
    #bellman equation for value function=(sum of policy(action|state) for all actions) * (sum of (probability of (s',r|s,a)) * (reward + gamma*value function of s')
    def stateValue(self, state) -> float:
        return self.value
    
    #Expected return starting from state, taking action, and thereafter following policy
    def actionValue(self, state, action) -> float:
        return self.value
    
    
    #Perform an expected update on all states to calculate policy value pg 74
    def interativePolicyEvaluation(policy) -> None:
        #Expected update
        #Loop
            #Delta = 0
            #Loop for each state s in S
                #v = Value(state)
                #Value(state) = Expected update
                #delta = max(delta,|v - Value(state))
            #until delta < theta-determines accuracy of estimation
        pass

    def export_policy(self) -> None:
        f = open("policy.log", "w")
        f.write(str(self.policyMap))
        f.close