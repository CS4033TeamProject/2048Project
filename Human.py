import selenium
from BrowserInterface import Interface

import time

class Human:
    def __init__(self, url: str, size: int) -> None:
        self.interface = Interface(url, size)
    
    def restart(self) -> None:
        self.interface.restart()
    
    def action(self, direction: str) -> None:
        self.interface.move(direction)
    
    def state(self) -> list:
        return self.interface.grid()

if __name__ == "__main__":
    try:
        gigaChad = Human("file:///C:/Users/kylew/Documents/Code/Machine%20Learning/2048%20RL/2048-master/index.html", 4)
        
        while True:
            for i in range(0, 4):
                gigaChad.action("up")
                gigaChad.action("down")
                gigaChad.action("up")
                gigaChad.action("down")
                print(gigaChad.state())
            
            gigaChad.restart()

            for i in range(0, 4):
                gigaChad.action("up")
                gigaChad.action("down")
                gigaChad.action("up")
                gigaChad.action("down")
                print(gigaChad.state())

    except selenium.common.exceptions.NoSuchWindowException:
        print("Closed!")
        