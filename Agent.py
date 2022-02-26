import selenium
from BrowserInterface import Interface

class MonteCarlo:
    def __init__(self, url: str, size: int) -> None:
        self.interface = Interface(url, size)
        self.states = []
        self.policy = {
            [
                [2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ] : {
                "up": 0.25,
                "down": 0.25,
                "left": 0.25,
                "right": 0.25
            }
        }
    
    def restart(self) -> None:
        self.interface.restart()
    
    def action(self, direction: str) -> None:
        self.interface.move(direction)
    
    def state(self) -> list:
        return self.interface.data()
    
    def run_episode(self) -> list:
        self.restart()
        episode = []
        
        while not self.interface.lost():
            state = self.interface.grid()

            timeStep = []
            timeStep.append(state)
        
        return episode



        

if __name__ == "__main__":
    FILE_URL = "file:///C:/Users/kylew/Documents/Code/Machine%20Learning/2048%20RL/2048-master/index.html"

    mc = MonteCarlo(FILE_URL, 4)

    try:
        mc.run()
    except selenium.common.exceptions.NoSuchWindowException:
        print("Closed!")