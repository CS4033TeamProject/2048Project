from Database import Database
from Policy import Policy
from Episode import Episode
from Environment import Environment
import random

class GLIEMonteCarlo:
    def __init__(self, environment: Environment, policy: Policy, database: Database, iterations = 1000) -> None:
        ##state-action values are 0
        ##state-action times visited are 0
        self.environment = environment
        self.database = database
        self.iterations = iterations
        self.episodes = 0
        self.epsilon = 1
        self.Q = None
        self.N = None
        self.policy = Policy(self.database.states, self.epsilon)

        while(self.episodes < self.iterations):
            episode = Episode(environment, policy)
            self.Q = self.updateQ(episode)
            self.episodes += 1
            self.epsilon = 1/self.episodes
            policy = Policy(environment.states, self.epsilon)

    def updateQ(self, episode):
        for move in episode.moves:
            state = move[0]
            action = move[1]
            self.N[state][action] += 1
            self.Q[state][action] = self.Q[state][action] + 1/self.N[state][action] * (episode.reward - self.Q[state][action])
    
