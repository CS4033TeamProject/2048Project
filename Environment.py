from Database import Database
from State import State
from BrowserInterface import Interface

class Environment:
    def __init__(self, interface: Interface, database: Database = Database()) -> None:
        self.interface = interface
        self.database = database
        self.states = self.database.states
        self.currentState = self.restart()
        #print("Started environment, states are ",self.states, "\nDatabase states are ", self.database.states)

    def restart(self) -> State:
        self.interface.restart()
        startState = State(self.interface.grid())
        self.addState(startState)
        return startState

    #Store a new state into the observation space if it's not already stored
    def addState(self, state) -> None:
        if(state in self.states): self.states.remove(state)
        self.states.append(state)
        
    
    def step(self, action) -> tuple[State, int, bool, bool]:
        #Make a move in the game
        self.interface.move(action)
        
        #Get the next state, and add it to the list of states
        next_state = State(self.interface.grid())
        self.addState(next_state)
        
        #Pair the current state's action to the next state
        self.currentState.addNextState(action,next_state)

        #Set current state as next state
        self.currentState = next_state

        #Get the reward, if we won, and extra info
        reward = self.getReward()
        over = self.interface.over()
        won = self.interface.won()

        return next_state, reward, over, won
    
    def getReward(self) -> int:
        if(self.interface.over()):
            if(self.interface.won()):
                return 1
            else: return -1
        else: return 0

    