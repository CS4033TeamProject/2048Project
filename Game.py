class Game:
    def __init__(self) -> None:
        self.state = {
                "grid": None,
                "score": None,
                "over": False,
                "won": False,
                "keepPlaying": True,
                "stateCounter" : 0
                }

        self.action = {
                "move": None,
                "actionCounter" : 0
                }
    
    def getState(self) -> dict:
        return self.state

    def getAction(self) -> dict:
        return self.action

    def setState(self, state: dict) -> None:
        self.state = state

    def setAction(self, action: dict) -> None:
        self.action = action