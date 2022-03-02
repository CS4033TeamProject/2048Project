from Database import Database
from Policy import Policy
from Episode import Episode
from Environment import Environment
import random

class GLIEMonteCarlo:
    def __init__(self, environment: Environment, policy: Policy, database: Database, iterations = 10000) -> None:
        ##state-action values are 0
        ##state-action times visited are 0
        self.environment = environment
        self.database = database
        self.iterations = iterations
        self.episodes = 0
        self.epsilon = 1
        self.Q_N = []
        self.policy = Policy(self.database.states, self.epsilon)
        self.winRate = 0
        self.wins = 0
        e = 0
        w = 0
        while(self.episodes < self.iterations):
            episode = Episode(self.environment, self.policy)
            self.update
            self.episodes += 1
            self.epsilon = 1/self.episodes
            self.policy.epsilon = self.epsilon
            if episode.win: w += 1
            e += 1
            if e == 10:
                print("Last 10 Winrate: ", w/e)
                w = 0
                e = 0
    ##TODO: Store N and Q within state, reduce the loops
    def update(self, episode: Episode):
        for move in episode.moves:
            state = move[0]
            action = move[1]
            state_action = [state, action]
            new_entry = True
            for entry in self.Q_N:
                if state_action == entry[0]:
                    new_entry = False
                    n = entry[1][0]
                    q = entry[1][1]
                    n += 1
                    q = q + 1/n * (episode.reward - q)
                    entry[1][0] = n
                    entry[1][1] = q
            if new_entry: 
                n = 1
                q = episode.reward
                self.N.append([state_action,[n,q]])
        #Update actionvalue in policy state with Q
            state_policy = self.policy.policyMap[state]
            for policy in state_policy:
                if policy[0] == action: policy[1] += q
    
