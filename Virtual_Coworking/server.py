# server.py
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return "Virtual Co-working Space Server"

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(f"{username} has entered the room.", room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(f"{username} has left the room.", room=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    send(data['message'], room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
