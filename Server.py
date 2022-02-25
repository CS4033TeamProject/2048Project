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
        GAME.setAction(request.json)

    return GAME.getAction()

@app.route('/grid', methods=['GET', 'POST'])
def grid():
    if request.method == "POST":
        print(request.json)
        GAME.setState(request.json)

    return GAME.getState()