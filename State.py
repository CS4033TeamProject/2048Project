import Policy

class State:
    def __init__(self, grid, previousState = None, terminal = False) -> None:
        self.grid = tuple(tuple(sub) for sub in grid)
        #[Action value, set of possible next states]
        self.actions = {
            "up"    : [0, [] ],
            "down"  : [0, [] ],
            "left"  : [0, [] ],
            "right" : [0, [] ]}
        self.value = 0
        self.previousState = previousState
        self.terminal = terminal
        self.start = True
    def __hash__(self) -> int:
        ##No two states have same grid, so grid should work for hash
        return hash(self.grid)

    def __eq__(self, other) -> bool:
        return self.grid == other.grid

    #Sets the next state the action leads to
    def addNextState(self, action, nextState):
        self.actions[action][1].append(nextState)
    
    def getNextStates(self, action):
        return self.actions[action][1]

    #Expected return when starting in state and following policy thereafter
    #@property
    #def value(self) -> float:
    #    return self.value
    
    @property
    def action_values(self):
        action_values = []
        for action in self.actions:
            action_values.append(self.actions[action][0])
        return action_values

    @action_values.setter
    def setActionValue(self, action_values, value) -> float:
        for action in action_values:
            self.actions[action][0] = value
    