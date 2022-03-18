import matplotlib.pyplot as plt
import numpy as np

from Database import Database

def plotWins(databases, random = None, td = None, mc = None):
    
    plot = 0
    colors = ['magenta','orange','green','crimson','purple','brown','pink','gray','olive','cyan', 'yellow']
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
    
    plot += 1
    if random:
        x = range(1, len(random.episodes) + 1)
        y = []
        episodes = 0
        wins = 0
        for episode in random.episodes:
            episodes += 1 
            if episode.win : wins += 1
            win_rate = wins/episodes
            y.append(win_rate)
        ax.plot(x, y, color = 'black', label = 'Random')
    
    if td:
        x = range(1, len(td.episodes) + 1)
        y = []
        episodes = 0
        wins = 0
        for episode in td.episodes:
            episodes += 1 
            if episode.win : wins += 1
            win_rate = wins/episodes
            y.append(win_rate)
        ax.plot(x, y, color = 'red', label = 'Temporal Difference')
    
    if mc:
        x = range(1, len(mc.episodes) + 1)
        y = []
        episodes = 0
        wins = 0
        for episode in mc.episodes:
            episodes += 1 
            if episode.win : wins += 1
            win_rate = wins/episodes
            y.append(win_rate)
        ax.plot(x, y, color = 'blue', label = 'Monte Carlo')

    ax.legend(loc = 'upper right')
    plt.xlim(0,100000)
    plt.show()


def printActionValues(database: Database):
    for state in database.states.values():
        for action in state.actions:
            if action[1] != 0: print(action[1])

if __name__ == "__main__":
    td = Database.load_db("TD_Database_alpha_0.05_discount_0.00_size_2_win_16.pickle")
    database1 = Database.load_db("TD_Database_alpha_0.05_discount_0.10_size_2_win_16.pickle")
    database2 = Database.load_db("TD_Database_alpha_0.05_discount_0.20_size_2_win_16.pickle")
    database3 = Database.load_db("TD_Database_alpha_0.05_discount_0.30_size_2_win_16.pickle")
    database4 = Database.load_db("TD_Database_alpha_0.05_discount_0.40_size_2_win_16.pickle")
    database5 = Database.load_db("TD_Database_alpha_0.05_discount_0.50_size_2_win_16.pickle")
    database6 = Database.load_db("TD_Database_alpha_0.05_discount_0.60_size_2_win_16.pickle")
    database7 = Database.load_db("TD_Database_alpha_0.05_discount_0.70_size_2_win_16.pickle")
    database8 = Database.load_db("TD_Database_alpha_0.05_discount_0.80_size_2_win_16.pickle")
    database9 = Database.load_db("TD_Database_alpha_0.05_discount_0.90_size_2_win_16.pickle")
    mc = Database.load_db("TD_Database_alpha_0.05_discount_1.00_size_2_win_16.pickle")
    #database10 = Database.load_db("negative10reward.pickle")
    random = Database.load_db("random_agent_size_2_win_16.pickle")
    dbs = [database1,database2,database3,database4,database5,database6,database7,database8, database9]
    #db = Database.load_db("TD_Database_alpha_0.2_discount_0.5.pickle")
    plotWins(dbs, random, td, mc)
    #printActionValues(database=database)