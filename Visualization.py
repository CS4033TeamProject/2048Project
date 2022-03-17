import matplotlib.pyplot as plt
import numpy as np

from Database import Database

def plotWins(databases, random):
    
    plot = 0
    colors = ['blue','orange','green','red','purple','brown','pink','gray','olive','cyan', 'yellow']
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
    ax.legend(loc = 'upper right')
    plt.xlim(0,1000)
    plt.show()


def printActionValues(database: Database):
    for state in database.states.values():
        for action in state.actions:
            if action[1] != 0: print(action[1])

if __name__ == "__main__":
    database1 = Database.load_db("TD_Database_alpha_0.1_discount_0.1.pickle")
    database2 = Database.load_db("TD_Database_alpha_0.1_discount_0.2.pickle")
    database3 = Database.load_db("TD_Database_alpha_0.1_discount_0.3.pickle")
    database4 = Database.load_db("TD_Database_alpha_0.1_discount_0.4.pickle")
    database5 = Database.load_db("TD_Database_alpha_0.1_discount_0.5.pickle")
    database6 = Database.load_db("TD_Database_alpha_0.1_discount_0.6.pickle")
    database7 = Database.load_db("TD_Database_alpha_0.1_discount_0.7.pickle")
    database8 = Database.load_db("TD_Database_alpha_0.1_discount_0.8.pickle")
    database9 = Database.load_db("TD_Database_alpha_0.1_discount_0.9.pickle")
    database10 = Database.load_db("negative10reward.pickle")
    random = Database.load_db("random_agent.pickle")
    plotWins([database1,database2,database3,database4,database5,database6,database7,database8,database9, database10], random)
    #printActionValues(database=database)