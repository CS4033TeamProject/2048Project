import matplotlib.pyplot as plt
import numpy as np

from Database import Database

def plotWins(database: Database):
    x = range(1, len(database.episodes) + 1)
    y = [episode.win for episode in database.episodes]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
plotWins(Database.load_db())