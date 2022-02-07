const socket = io();

const chatForm = document.querySelector(".chat-form");
const input = document.querySelector(".chat-input");

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();

  socket.emit("chat", input.value);
  input.value = "";
});
