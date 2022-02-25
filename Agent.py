from EnviromentManager import *

class Agent:
    def __init__(self, url: str) -> None:
        self.env = EnviromentManager(url)
    
    def action(self, action: str) -> None:
        self.env.action(action)
    
    def state(self) -> dict:
        while True:
            # If the state has changed
            if self.env.state()[1]:
                # Returns new state
                return self.env.state()[0]
    
    # Temp function
    def GET_NEXT_ACTION_OR_SOMETHING(self, grid: list) -> str:
        return "left"
    
    def run(self) -> None:
        over = False
        won = False

        while not over or not won:
            newState = self.state() # Returns whole grid obj remember!!!
            a = self.GET_NEXT_ACTION_OR_SOMETHING(newState["grid"])
            self.action(a)

            over = newState["over"]
            won = newState["won"]

if __name__ == "__main__":
    bigbrain = Agent("127.0.0.1:5000")
    bigbrain.run()