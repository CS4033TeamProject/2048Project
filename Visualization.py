import matplotlib.pyplot as plt
import numpy as np

from Database import Database

def plotWins(database: Database):
    x = range(1, len(database.episodes) + 1)
    y = [episode.win for episode in database.episodes]
    print("Win rate = ", sum(y)/len(database.episodes))
    print("Last 1000 win rate = ", sum(y[-1000:])/1000)
    print("Last 100 win rate = ", sum(y[-100:])/100)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
plotWins(Database.load_db())