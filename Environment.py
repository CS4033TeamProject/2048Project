from Database import Database
from State import State

class Environment:
    def __init__(self, interface, database) -> None:
        self.interface = interface
        self.database = database
        self.currentState = self.restart()
        #print("Started environment, states are ",self.states, "\nDatabase states are ", self.database.states)

    def restart(self) -> State:
        self.interface.restart()
        startState = self.database.addState(State(self.interface.grid(), start=True))
        self.currentState = startState
        return startState        
    
    def step(self, policy) -> tuple:
        moved = False
        while not moved:
            #Get action from policy
            action = policy.getAction(self.currentState)
            #Make a move in the game
            self.interface.move(action)
            #Get the next state, and add it to the database of states
            next_state = self.database.addState(State(self.interface.grid()))
            #Add to the current state's action the next state
            moved = self.currentState.addNextState(action,next_state)
            #If we didnt move, repeat with invalid move removed

        #Get the reward, if we won, and extra info
        reward = self.getReward()
        over = self.interface.over()
        won = self.interface.won()

        #Increment state action times visited
        self.currentState.incrementTimesVisited(action)

        #Set current state as next state
        self.currentState = next_state
        #Set state as terminal if done
        if(over or won): self.currentState.terminal = True

        return next_state, action, reward, over, won
    
    def getReward(self) -> int:
        if(self.interface.over()):
            if(self.interface.won()):
                return 1
            else: return -1
        else: return 0

    