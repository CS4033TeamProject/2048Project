import selenium
from BrowserInterface import Interface

class MonteCarlo:
    def __init__(self, url: str, size: int) -> None:
        self.interface = Interface(url, size)
        self.states = []
    
    def restart(self) -> None:
        self.interface.restart()
    
    def action(self, direction: str) -> None:
        self.interface.move(direction)
    
    def state(self) -> list:
        self.states.append(self.interface.grid())
        return self.interface.grid()
    
    def run(self) -> None:
        return

if __name__ == "__main__":
    FILE_URL = "file:///C:/Users/kylew/Documents/Code/Machine%20Learning/2048%20RL/2048-master/index.html"

    mc = MonteCarlo(FILE_URL, 4)

    try:
        mc.run()
    except selenium.common.exceptions.NoSuchWindowException:
        print("Closed!")