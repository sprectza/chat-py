# Simple Chat Application

This is a basic chat application built using Python, Django, FastAPI, Socket.IO, and JavaScript. Users can send and receive messages in real-time with this application.

## Prerequisites

    Python 3.6 or higher
    FastAPI
    Uvicorn
    python-socketio

## Installation

Clone the repository:

git clone https://github.com/sprectza/chat-py.git

Change to the project directory:

cd chat-py

Install the required packages:

pip install -r requirements.txt

Running the Application

    Start the FastAPI server:

    uvicorn backend.app.main:app --host 0.0.0.0 --port 8001 --reload

    Open your preferred web browser and go to http://127.0.0.1:8000/chat/.

## Usage

    Type your message in the input field.
    Click the "Send" button or press Enter to send the message.
    The message will appear in the chatbox.

You can open the chat application in multiple browser windows to simulate a multi-user chat experience.
