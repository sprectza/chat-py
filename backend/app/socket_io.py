import socketio
from fastapi import FastAPI
from socketio import ASGIApp

sio = socketio.AsyncServer(
    async_mode="asgi", cors_allowed_origins=["http://127.0.0.1:8000"]
)

app = FastAPI()
sio_app = ASGIApp(socketio_server=sio)


@app.on_event("startup")
async def startup():
    sio.attach(app)


@sio.event
async def connect(sid, environ):
    print(f"User connected: {sid}")


@sio.event
async def disconnect(sid):
    print(f"User disconnected: {sid}")


@sio.event
async def send_message(sid, message):
    print(f"Message received: {message}")
    await sio.emit("receive_message", message, room=None, skip_sid=sid)
