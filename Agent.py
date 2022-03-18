from Environment import Environment
from Episode import Episode
from Policy import Policy
from Database import Database
from TemporalDifference import TemporalDifference
from PythonInterface import PythonInterface

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

    for i in range(0, 100):
        print("Run number: ", i)
        runSarsa(1000, .005, 1, 1)
        