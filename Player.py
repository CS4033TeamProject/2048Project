from EnviromentManager import *

class Agent:
    def __init__(self, url: str) -> None:
        self.env = EnviromentManager(url)
    
    def action(self, action: str) -> None:
        self.env.action(action)
    
    def state(self) -> dict:
        print(self.env.stateCounter)
        print(self.env.state())
        while True:
            # If the state has changed
            if self.env.state()[1]:
                # Returns new state
                return self.env.state()[0]
    
    # Temp function
    def getAction(self, grid: list) -> str:
        return input(">> ")
    
    def run(self) -> None:
        over = False
        won = False

        while not over or not won:
            newState = self.state() # Returns whole grid obj remember!!!
            a = self.getAction(newState)
            self.action(a)

            over = newState["over"]
            won = newState["won"]

if __name__ == "__main__":
    bigbrain = Agent("http://127.0.0.1:5000")
    bigbrain.run()