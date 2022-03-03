import Policy

class State:
    def __init__(self, grid, previousState = None, terminal = False) -> None:
        self.grid = grid
        #[action, Action value, set of possible next states]
        self.actions = [
            [   "up", 0, [] ],
            [ "down", 0, [] ],
            [ "left", 0, [] ],
            ["right", 0, [] ]]
        self.value = 0
        self.previousState = previousState
        self.terminal = terminal
        self.start = True
    def __hash__(self) -> int:
        ##No two states have same grid, so grid should work for hash
        return hash(self.grid)

    def __eq__(self, other) -> bool:
        return self.grid == other.grid

    def getNextStates(self, action):
        for entry in self.actions:
            if entry[0] == action: return entry[2]

    #Sets the next state the action leads to
    def addNextState(self, action, nextState):
        for entry in self.actions:
            if entry[0] == action: entry[2].append(nextState)
    
    #Expected return when starting in state and following policy thereafter  
    def getActionValue(self, action):
        for entry in self.actions:
            if entry[0] == action: return entry[1]

    def setActionValue(self, action, value) -> float:
        for entry in self.actions:
            if entry[0] == action: entry[1] = value
    