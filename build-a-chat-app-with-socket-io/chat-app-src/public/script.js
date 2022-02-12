const socket = io();

const messages = document.getElementById("messages");
const chatForm = document.getElementById("chat-form");
const input = document.getElementById("chat-input");

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();
  if (input.value) {
    socket.emit("chat", input.value);
    input.value = "";
  }
});

socket.on("chat", (msg) => {
  let item = document.createElement("li");
  item.textContent = msg;
  messages.appendChild(item);
  window.scrollTo(0, document.body.scrollHeight);
});