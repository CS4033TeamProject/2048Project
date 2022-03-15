from Tile import Tile
from Grid import Grid
import random
##"C:\\Users\\tyler\\OneDrive\\Documents\\OU\\Spring 2022\\Machine Learning\\2048Project\\2048-master\\js\\game_manager.js"

class GameManager():
    def __init__(self, size, InputManager, Actuator, StorageManager) -> None:
        self.size = size 
        #self.inputManager = InputManager
        #self.storageManager = StorageManager
        #self.actuator       = Actuator

        self.startTiles     = 2

        #self.inputManager.on("move", self.move.bind(self));
        #self.inputManager.on("restart", self.restart.bind(self));
        #self.inputManager.on("keepPlaying", self.keepPlaying.bind(self));

        self.setup()

    # Restart the game
    def restart(self):
        #self.storageManager.clearGameState()
        #self.actuator.continueGame() # Clear the game won/lost message
        self.setup()

    # Keep playing after winning (allows going over 2048)
    def keepPlaying(self):
        self.keepPlaying = True
        #self.actuator.continueGame() # Clear the game won/lost message

    # Return true if the game is lost, or has won and the user hasn't kept playing
    def isGameTerminated(self):
        return self.over or (self.won and not self.keepPlaying)

    # Set up the game
    def setup(self):
        #previousState = self.storageManager.getGameState()

        # Reload the game from a previous game if present
        # if (previousState):
        #     self.grid = Grid(previousState.grid.size, previousState.grid.cells) ## Reload grid
        #     self.score       = previousState.score
        #     self.over        = previousState.over
        #     self.won         = previousState.won
        #     self.keepPlaying = previousState.keepPlaying
        #else:
        self.grid        = Grid(self.size)
        self.score       = 0
        self.over        = False
        self.won         = False
        self.keepPlaying = False

        # Add the initial tiles
        self.addStartTiles()

        # Update the actuator
        #self.actuate()
        
    # Set up the initial tiles to start the game with
    def addStartTiles(self):
        for i in range(0, self.startTiles):
            self.addRandomTile()

    # Adds a tile in a random position
    def addRandomTile(self):
        if self.grid.cellsAvailable():
            value = 2 if random.random() < 0.9 else 4
            tile = Tile(self.grid.randomAvailableCell(), value)
            self.grid.insertTile(tile)

    # Sends the updated grid to the actuator
    def actuate(self):
        if self.storageManager.getBestScore() < self.score:
            self.storageManager.setBestScore(self.score)

    # Clear the state when the game is over (game over only, not win)
        if (self.over):
            self.storageManager.clearGameState()
        else: 
            self.storageManager.setGameState(self.serialize())


        self.actuator.actuate(
            self.grid, {
            "score":      self.score,
            "over":       self.over,
            "won":        self.won,
            "bestScore":  self.storageManager.getBestScore(),
            "terminated": self.isGameTerminated()
            })

    # Represent the current game as an object
    def serialize(self):
        return {
            "grid":        self.grid.serialize(),
            "score":       self.score,
            "over":        self.over,
            "won":         self.won,
            "keepPlaying": self.keepPlaying}

    # Save all tile positions and remove merger info
    def prepareTiles(self):
        def callback(x, y, tile):
            if tile:
                tile.mergedFrom = None
                tile.savePosition()
            
        self.grid.eachCell(callback)


    # Move a tile and its representation
    def moveTile(self, tile, cell):
        self.grid.cells[tile.x][tile.y] = None
        self.grid.cells[cell["x"]][cell["y"]] = tile
        tile.updatePosition(cell)

    # Move tiles on the grid in the specified direction
    def move(self, direction):
        # 0: up, 1: right, 2: down, 3: left
        if (self.isGameTerminated()): return; # Don't do anything if the game's over
        cell = None
        tile = None

        vector     = self.getVector(direction)
        traversals = self.buildTraversals(vector)
        moved      = False

        # Save the current tile positions and remove merger information
        self.prepareTiles()

        # Traverse the grid in the right direction and move tiles
        for x in traversals["x"]:
            for y in traversals["y"]:
                cell = { "x": x, "y": y }
                tile = self.grid.cellContent(cell)

                if (tile):
                    positions = self.findFarthestPosition(cell, vector)
                    next      = self.grid.cellContent(positions["next"])

                    # Only one merger per row traversal?
                    if (next and next.value == tile.value and not next.mergedFrom):
                        merged = Tile(positions["next"], tile.value * 2)
                        merged.mergedFrom = [tile, next]

                        self.grid.insertTile(merged)
                        self.grid.removeTile(tile)

                        # Converge the two tiles' positions
                        tile.updatePosition(positions["next"])

                        # Update the score
                        self.score += merged.value

                        # The mighty 2048 tile
                        if merged.value == 2048: self.won = True
                    else:
                        self.moveTile(tile, positions["farthest"])

                    if not self.positionsEqual(cell, tile): 
                        moved = True # The tile moved from its original cell!

        if moved:
            self.addRandomTile()

        if not self.movesAvailable():
            self.over = True # Game over!

        #self.actuate()

    # Get the vector representing the chosen direction
    def getVector(self, direction):
        # Vectors representing tile movement
        map = {
            "0": { "x": 0,  "y": -1 }, # Up
            "1": { "x": 1,  "y": 0 },  # Right
            "2": { "x": 0,  "y": 1 },  # Down
            "3": { "x": -1, "y": 0 }   # Left
        }
        return map[direction]

    # Build a list of positions to traverse in the right order
    def buildTraversals(self, vector):
        traversals = { "x": [], "y": [] }

        for pos in range(self.size):
            traversals["x"].append(pos)
            traversals["y"].append(pos)

        # Always traverse from the farthest cell in the chosen direction
        if (vector["x"] == 1): traversals["x"].reverse()
        if (vector["y"] == 1): traversals["y"].reverse()

        return traversals

    def findFarthestPosition(self, cell, vector):
        #previous

        # Progress towards the vector direction until an obstacle is found
        while True:
            previous = cell
            cell     = { "x": previous["x"] + vector["x"], "y": previous["y"] + vector["y"] }
            if not (self.grid.withinBounds(cell) and self.grid.cellAvailable(cell)): break

        return {
            "farthest": previous,
            "next": cell # Used to check if a merge is required
            }

    def movesAvailable(self):
        return self.grid.cellsAvailable() or self.tileMatchesAvailable()

    # Check for available matches between tiles (more expensive check)
    def tileMatchesAvailable(self):
        tile = None

        for x in range(self.size):
            for y in range (self.size):
                tile = self.grid.cellContent({ "x": x, "y": y })

        if (tile):
            for direction in range(0, 4): #var direction = 0; direction < 4; direction++) {
                vector = self.getVector(direction)
                cell   = { "x": x + vector["x"], "y": y + vector["y"] }

                other  = self.grid.cellContent(cell)

            if (other or other.value == tile.value):
                return True # These two tiles can be merged

        return False

    def positionsEqual(self, first, second):
        return first["x"] == second.x and first["y"] == second.y

if __name__ == "__main__":
    game = GameManager(3, None, None, None)
    while(game.over == False):
        game.grid.printToTerminal()
        print("Enter move:")
        move = input()
        game.move(move)
        
    print("Game over!")