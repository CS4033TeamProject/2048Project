from urllib import request
import requests
from Game import Game

class EnviromentManager:
    def __init__(self, url: str) -> None:
        self.url = url
        self.actionCounter = 0
        self.stateCounter = 0
        self.game = Game()

    def action(self, action: str) -> None:
        self.actionCounter += 1
        r = requests.post(self.url + "/move", json = {"move": action, "actionCounter": self.actionCounter})

    def state(self) -> tuple:
        r = requests.get(self.url + "/grid")
        self.game.setState(r.json())

        # Now passes a tuple that tells the agent whether new state or not
        if self.game.getState()["gridCounter"] > self.stateCounter:
            self.stateCounter += 1
            return (self.game.getState(), True)

        return (self.game.getState(), False)

if __name__ == "__main__":
    test = EnviromentManager("http://127.0.0.1:5000")
    print(test.state())
    test.action("right")
    print("did action right")
    print(requests.get("http://127.0.0.1:5000/move").json())