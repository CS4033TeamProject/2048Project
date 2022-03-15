from h11 import Data
import matplotlib.pyplot as plt
import numpy as np

from Database import Database

def plotWins(databases):
    
    plot = 0
    colors = ['red', 'green', 'blue', 'purple']
    fig, ax = plt.subplots()
    
    for database in databases:
        plot += 1
        x = range(1, len(database.episodes) + 1)
        y = []
        episodes = 0
        wins = 0
        for episode in database.episodes:
            episodes += 1 
            if episode.win : wins += 1
            win_rate = wins/episodes
            y.append(win_rate)
        
        ax.plot(x, y, color = colors[plot], label = str(plot))
    ax.legend(loc = 'upper right')
    plt.show()


def printActionValues(database: Database):
    for state in database.states.values():
        for action in state.actions:
            if action[1] != 0: print(action[1])

if __name__ == "__main__":
    database1 = Database.load_db("TD_Database_alpha_0.1_discount_0.1.pickle")
    database2 = Database.load_db("TD_Database_alpha_0.1_discount_0.2.pickle")
    plotWins([database1,database2])
    #printActionValues(database=database)