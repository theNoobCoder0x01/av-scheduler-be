import axios from "axios";
import express from "express";

// index.js
const app = express();
const port = 3000;

const VLC_AUTH = {
  username: "",
  password: "your_password",
};

const VLC_URL = "http://localhost:8080/requests/status.json";

app.get("/play", async (req, res) => {
  await axios.get(VLC_URL + "?command=pl_play", { auth: VLC_AUTH });
  res.json({ status: "playing" });
});

app.get("/pause", async (req, res) => {
  await axios.get(VLC_URL + "?command=pl_pause", { auth: VLC_AUTH });
  res.json({ status: "paused" });
});

app.get("/stop", async (req, res) => {
  await axios.get(VLC_URL + "?command=pl_stop", { auth: VLC_AUTH });
  res.json({ status: "stopped" });
});

app.post("/load_playlist", express.json(), async (req, res) => {
  const path = req.body.path;
  await axios.get(
    VLC_URL + `?command=in_play&input=${encodeURIComponent(path)}`,
    { auth: VLC_AUTH }
  );
  res.json({ status: "playlist loaded", path });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
