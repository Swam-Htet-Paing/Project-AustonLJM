let movingInterval = null;

function sendCommand(command) {
    fetch('/' + command, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ command: command })
    }).then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}

document.addEventListener("keydown", event => {
    if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'KeyW', 'KeyA', 'KeyS', 'KeyD'].includes(event.code)) {
        switch (event.code) {
            case "ArrowUp":
            case "KeyW":
                sendCommand('w');
                break;
            case "ArrowDown":
            case "KeyS":
                sendCommand('s');
                break;
            case "ArrowLeft":
            case "KeyA":
                sendCommand('a');
                break;
            case "ArrowRight":
            case "KeyD":
                sendCommand('d');
                break;
        }
    }
});

function startMoving(direction) {
    if (movingInterval) clearInterval(movingInterval);
    movingInterval = setInterval(() => {
        switch (direction) {
            case 'up':
                sendCommand('w');
                break;
            case 'down':
                sendCommand('s');
                break;
            case 'left':
                sendCommand('a');
                break;
            case 'right':
                sendCommand('d');
                break;
        }
        updatePosition();
    }, 30);
}

function stopMoving() {
    clearInterval(movingInterval);
}

const buttons = ["up", "down", "left", "right"];
buttons.forEach(direction => {
    document.getElementById(direction).addEventListener("mousedown", () => startMoving(direction));
    document.getElementById(direction).addEventListener("touchstart", (event) => {
        event.preventDefault(); // Prevent context menu
        startMoving(direction);
    });

    document.getElementById(direction).addEventListener("mouseup", stopMoving);
    document.getElementById(direction).addEventListener("touchend", (event) => {
        event.preventDefault(); // Prevent context menu
        stopMoving();
    });

    document.getElementById(direction).addEventListener("mouseleave", stopMoving);
    document.getElementById(direction).addEventListener("touchcancel", (event) => {
        event.preventDefault(); // Prevent context menu
        stopMoving();
    });
});