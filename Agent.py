import os
import random

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

if __name__ == "__main__":
    try:
        # GAME_URL = "file:" + os.getcwd() + "/2048-master/index.html"
        # DATABASE_URL = "file:" + os.getcwd() + "/2048-master/database.pickle"
        # database = Database.load_db()
        # interface = Interface(GAME_URL, 3, 32)
        # environment = Environment(interface = interface ,database=database)
        # policy = Policy()
        # iterations = 50000
        # algorithm = GLIEMonteCarlo(environment, database, policy, iterations)
        # database.save_db()
        alpha = .1
        discount_rate = 0.0
        iterations = 500
        while discount_rate < 1:
            discount_rate += .1
            TemporalDifference(alpha=alpha, discount_rate=discount_rate, iterations=iterations)
        
    except selenium.common.exceptions.NoSuchWindowException:
        # database.save_db()
        print("Closed!")
        