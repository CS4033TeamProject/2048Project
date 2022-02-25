class Game:
    def __init__(self) -> None:
        self.grid = {
                "grid": None,
                "score": None,
                "over": False,
                "won": False,
                "keepPlaying": True,
                "gridCounter" : 0
                }

        self.move = {
                "move": None,
                "moveNumber" : 0
                }
    
    def getGrid(self) -> dict:
        return self.grid

    def getMove(self) -> dict:
        return self.move

    def setGrid(self, grid: dict) -> None:
        self.grid = grid

    def setMove(self, move: dict) -> None:
        self.move = move