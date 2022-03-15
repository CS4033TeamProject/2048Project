from h11 import Data
import matplotlib.pyplot as plt
import numpy as np

from Database import Database

def plotWins(database: Database):
    x = range(1, len(database.episodes) + 1)
    y = []
    episodes = 0
    wins = 0
    for episode in database.episodes:
        episodes += 1 
        if episode.win : wins += 1
        win_rate = wins/episodes
        y.append(win_rate)
    #y = [episode.win for episode in database.episodes]
    print("Win rate = ", sum(y)/len(database.episodes))
    print("Last 1000 win rate = ", sum(y[-1000:])/1000)
    print("Last 100 win rate = ", sum(y[-100:])/100)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


def printActionValues(database: Database):
    for state in database.states.values():
        for action in state.actions:
            if action[1] != 0: print(action[1])

if __name__ == "__main__":
    database = Database.load_db("TD_Database.pickle")
    plotWins(database=database)
    #printActionValues(database=database)