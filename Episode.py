class Episode:
    def __init__(self, environment, policy) -> None:
        #move = (state, action, reward)
        self.moves = []
        self.reward = 0
        self.win = False
        self.policy = policy

    def run_episode(self, environment):
        done = False
        state = environment.restart()
        while(not done):
            action = self.policy.getAction(state)
            self.moves.append([state, action])
            results = environment.step(action)
            state = results[0]
            self.reward += results[1]
            done = results[2]
            self.win = results[3]
            if self.win: done = True
