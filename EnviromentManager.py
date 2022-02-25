from urllib import request
import requests

class EnviromentManager:
    def __init__(self, url: str) -> None:
        self.url = url
        self.actionCounter = 0
        self.stateCounter = -1

    def action(self, action: str) -> None:
        self.actionCounter += 1
        r = requests.post(self.url + "/move", json = {"move": action, "actionCounter": self.actionCounter})

    def state(self) -> tuple:
        r = requests.get(self.url + "/grid")

        # Now passes a tuple that tells the agent whether new state or not
        if r.json()["stateCounter"] > self.stateCounter:
            self.stateCounter += 1
            return (r.json(), True)

        return (r.json(), False)

if __name__ == "__main__":
    test = EnviromentManager("http://127.0.0.1:5000")
    print(test.state())
    test.action("right")
    print("did action right")
    print(requests.get("http://127.0.0.1:5000/move").json())