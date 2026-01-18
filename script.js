// 🔴 CHANGE THIS ONLY WHEN BACKEND IS READY
const BACKEND_URL = "http://127.0.0.1:8000";


// UI switching
function showChat() {
  document.getElementById("chatbox").classList.remove("hidden");
  document.getElementById("sortingbox").classList.add("hidden");
}

function showSorting() {
  document.getElementById("sortingbox").classList.remove("hidden");
  document.getElementById("chatbox").classList.add("hidden");
}

// --------------------
// MastiKhorBot
// --------------------
async function sendChat() {
  const input = document.getElementById("chatInput");
  const message = input.value.trim();
  if (!message) return;

  const chatDiv = document.getElementById("chat");

  chatDiv.innerHTML += `<div class="message user">${message}</div>`;
  input.value = "";

  try {
    const response = await fetch(`${BACKEND_URL}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const botReply = await response.text();
    chatDiv.innerHTML += `<div class="message bot">${botReply}</div>`;
    chatDiv.scrollTop = chatDiv.scrollHeight;

    if (message.toLowerCase() === "bye") {
      input.disabled = true;
    }

  } catch (err) {
    chatDiv.innerHTML += `<div class="message bot">⚠️ Backend not connected</div>`;
  }
}

// --------------------
// SortingHat
// --------------------
async function uploadChat() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];

  if (!file) {
    alert("Please upload a .txt file");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch(`${BACKEND_URL}/sortinghat`, {
      method: "POST",
      body: formData
    });

    const resultText = await response.text();
    document.getElementById("result").innerText = resultText;

  } catch (err) {
    document.getElementById("result").innerText =
      "⚠️ Backend not connected";
  }
}
