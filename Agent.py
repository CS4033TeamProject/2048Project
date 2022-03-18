import os

from Environment import Environment
from Episode import Episode
from Policy import Policy
from State import State
from Database import Database
from MonteCarlo import MonteCarlo
from GLIEMonteCarlo import GLIEMonteCarlo
from TemporalDifference import TemporalDifference
from PythonInterface import PythonInterface

import selenium

from BrowserInterface import Interface
from MatrixHasher import MatrixHasher

def runSarsa(iterations, alpha, start, end):
    #Iterate with discount rates .1-.9
    alpha = alpha
    discount_rate = start
    iterations = iterations
    while discount_rate <= end:
        TemporalDifference(alpha=alpha, discount_rate=discount_rate, iterations=iterations, size = 2, win = 16)
        discount_rate += .1
        discount_rate = round(discount_rate, 1)

def runRandom(iterations, size, win):
    database_name = "random_agent_size_{}_win_{}.pickle".format(size, win)
    database = Database.load_db(database_name)
    interface = PythonInterface(size, win)
    environment = Environment(interface = interface ,database=database)
    policy = Policy(epsilon=1)
    episode_number = 0
    while(episode_number < iterations):
        #Re-initialize eleigibility traces vector to 0.0 at beginning of each episode
        done = False
        episode_number += 1
        episode = Episode(None, None)
        environment.restart()
        #print(episode_number)
        while(not done):
            results = environment.step(policy)
            done = results[3]
            win = results[4]
            if win: done = True
        if win: episode.win = True
        database.addEpisode(episode)

    database.save_db()

if __name__ == "__main__":
    try:
        for i in range(0, 100):
            print("Run number: ", i)
            runSarsa(1000, .005, 1, 1)
            #runRandom(1000, 2, 16)
        # GAME_URL = "file:" + os.getcwd() + "/2048-master/index.html"
        # DATABASE_URL = "file:" + os.getcwd() + "/2048-master/database.pickle"
        # database = Database.load_db()
        # interface = Interface(GAME_URL, 3, 32)
        # environment = Environment(interface = interface ,database=database)
        # policy = Policy()
        # iterations = 50000
        # algorithm = GLIEMonteCarlo(environment, database, policy, iterations)
        # database.save_db()



    except selenium.common.exceptions.NoSuchWindowException:
        # database.save_db()
        print("Closed!")
        