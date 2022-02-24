from flask import Flask, render_template, request

app = Flask(__name__)

class Game:
    def __init__(self) -> None:
        self.grid = {
                "grid": None,
                "score": None,
                "over": False,
                "won": False,
                "keepPlaying": True
                }

        self.move = {
                "move": None
                }

GAME = Game()

@app.route('/move', methods=['GET', 'POST'])
def move():
    if request.method == "POST":
        GAME.move = request.data

    return GAME.move

@app.route('/grid', methods=['GET', 'POST'])
def grid():
    if request.method == "POST":
        GAME.grid = request.data

    return GAME.grid