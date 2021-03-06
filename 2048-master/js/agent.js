function Agent(){
    this.events = {};
    this.intervalID;
    this.state = "stopped";
    this.storageManager = new LocalStorageManager();
    this.moveInterval = 1000;
    this.gameState = this.storageManager.getGameState();
    console.log("Agent Called");
    
    this.listen();
    
    
}

Agent.prototype.on = function (event, callback) {
    if (!this.events[event]) {
        this.events[event] = [];
    }
    this.events[event].push(callback);
};

Agent.prototype.emit = function (event, data) {
    var callbacks = this.events[event];
    if (callbacks) {
        callbacks.forEach(function (callback) {
        callback(data);
    });
    }
};

Agent.prototype.listen = function() {
    console.log("Agent Listening");
    var self = this;

    document.addEventListener("startAgent", function (event) {
        console.log("Starting Agent");
        self.startAgent.call(self, event);
    });
    document.addEventListener("stopAgent", function (event) {
        console.log("Stopping Agent");
        self.stopAgent.call(self, event);
    });
}

Agent.prototype.startAgent = function (event) {
    event.preventDefault();
    console.log("Start Agent event called");
    this.state = "started";
    this.storageManager = new LocalStorageManager();
    this.gameState = this.storageManager.getGameState();
    //Makes moves until game is over
    while(!this.gameState.over){
        this.makeMove();
        this.gameState = this.storageManager.getGameState();
    }
    //Make a move every second
    //this.intervalID = window.setInterval(this.makeMove, this.moveInterval);
}

Agent.prototype.stopAgent = function (event) {
    event.preventDefault();
    this.state = "stopped";
    window.clearInterval(this.intervalID);
}

Agent.prototype.makeMove = function () {
    console.log("Moving");
    //Assigns move to a random integer from 0 to 3
    var move = Math.floor(Math.random() * 4 + 100);
    const moveEvent = new CustomEvent("agent-move", { detail: move});
    document.dispatchEvent(moveEvent);
}



