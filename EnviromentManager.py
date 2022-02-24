from urllib import request
import requests
from Game import Game

class EnviromentManager:
    def __init__(self, url: str) -> None:
        self.url = url
        self.moveCounter = 0
        self.game = Game()

    def action(self, action: str) -> None:
        self.moveCounter += 1
        r = requests.post(self.url + "/move", json = {"move": action, "moveCounter": self.moveCounter})

    def state(self) -> dict:
        r = requests.get(self.url + "/grid")
        self.game.grid = r.json()

        return self.game.grid

if __name__ == "__main__":
    test = EnviromentManager("http://127.0.0.1:5000")
    print(test.state())
    test.action("right")
    print("did action right")
    print(requests.get("http://127.0.0.1:5000/move").json())