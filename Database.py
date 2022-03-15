import pickle

class Database:
    def __init__(self, FILE_URL = 'database.pickle') -> None:
        self.states = dict()
        self.episodes = []
        self.FILE_URL = FILE_URL
    
        #Store a new state into the database if it's not already stored
    def addState(self, new_state) -> None:
        #If new state is already in dictionary, assign it to new_state
        if new_state in self.states: new_state = self.states[new_state]
        #Else add new state to dictionary
        else: self.states[new_state] = new_state
        return new_state
    
    def addEpisode(self, new_episode) -> None:
        self.episodes.append(new_episode)
        return new_episode

    def getState(self, state):
        return self.states[state]
        
    def win_percentage(self) -> float:
        wins = 0

        for episode in self.episodes:
            if episode.win():
                wins += 1
        
        return wins / len(self.episodes)

    def save_db(self):
        try:
            with open(self.FILE_URL, "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)


    def load_db(FILE_URL = 'database.pickle'):

        try:
            with open(FILE_URL, "rb") as f:
                return pickle.load(f)
        except IOError:
            print("Database file not found, creating new database")
            return Database(FILE_URL)
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)
    