from GameManager import GameManager
from Grid  import Grid
from Tile import Tile

class PythonInterface:
    def __init__(self, size: int, win: int) -> None:
        self.size = size
        self.win = win
        self.data = {}
        self.game = GameManager(self.size, self.win)
        self.getData()
    
    def move(self, direction: str) -> None:
        keymap = {
            "up": "0",
            "right": "1",
            "down": "2",
            "left": "3",
        }

        self.game.move(keymap[direction])
        self.getData()
    
    def restart(self) -> None:
        self.game.restart()
        self.getData()

    def getData(self) -> dict:
        tiles = []
        grid = self.game.grid
        for row in range(0, self.size):
            temp = []
            for column in range(0, self.size):
                # If tile object
                if grid.cells[column][row]:
                    temp.append(grid.cells[column][row].value)
                # If null
                else:
                    temp.append(0)
            tiles.append(tuple(temp))

        self.data["grid"] = tuple(tiles)
        self.data["over"] = self.game.over
        self.data["won"] = self.game.won
    
    def grid(self) -> tuple:
        return self.data["grid"]
    
    def score(self) -> int:
        return self.data["score"]
    
    def over(self) -> bool:
        return self.data["over"]
    
    def won(self) -> bool:
        grid = self.grid()
        for i in range(0, self.size):
            for j in range(0, self.size):
                if grid[i][j] == self.win:
                    return True
        
        return False

    def printToTerminal(self):
        for x in range(self.size):
            row = "["
            for y in range(self.size):
                if self.data["grid"][x][y] == None: row = row + "0 "
                else: row = row + str(self.data["grid"][x][y]) + " "
            row = row[:-1] + "]"
            print(row)

if __name__ == "__main__":
    interface = PythonInterface(3, 16)
    while(interface.over() == False):
        interface.printToTerminal()
        print("Enter move:")
        move = input()
        if move == 'quit': break
        if move == 'r': 
            interface.restart()
            continue
        interface.move(move)
        if interface.won() == True:
            print("You win!")
            break
    print("Game over!")
