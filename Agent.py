import os
import selenium
import random

from BrowserInterface import Interface
from MatrixHasher import MatrixHasher

class MonteCarlo:
    def __init__(self, url: str, size: int, win: int) -> None:
        self.interface = Interface(url, size, win)
        self.mh = MatrixHasher()
        self.states = []

        # Example state (never will encounter)
        self.policy = {self.mh.matrixToString(
            [
                [2, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]) : [
                    ("up", 0.25),
                    ("down", 0.25),
                    ("left", 0.25),
                    ("right", 0.25)
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
        if not state in self.value:
            self.value[state] = 0.0
        
        return self.value[state]
    
    def update_value(self, state: str, reward: float) -> None:
        self.value[state] += reward
    
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
                    ("up", 0.25),
                    ("down", 0.25),
                    ("left", 0.25),
                    ("right", 0.25)
                ]

            # Get the action base on random n
            top = 0
            for i in range(0, len(self.policy[hashableState])):
                # Add prob of action to top
                top += self.policy[hashableState][i][1] # This is accessing the prob in (action, 0.xx)

                if n < top: # If prob sum is more than n do that action
                    action = self.policy[hashableState][i][0] # This is accessing the action in (action, 0.xx)
                    break

            self.interface.move(action)

            timeStep.append(action)
            timeStep.append(self.reward(self.interface.score()))
            self.lastScore = self.interface.score()

            episode.append(timeStep)

            # self.interface.lost should be properly breaking while loop
        
        return (episode, self.interface.won())
    
    def win_percentage(self, number_of_episodes: int) -> float:
        wins = 0

        for i in range(0, number_of_episodes):
            if self.run_episode()[1]:
                wins += 1
        
        return wins / number_of_episodes
    
    def export_policy(self) -> None:
        f = open("policy.log", "W")

        for k, v in self.policy:
            f.write("{k}:{v}")
        
        f.close
    '''
    def create_state_action_dictionary(self, policy):
        Q = {}
        for key in policy.keys():
            Q[key] = {a: 0.0 for a in range(0, self.interface.size)}
        return Q

    def create_random_policy(self):
     policy = {}
     for key in range(0, self.interface.size^2):
          current_end = 0
          p = {}
          for action in range(0, 4):
               p[action] = 1 / 4
          policy[key] = p
     return policy

    def test_policy(self):
      wins = 0
      r = 100
      for i in range(r):
            w = self.run_episode()[-1][-1]
            if w == 1:
                  wins += 1
      return wins / r
     
    def monte_carlo_e_soft(self, episodes=100, policy=None, epsilon=0.01):
        if not policy:
            policy = self.create_random_policy()  # Create an empty dictionary to store state action values    
        Q = self.create_state_action_dictionary(policy) # Empty dictionary for storing rewards for each state-action pair
        returns = {} # 3.
        
        for _ in range(episodes): # Looping through episodes
            G = 0 # Store cumulative reward in G (initialized at 0)
            episode = self.run_episode(policy=policy) # Store state, action and value respectively 
            
            # for loop through reversed indices of episode array. 
            # The logic behind it being reversed is that the eventual reward would be at the end. 
            # So we have to go back from the last timestep to the first one propagating result from the future.
            
            for i in reversed(range(0, len(episode))):   
                s_t, a_t, r_t = episode[i] 
                state_action = (s_t, a_t)
                G += r_t # Increment total reward by reward on current timestep
                
                if not state_action in [(x[0], x[1]) for x in episode[0:i]]: # 
                    if returns.get(state_action):
                        returns[state_action].append(G)
                    else:
                        returns[state_action] = [G]   
                        
                    Q[s_t][a_t] = sum(returns[state_action]) / len(returns[state_action]) # Average reward across episodes
                    
                    Q_list = list(map(lambda x: x[1], Q[s_t].items())) # Finding the action with maximum value
                    indices = [i for i, x in enumerate(Q_list) if x == max(Q_list)]
                    max_Q = random.choice(indices)
                    
                    A_star = max_Q # 14.
                    
                    for a in policy[s_t].items(): # Update action probability for s_t in policy
                        if a[0] == A_star:
                            policy[s_t][a[0]] = 1 - epsilon + (epsilon / abs(sum(policy[s_t].values())))
                        else:
                            policy[s_t][a[0]] = (epsilon / abs(sum(policy[s_t].values())))

        return policy
        '''

if __name__ == "__main__":
    FILE_URL = "file:" + os.getcwd() + "/2048-master/index.html"

    mc = MonteCarlo(FILE_URL, 3, 32)
    
    try:
        print(mc.win_percentage(100))

    except selenium.common.exceptions.NoSuchWindowException:
        print("Closed!")