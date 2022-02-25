''' JSON from Server
{
    "grid":[[0,2,0,0],[0,0,0,0],[0,0,0,0],[2,0,4,0]],
    "keepPlaying":true,
    "over":false,
    "score":4,
    "stateCounter":0,
    "won":false
}
'''

class Game:
    def __init__(self) -> None:
        self.states = []
        self.currentState = {
                "grid": None,
                "score": None,
                "over": False,
                "won": False,
                "keepPlaying": True,
                "stateCounter": 0
                }

        self.action = {
                "move": None,
                "actionCounter": 0
                }
    
    def getState(self) -> dict:
        return self.currentState
    
    def getStates(self) -> list:
        return self.states

    def getAction(self) -> dict:
        return self.action

    def addState(self, state: dict) -> None:
        self.currentState["score"] = state["score"]
        self.currentState["over"] = state["over"]
        self.currentState["won"] = state["won"]
        self.currentState["stateCounter"] = state["state"]

        # Parses wack ass JSON into better form
        self.currentState["grid"] = []
        size = state["grid"]["size"]

        for row in range(0, size):
            temp = []
            for column in range(0, size):
                # If JS cell object
                if type(state["grid"]["cells"][column][row]) is dict:
                    temp.append(state["grid"]["cells"][column][row]["value"])
                # If null
                else:
                    temp.append(0)
            
            self.currentState["grid"].append(temp)
        
        self.states.append(self.currentState)

    def setAction(self, action: dict) -> None:
        self.action = action