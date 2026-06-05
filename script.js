// ===== DOM Elements =====
const messagesDiv = document.getElementById("messages");
const input = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const typingIndicator = document.getElementById("typing");
const clearBtn = document.getElementById("clearBtn");

// ===== Utility: Get formatted time =====
function getTimeString() {
  return new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
  });
}

// ===== Utility: Escape HTML to prevent XSS =====
function escapeHTML(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

// ===== Add a message to the chat =====
function addMessage(text, sender) {
  const messageEl = document.createElement("div");
  messageEl.classList.add("message", sender);

  const avatar = document.createElement("div");
  avatar.classList.add("avatar"); // FIXED: Removed trailing space

  if (sender === "bot") {
    avatar.classList.add("bot-avatar"); // FIXED: Removed trailing space
    avatar.innerHTML = '<i class="fas fa-robot"></i>';
  } else {
    avatar.classList.add("user-avatar"); // FIXED: Removed trailing space
    avatar.innerHTML = '<i class="fas fa-user"></i>';
  }

  const wrapper = document.createElement("div");
  wrapper.classList.add("bubble-wrapper");

  const bubble = document.createElement("div");
  bubble.classList.add("bubble");

  // FIXED: Corrected the mangled regex for bold text
  bubble.innerHTML = escapeHTML(text).replace(/\*\*(.*?)\*\*/g, "<b>$1</b>");

  const timestamp = document.createElement("span");
  timestamp.classList.add("timestamp");
  timestamp.textContent = getTimeString();

  wrapper.appendChild(bubble);
  wrapper.appendChild(timestamp);
  messageEl.appendChild(avatar);
  messageEl.appendChild(wrapper);

  messagesDiv.appendChild(messageEl);
  scrollToBottom();
}

// ===== Scroll to bottom of messages =====
function scrollToBottom() {
  requestAnimationFrame(() => {
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  });
}

// ===== Show / Hide typing indicator =====
function showTyping() {
  typingIndicator.classList.add("show");
  scrollToBottom();
}

function hideTyping() {
  typingIndicator.classList.remove("show");
}

// ===== Auto-resize textarea =====
function autoResize() {
  input.style.height = "auto";
  input.style.height = Math.min(input.scrollHeight, 120) + "px";
}

// ===== Send message =====
async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  sendBtn.disabled = true;
  input.disabled = true;

  addMessage(text, "user");
  input.value = "";
  autoResize();
  showTyping();

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();
    hideTyping();
    addMessage(data.response || "No response received.", "bot");
  } catch (error) {
    console.error("Error:", error);
    hideTyping();
    addMessage(
      "Connection error. Make sure app.py is running on port 5000.",
      "bot",
    );
  } finally {
    sendBtn.disabled = false;
    input.disabled = false;
    input.focus();
  }
}

// ===== Clear chat =====
function clearChat() {
  messagesDiv.innerHTML = "";
  addMessage("Chat cleared! Type <b>help</b> to see what I can do.", "bot");
}

// ===== Event Listeners =====
sendBtn.addEventListener("click", (e) => {
  e.preventDefault();
  sendMessage();
});

input.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

input.addEventListener("input", autoResize);

clearBtn.addEventListener("click", () => {
  if (messagesDiv.children.length > 0) {
    clearChat();
  }
});

// ===== Initialize =====
input.focus();
