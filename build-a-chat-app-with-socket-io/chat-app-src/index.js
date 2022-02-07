const express = require("express");

const chatApp = express();
const server = require("http").createServer(chatApp);
const port = 3000;
const io = require("socket.io")(server);
const path = require("path");

chatApp.use(express.static(path.join(__dirname + "/public")));

server.listen(port, () => {
  console.log("Server running on port: " + port);
});

io.on("connection", (socket) => {
  console.log("Some clinet is connected.\n" + socket);

  socket.on("chat", (msg) => {
    console.log("From client", msg);
  });
});
