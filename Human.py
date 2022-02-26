from BrowserInterface import Interface

import time

class Human:
    def __init__(self, url: str) -> None:
        self.interface = Interface(url)
    
    def action(self, direction):
        self.interface.move(direction)

if __name__ == "__main__":
    gigaChad = Human("file:///C:/Users/kylew/Documents/Code/Machine%20Learning/2048%20RL/2048-master/index.html")
    
    while True:
        gigaChad.action("up")
        gigaChad.action("down")
        gigaChad.action("up")
        gigaChad.action("down")