class Database:
    def __init__(self, FILE_URL = 'database.json') -> None:
        self.states = dict()
        self.FILE_URL = FILE_URL
    
        #Store a new state into the database if it's not already stored
    def addState(self, new_state) -> None:
        #If new state is already in dictionary, assign it to new_state
        if new_state in self.states: new_state = self.states[new_state]
        #Else add new state to dictionary
        else: self.states[new_state] = new_state
        return new_state
    
    def getState(self, state):
        return self.states[state]
        
    def win_percentage(self, number_of_episodes: int) -> float:
        wins = 0

        for i in range(0, number_of_episodes):
            if self.run_episode()[1]:
                wins += 1
        
        return wins / number_of_episodes