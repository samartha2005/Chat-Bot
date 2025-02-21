function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput) return;
    
    let messageContainer = document.getElementById("messages");
    messageContainer.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    document.getElementById("user-input").value = "";

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        messageContainer.innerHTML += `<p><strong>Bot:</strong> ${data.message}</p>`;
        messageContainer.scrollTop = messageContainer.scrollHeight;
    })
    .catch(error => console.error("Error:", error));
}
