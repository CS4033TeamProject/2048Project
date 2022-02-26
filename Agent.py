from os import times_result
import selenium
import random
from BrowserInterface import Interface

class MonteCarlo:
    def __init__(self, url: str, size: int, win: int) -> None:
        self.interface = Interface(url, size, win)
        self.states = []
        self.policy = {
            [
                [2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ] : [
                    ("up", 0.25),
                    ("down", 0.25),
                    ("left", 0.25),
                    ("right", 0.25)
            ]
        }
        self.lastScore = 0
    
    def restart(self) -> None:
        self.interface.restart()
    
    def action(self, direction: str) -> None:
        self.interface.move(direction)
    
    def state(self) -> list:
        return self.interface.data()
    
    def reward(self, currentScore: int) -> int:
        return currentScore - self.lastScore
    
    def run_episode(self) -> list:
        self.restart()
        
        # Episode will hold each time step: [[state, action, reward], [...]]
        episode = []
        
        while not self.interface.lost():
            state = self.interface.grid()

            # Time step will hold [state, action, reward]
            timeStep = []
            timeStep.append(state)

            # Generate random iid probabiity
            n = random.uniform(0, 1)

            # Make sure state is in policy
            # If not then add to policy with default probs
            if not state in self.policy:
                self.policy[state] = [
                    ("up", 0.25),
                    ("down", 0.25),
                    ("left", 0.25),
                    ("right", 0.25)
                ]

            # Get the action base on random n
            top = 0
            for prob in self.policy[state]:
                # Add prob of action to top
                top += self.policy[state][prob][1] # This is accessing the prob in (action, 0.xx)

                if n < top: # If prob sum is more than n do that action
                    action = self.policy[state][prob][0] # This is accessing the action in (action, 0.xx)
                    break

            self.interface.move(action)

            timeStep.append(action)
            timeStep.append(self.reward(self.interface.score()))
            self.lastScore = self.interface.score()

            episode.append(timeStep)

            # self.interface.lost should be properly breaking while loop
        
        return episode

if __name__ == "__main__":
    FILE_URL = "file:///C:/Users/kylew/Documents/Code/Machine%20Learning/2048%20RL/2048-master/index.html"

    mc = MonteCarlo(FILE_URL, 4, 32)

    try:
        mc.run()
    except selenium.common.exceptions.NoSuchWindowException:
        print("Closed!")