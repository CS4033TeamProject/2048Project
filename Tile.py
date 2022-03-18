class Tile():
    def __init__(self, position, value) -> None:
        self.x = position["x"]
        self.y = position["y"]
        self.value = value or 2
        self.previousPosition = None
        self.mergedFrom = None # Tracks tiles that merged together

    def savePosition(self):
        self.previousPosition = { "x": self.x, "y": self.y }

    def updatePosition(self, position):
        self.x = position["x"]
        self.y = position["y"]

    def serialize(self):
        return {
            "position" : { 
                "x": self.x,
                "y": self.y},
            "value": self.value}
