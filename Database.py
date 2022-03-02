class Database:
    def __init__(self, FILE_URL = 'database.json') -> None:
        self.states = []
        self.FILE_URL = FILE_URL
    def win_percentage(self, number_of_episodes: int) -> float:
        wins = 0

        for i in range(0, number_of_episodes):
            if self.run_episode()[1]:
                wins += 1
        
        return wins / number_of_episodes