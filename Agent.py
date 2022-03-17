import os

from Environment import Environment
from Episode import Episode
from Policy import Policy
from State import State
from Database import Database
from MonteCarlo import MonteCarlo
from GLIEMonteCarlo import GLIEMonteCarlo
from TemporalDifference import TemporalDifference

import selenium

from BrowserInterface import Interface
from MatrixHasher import MatrixHasher

def runSarsa(eps: int):
        #Iterate forever with discount rates .1-.9
    while True:
        alpha = .2
        discount_rate = .5
        iterations = eps
        while discount_rate < .6:
            TemporalDifference(alpha=alpha, discount_rate=discount_rate, iterations=iterations)
            discount_rate += .1
            discount_rate = round(discount_rate, 1)

def runRandom():
    iterations = 1000
    GAME_URL = "file:" + os.getcwd() + "/2048-master/index.html"
    database = Database.load_db("random_agent_2.pickle")
    
    interface = Interface(GAME_URL, 3, 32)
    environment = Environment(interface = interface ,database=database)
    policy = Policy(epsilon=1)
    episodeNumber = 0
    while(iterations > episodeNumber):
        episodeNumber+=1
        episode = Episode(environment, policy)
        episode.run_episode(environment)
        database.addEpisode(episode)

    database.save_db()

if __name__ == "__main__":
    try:
        runSarsa(10000)
        #runRandom()
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
        