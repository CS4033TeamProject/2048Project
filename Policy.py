from os import stat_result
import random

class Policy:
    def __init__(self, states, epsilon = 1) -> None:
        self.states = states
        self.uniform = [
            ["up",.25],
            ["down",.25],
            ["left",.25],
            ["right",.25]]
        self.policyMap = self.mapPolicyToStates(self.states, self.uniform)
        self.epsilon = epsilon
    
    def mapPolicyToStates(self, states, policy) -> dict:
        return dict.fromkeys(states, policy)

    def getMove(self, state):
        self.policyMap = self.mapPolicyToStates(self.states, self.uniform)
        #Probability 1-e select greedy action
        if((random.random()-self.epsilon) > 0):
            return self.selectGreedy(state)
        else:
            return self.selectRandom(state)

    def selectRandom(self, state):
        print("Selecting from ", self.policyMap[state])
        move = random.choice(self.policyMap[state])[0]
        return move

    def selectGreedy(self, state):
        return max(self.policyMap[state][1])[0]
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