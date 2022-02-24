function Agent(){
    this.events = {};

    console.log("Agent Called");
    this.state = "stopped";
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
    //Make a move every second
    setInterval(this.makeMove(), 1000);
}

Agent.prototype.stopAgent = function (event) {
    event.preventDefault();
    this.state = "stopped";
}

Agent.prototype.makeMove = function () {
    console.log("Moving");
    if(this.state === "started"){
        //Assigns move to a random integer from 0 to 3
        var move = Math.floor(Math.random() * 4);
        const moveEvent = new CustomEvent('agent-move', { detail: move});
        document.dispatchEvent(moveEvent);
    }
    
}

