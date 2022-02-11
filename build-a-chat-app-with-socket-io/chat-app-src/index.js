const express = require("express");
const app = express();
const server = require("http").Server(app);
const port = 3000;

app.use(express.static("public"));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

server.listen(port, () => {
  console.log("Chat app server running at port " + port);
});

const io = require("socket.io")(server);

io.on("connection", (socket) => {
  socket.on("chat", (msg) => {
    io.emit("chat", msg);
  });
});
