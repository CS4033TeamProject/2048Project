import matplotlib.pyplot as plt
import numpy as np

from Database import Database

def plotDatabase(database, label):
    x = range(1, len(database.episodes) + 1)
    y = []
    episodes = 0
    wins = 0
    for episode in database.episodes:
        episodes += 1 
        if episode.win : wins += 1
        win_rate = wins/episodes
        y.append(win_rate)
    plt.plot(x, y, label = database.FILE_URL)

def plotWins(databases, limit):
    plot = 0
    for database in databases:
        plotDatabase(database, str(plot))
        plot += 1
    plt.legend(loc = 'upper right')
    plt.xlim(0,limit)
    plt.show()

def printActionValues(database: Database):
    for state in database.states.values():
        for action in state.actions:
            if action[1] != 0: print(action[1])

if __name__ == "__main__":
    dbs = []
    dbs.append(Database.load_db("TD_Database_alpha_0.005_discount_0.000_size_2_win_16.pickle"))
    dbs.append(Database.load_db("TD_Database_alpha_0.005_discount_1.000_size_2_win_16.pickle"))
    dbs.append(Database.load_db("random_agent_size_2_win_16.pickle"))
    xlim = 10000
    plotWins(dbs, xlim)
