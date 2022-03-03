import os
import random
from Environment import Environment
from Episode import Episode
from Policy import Policy
from State import State
from Database import Database
from MonteCarlo import MonteCarlo
from GLIEMonteCarlo import GLIEMonteCarlo
from datetime import datetime

from BrowserInterface import Interface
from MatrixHasher import MatrixHasher

if __name__ == "__main__":
    GAME_URL = "file:" + os.getcwd() + "/2048-master/index.html"
    DATABASE_URL = "file:" + os.getcwd() + "/2048-master/database.json"
    database = Database(DATABASE_URL)
    states = database.states
    interface = Interface(GAME_URL, 3, 64)
    environment = Environment(interface = interface ,database=database)
    policy = Policy(database.states, epsilon = 1)
    iterations = 1000
    algorithm = GLIEMonteCarlo(environment, database, policy, iterations)