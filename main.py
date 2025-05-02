# main.py
from fastapi import FastAPI
import requests
from requests.auth import HTTPBasicAuth

VLC_URL = "http://localhost:8080/requests/status.json"
VLC_COMMAND_URL = "http://localhost:8080/requests/status.json?command="
auth = HTTPBasicAuth('', 'your_password')  # Username is empty, only password used

app = FastAPI()

@app.get("/play")
def play():
    try:
        requests.get(VLC_COMMAND_URL + "pl_play", auth=auth)
    except Exception as e:
        return {"error": "Failed to play VLC", "details": str(e)}
    return {"status": "playing"}

@app.get("/pause")
def pause():
    try:
        requests.get(VLC_COMMAND_URL + "pl_pause", auth=auth)
    except Exception as e:
        return {"error": "Failed to pause VLC", "details": str(e)}
    return {"status": "paused"}

@app.get("/stop")
def stop():
    try:
        requests.get(VLC_COMMAND_URL + "pl_stop", auth=auth)
    except Exception as e:
        return {"error": "Failed to stop VLC", "details": str(e)}
    return {"status": "stopped"}

@app.post("/load_playlist")
def load_playlist(path: str):
    try:
        requests.get(VLC_COMMAND_URL + f"in_play&input={path}", auth=auth)
    except Exception as e:
        return {"error": "Failed to load playlist", "details": str(e)}
    return {"status": "playlist loaded", "path": path}

@app.get("/playlist")
def get_playlist():
    r = requests.get("http://localhost:8080/requests/playlist.json", auth=auth)
    return r.json()

@app.get("/seek_to_track")
def seek_to_track(track_id: int):
    try:
        requests.get(VLC_COMMAND_URL + f"pl_play&id={track_id}", auth=auth)
    except Exception as e:
        return {"error": "Failed to seek to track", "details": str(e)}
    return {"status": "seeking to track", "id": track_id}

@app.get("/seek_time")
def seek_time(seconds: int):
    try:
        requests.get(VLC_COMMAND_URL + f"seek&val={seconds}", auth=auth)
    except Exception as e:
        return {"error": "Failed to seek time", "details": str(e)}
    return {"status": f"seeked to {seconds}s"}
