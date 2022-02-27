import os
import selenium
import random
from datetime import datetime

from BrowserInterface import Interface
from MatrixHasher import MatrixHasher

class GLIEMonteCarlo:
    def __init__(self, iterations = 1000, environment = Environment()) -> None:
        ##state-action values are 0
        ##state-action times visited are 0
        self.environment = environment
        self.iterations = iterations
        self.episodes = 1
        self.epsilon = 1
        self.Q = None
        self.N = None
        self.policy = ESoftPolicy(self.epsilon, environment.states)

        while(self.episodes < self.iterations):
            episode = Episode(environment, policy)
            self.Q = self.updateQ(episode)
            self.episodes += 1
            self.epsilon = 1/self.episodes
            policy = Policy(environment.states, self.epsilon)

    def updateQ(self, episode):
        for move in episode.moves:
            state = move[0]
            action = move[1]
            self.N[state][action] += 1
            self.Q[state][action] = self.Q[state][action] + 1/self.N[state][action] * (episode.reward - self.Q[state][action])
        
class Episode:
    def __init__(self, environment, policy) -> None:
        #move = (state, action, reward)
        self.moves = []
        self.reward = 0
        self.run_episode(environment, policy)
    def run_episode(self, environment, policy):
        done = False
        state = environment.start()
        while(not done):
            move = environment.step(policy.getAction(state))
            self.moves.append(move)
            self.reward += move[2]
            state = move[0]
            if(state.isTerminal): done = True


class Environment:
    def __init__(self, interface=Interface(), states = []) -> None:
        self.interface = interface
        self.states = states
        self.action_space = self.interface.getActions()
        self.initialState = interface.start()
        self.currentState = self.initialState
    
    #Store a new state into the observation space if it's not already stored
    def addState(self, state) -> None:
        if(state not in self.states): self.states.append(state)
    
    def step(self, action):
        #Make a move in the game
        self.interface.move(action)
        
        #Get the next state, and add it to the list of states
        next_state = self.interface.getGrid()
        self.states.add(next_state)
        
        #Pair the current state's action to the next state
        self.currentState.pairAction(action,next_state)

        #Get the reward, if we won, and extra info
        reward = self.interface.getReward()
        done = self.interface.getDone()
        info = self.interface.getInfo()

        return next_state, reward, done, info

    def incrementalUpdate(state, reward) -> float:
        value = state.value + 1/env.states.size()*(reward-state.value)
        return value

    def reset():
        pass


class State:
    def __init__(self, grid, value=0, previousState = None) -> None:
        self.grid = grid
        self.actions = {
            "up"    : None,
            "down"  : None,
            "left"  : None,
            "right" : None}
        self.value = value
        self.previousState = previousState
        #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     self.policy = policy

    def __hash__(self) -> int:
        return hash((self.grid, self.actions, self.value, self.previousState))

    def pairAction(self, action, nextState):
        self.actions[action] = nextState

    #Expected return when starting in state and following policy thereafter
    def value(self, policy) -> float:
        return self.value
    
    def actionValueFunction(self, action) -> float:
        return self.value
    
class Policy:
    def __init__(self) -> None:
        pass

    #Expected return when starting in state and following policy thereafter
    #
    #bellman equation for value function=(sum of policy(action|state) for all actions) * (sum of (probability of (s',r|s,a)) * (reward + gamma*value function of s')
    def stateValue(self, state) -> float:
        return self.value
    
    #Expected return starting from state, taking action, and thereafter following policy
    def actionValue(self, state, action) -> float:
        return self.value
    
    
    #Perform an expected update on all states to calculate policy value pg 74
    def interativePolicyEvaluation(policy) -> None:
        #Expected update
        #Loop
            #Delta = 0
            #Loop for each state s in S
                #v = Value(state)
                #Value(state) = Expected update
                #delta = max(delta,|v - Value(state))
            #until delta < theta-determines accuracy of estimation
        pass
class MonteCarlo:
    def __init__(self, url: str, size: int, win: int) -> None:
        self.interface = Interface(url, size, win)
        self.mh = MatrixHasher()

        # Dictionary that tells which states follow a state
        self.states = {}
        '''
        self.states = {self.mh.matrixToString(
            [
                [2, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]) : {
                    "up": state,
                    "down": state,
                    ...
            }
        }
        '''

        # Example state (never will encounter)
        self.policy = {self.mh.matrixToString(
            [
                [2, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]) : [ #TODO make this a dict
                    ["up", 0.25],
                    ["down", 0.25],
                    ["left", 0.25],
                    ["right", 0.25]
            ]
        }
        self.values = {}
        self.lastScore = 0
    
    def restart(self) -> None:
        self.interface.restart()
    
    def action(self, direction: str) -> None:
        self.interface.move(direction)
    
    def state(self) -> list:
        return self.interface.data()
    
    def score_reward(self, currentScore: int) -> int:
        return currentScore - self.lastScore
    
    def reward(self) -> int:
        if self.interface.won():
            return 1
        return 0
    
    def value(self, state: str) -> float:
        if not state in self.values:
            self.values[state] = 0.0
        
        return self.values[state]
    
    # Update state and also add state
    def update_state(self, state: str, action = None, next_state = None) -> None:
        if not state in self.states:
            self.states[state] = {
                "up": "[0, 0, 0],[0, 0, 0],[0, 0, 0]",
                "down": "[0, 0, 0],[0, 0, 0],[0, 0, 0]",
                "left": "[0, 0, 0],[0, 0, 0],[0, 0, 0]",
                "right": "[0, 0, 0],[0, 0, 0],[0, 0, 0]"
            }

        if action != None and next_state != None:
            self.states[state][action] = next_state
    
    def run_episode(self) -> list:
        self.restart()
        self.lastScore = 0
        
        # Episode will hold each time step: [[state, action, reward], [...]]
        episode = []
        
        while (not self.interface.lost()) and (not self.interface.won()):
            state = self.interface.grid()
            hashableState = self.mh.matrixToString(state)

            # Time step will hold [state, action, reward]
            timeStep = []
            timeStep.append(state)

            # Generate random iid probabiity
            n = random.uniform(0, 1)

            # Make sure state is in policy
            # If not then add to policy with default probs
            if not hashableState in self.policy:
                self.policy[hashableState] = [
                    ["up", 0.25],
                    ["down", 0.25],
                    ["left", 0.25],
                    ["right", 0.25]
                ]

            # Get the action base on random n
            top = 0
            for i in range(0, len(self.policy[hashableState])):
                # Add prob of action to top
                top += self.policy[hashableState][i][1] # This is accessing the prob in [action, 0.xx]

                if n < top: # If prob sum is more than n do that action
                    action = self.policy[hashableState][i][0] # This is accessing the action in [action, 0.xx]
                    break

            self.interface.move(action)

            timeStep.append(action)
            timeStep.append(self.reward())
            self.lastScore = self.interface.score()

            episode.append(timeStep)

            # Updates self.states dictionary
            if len(episode) > 1:
                self.update_state(self.mh.matrixToString(episode[len(episode)-1][0]), episode[len(episode)-1][1], hashableState)

            # self.interface.lost should be properly breaking while loop
        
        return (episode, self.interface.won())
    
    def value_iteration(self, episode: tuple) -> None:
        numTimeSteps = len(episode[0])

        # If won the episode
        if episode[1]:
            # Loop thru and give equal reward to states
            for i in range(0, numTimeSteps):
                state = self.mh.matrixToString(episode[0][i][0])

                # Make sure state is in values
                if not state in self.values:
                    self.values[state] = 0.0

                self.values[state] += (1 / numTimeSteps)
    
    def policy_update(self, episode: tuple):
        self.value_iteration(episode)

        numTimeSteps = len(episode[0])

        map = {
                0: "up",
                1: "down",
                2: "left",
                3: "right"
            }

        for i in range(0, numTimeSteps):
            bestValue = 0
            bestAction = "up"

            # Determine the action that leads to the highest value state
            for i in range(0, 4):
                # Make sure state is in states dict
                self.update_state(self.mh.matrixToString(episode[0][i][0]))

                if self.value( self.states[self.mh.matrixToString(episode[0][i][0])][map[i]] ) > bestValue:
                    bestValue = self.value( self.states[self.mh.matrixToString(episode[0][i][0])][map[i]] )
                    bestAction = map[i]
            
            # Update policy to favor that action
            
            # Make sure no action is already at 1.0
            bestActionExists = False
            for i in range(0, 4):
                state = self.mh.matrixToString(episode[0][i][0])
                action_prob = self.policy[state][i][1]
                
                if action_prob == 1.0:
                    bestActionExists = True
            
            # If no action is at 1.0 then update
            if not bestActionExists:
                for i in range(0, 4):
                    state = self.mh.matrixToString(episode[0][i][0])
                    action_prob = self.policy[state][i][1]

                    if map[i] == bestAction:
                        action_prob += 0.15
                    else:
                        action_prob -= 0.05
    
    def win_percentage(self, number_of_episodes: int) -> float:
        wins = 0

        for i in range(0, number_of_episodes):
            if self.run_episode()[1]:
                wins += 1
        
        return wins / number_of_episodes
    
    def export_policy(self) -> None:
        f = open("policy.log", "w")

        f.write(str(self.policy))
        
        f.close
    
    def run_with_policy_update(self, number_of_episodes: int) -> float:
        wins = 0

        f = open("big.csv", "a")
        f.write("time,episode,wins,winrate\n")

        for i in range(0, number_of_episodes):
            episode = self.run_episode()

            if episode[1]:
                wins += 1
            
            # OUTPUTS
            time = datetime.now().strftime("%H:%M:%S")
            print(time)
            print(f"Episode number = {i}")
            print(f"Wins = {wins}")
            print(f"Win rate = {wins / (i + 1)}")
            print()

            f = open("big.csv", "a")
            f.write(time + "," + str(i) + "," + str(wins) + "," + str(wins / (i + 1)) + "\n")
            f.close()


            self.policy_update(episode)
        
        print("Done.")

if __name__ == "__main__":
    FILE_URL = "file:" + os.getcwd() + "/2048-master/index.html"

    mc = MonteCarlo(FILE_URL, 3, 8)
    
    try:
<<<<<<< HEAD
        mc.run_with_policy_update(50000)
=======
        mc.run_with_policy_update(1000)
>>>>>>> 463b82bb95321145f0cddf3e610cbedb5d9d861c
        mc.export_policy()

    except selenium.common.exceptions.NoSuchWindowException:
        mc.export_policy()
        print("Closed!")