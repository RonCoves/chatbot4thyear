// script.js
document.addEventListener('DOMContentLoaded', function () {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendButton = document.querySelector('button');

    function appendMessage(sender, text) {
        const messageElement = document.createElement('div');
        messageElement.innerHTML = `<strong>${sender}:</strong> ${text}`;
        chatBox.appendChild(messageElement);
    }

    function sendMessage() {
        const userMessage = userInput.value;
        appendMessage('You', userMessage);

        // Send the user message to the server
        fetch('http://127.0.0.1:8082/webhook', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: { text: userMessage } }),
        })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.text;
            appendMessage('Bot', botResponse);
        })
        .catch(error => console.error('Error sending message:', error));

        // Clear the user input field
        userInput.value = '';
    }

    // Attach the sendMessage function to the button click event
    sendButton.addEventListener('click', sendMessage);

    // Listen for the 'keydown' event on the input field
    userInput.addEventListener('keydown', function (event) {
        // Check if the pressed key is Enter (key code 13)
        if (event.keyCode === 13) {
            // Prevent the default behavior (form submission)
            event.preventDefault();
            // Trigger the sendMessage function
            sendMessage();
        }
    });
});