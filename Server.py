from flask import Flask, request
from flask_cors import CORS
from Game import Game

app = Flask(__name__)
CORS(app)

GAME = Game()

@app.route('/move', methods=['GET', 'POST'])
def move():
    if request.method == "POST":
        print(request.json)
        GAME.setMove(request.json)

    return GAME.getMove()

@app.route('/grid', methods=['GET', 'POST'])
def grid():
    if request.method == "POST":
        print(request.json)
        GAME.setGrid(request.json)

    return GAME.getGrid()