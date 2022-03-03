class Database:
    def __init__(self, FILE_URL = 'database.json') -> None:
        self.states = []
        self.FILE_URL = FILE_URL
    
        #Store a new state into the database if it's not already stored
    def addState(self, new_state) -> None:
        new_entry = True
        for state in self.states:
            if new_state == state:
                new_entry = False
                new_state = state
                break
        if new_entry: self.states.append(new_state)
        return new_state

    def win_percentage(self, number_of_episodes: int) -> float:
        wins = 0

        for i in range(0, number_of_episodes):
            if self.run_episode()[1]:
                wins += 1
        
        return wins / number_of_episodes