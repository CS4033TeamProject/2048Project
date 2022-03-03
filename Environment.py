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
        startState = self.database.addState(State(self.interface.grid()))
        return startState        
    
    def step(self, action) -> tuple[State, int, bool, bool]:
        #Make a move in the game
        self.interface.move(action)
        
        #Get the next state, and add it to the database of states
        next_state = self.database.addState(State(self.interface.grid()))
        
        #Add to the current state's action the next state
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

    