function Agent(){
    this.state = "stopped";
    //this.listen();
}

document.addEventListener("start-agent", startAgent);

Agent.prototype.startAgent = function () {
    state = "started";
    while(this.state == "started"){
        //Make a move every second
        setInterval(this.makeMove(), 1000);
    }
}

Agent.prototype.stopAgent = function () {
    state = "stopped";
}

Agent.prototype.makeMove = function () {
    //Assigns move to a random integer from 0 to 3
    var move = Math.floor(Math.random() * 4);
    const moveEvent = new CustomEvent('agent-move', { detail: move});
    document.dispatchEvent(moveEvent);
}

