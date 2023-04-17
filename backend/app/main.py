from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .socket_io import sio_app

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", sio_app)
