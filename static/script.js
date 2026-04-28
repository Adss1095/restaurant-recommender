// ===== Send Message =====
async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const userText = inputField.value.trim();

    if (userText === "") return;

    // Show user message
    addMessage(userText, "user");

    inputField.value = "";

    try {
        const response = await fetch("/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: userText })
        });

        const data = await response.json();

        if (data.error) {
            addMessage("❌ " + data.error, "bot");
            return;
        }

        addMessage("Here are some recommendations 👇", "bot");

        // Show cards
        data.results.forEach(r => {
            addRestaurantCard(r);
        });

    } catch (error) {
        addMessage("⚠️ Server error. Please try again.", "bot");
        console.error(error);
    }
}


// ===== Add Chat Message =====
function addMessage(message, type) {
    const chatBox = document.getElementById("chat-box");

    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", type);
    msgDiv.innerText = message;

    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}


// ===== Add Restaurant Card =====
function addRestaurantCard(r) {
    const chatBox = document.getElementById("chat-box");

    const card = document.createElement("div");
    card.classList.add("card");

    card.innerHTML = `
        <h3>${r.name}</h3>
        <p>⭐ Rating: ${r.rating}</p>
        <p>💰 Cost for two: ₹${r.cost}</p>
        <p class="score">Match Score: ${r.score}</p>
    `;

    chatBox.appendChild(card);
    chatBox.scrollTop = chatBox.scrollHeight;
}


// ===== Enter Key Support =====
document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("user-input");

    input.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            sendMessage();
        }
    });
});