from Policy import Policy
from State import State
from Environment import Environment

class Episode:
    def __init__(self, environment: Environment, policy: Policy) -> None:
        #move = (state, action, reward)
        self.moves = []
        self.reward = 0
        self.win = False
        self.policy = policy
        self.environment = environment
        self.run_episode()
        print("Episode Done")

    def run_episode(self):
        done = False
        state = self.environment.restart()
        while(not done):
            move = self.environment.step(self.policy.getMove(state))
            self.moves.append(move)
            state = move[0]
            self.reward += move[1]
            done = move[2]
            self.win = move[3]
