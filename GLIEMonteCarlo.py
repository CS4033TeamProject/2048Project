from sre_parse import State
from Database import Database
from Policy import Policy
from Episode import Episode
from Environment import Environment
from State import State
import random

class GLIEMonteCarlo:
    def __init__(self, environment: Environment, database: Database, policy: Policy, iterations = 10000) -> None:
        ##state-action values are 0
        ##state-action times visited are 0
        self.environment = environment
        self.database = database
        self.policy = policy
        self.iterations = iterations
        self.episodes = 0
        self.epsilon = 1
        self.wins = 0

        while(self.episodes < self.iterations):
            episode = Episode(self.environment, self.policy)
            self.update(episode)
            self.episodes += 1
            self.epsilon = 1/self.episodes
            self.policy.epsilon = self.epsilon
            if episode.win: self.wins+=1
            print("Win percent: ", self.wins/self.episodes)

    ##TODO: Store N and Q within state, reduce the loops
    def update(self, episode: Episode):
        for move in episode.moves:
            state = move[0]
            action = move[1]
            q = state.getActionValue(action)
            n = state.getTimesVisited(action)
            q = q + 1/n * (episode.reward - q)
            state.setActionValue(action, q)
    
