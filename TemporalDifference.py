import os
import random
from Environment import Environment
from Episode import Episode
from Policy import Policy
from State import State
from Database import Database
from MonteCarlo import MonteCarlo
from GLIEMonteCarlo import GLIEMonteCarlo

import selenium

from BrowserInterface import Interface
from MatrixHasher import MatrixHasher

##Sarsa
def TemporalDifference(alpha, discount_rate, iterations, trace_decay = 0):
    #Initialize states with V = 0, Q = 0, e = 0
    GAME_URL = "file:" + os.getcwd() + "/2048-master/index.html"
    DATABASE_URL = "file:" + os.getcwd() + "/2048-master/TDdatabase.pickle"
    #database_name = "negative10reward.pickle"
    database_name = "TD_Database_alpha_{:.1f}_discount_{:.1f}.pickle".format(alpha, discount_rate)
    print(database_name)
    database = Database.load_db(database_name)
    interface = Interface(GAME_URL, 3, 32)
    environment = Environment(interface = interface ,database=database)
    policy = Policy(epsilon=0)
    episode_number = 0
    while(episode_number < iterations):
        #Re-initialize eleigibility traces vector to 0.0 at beginning of each episode
        done = False
        for state in database.states.values():
            state.eligibility_trace = 0
        episode_number += 1
        episode = Episode(None, None)
        state = environment.restart()
        print(episode_number)
        while(not done):
            results = environment.step(policy)
            nextState = results[0]
            action = results[1]
            nextAction = policy.getAction(nextState)
            reward = results[2]
            done = results[3]
            win = results[4]
            if win: done = True

            error = reward + discount_rate * nextState.getActionValue(nextAction) - state.getActionValue(action)
            state.setEligibilityTrace(action, state.getActionValue(action) + 1)
            for state in database.states.values():
                for action in state.actions:
                    action_name = action[0]
                    state.setActionValue(action_name, state.getActionValue(action_name) + alpha * error * state.getEligibilityTrace(action_name))
                    state.setEligibilityTrace(action, discount_rate * trace_decay * state.getEligibilityTrace(action_name))
            state = nextState
        if win: episode.win = True
        database.addEpisode(episode)
    database.save_db()