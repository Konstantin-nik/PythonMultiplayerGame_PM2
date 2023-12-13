from threading import Lock, Thread
from socket import socket


class ReceiveThread(Thread):
    def __init__(self, client_socket: socket, game_state_lock: Lock):
        Thread.__init__(self)
        self.client_socket = client_socket
        self.game_state = game_state
        self.game_state_lock = game_state_lock

    def run(self):
        while True:
            data = self.client_socket.recv(2048)
            if not data:
                break

            with self.game_state_lock:
                self.game_state.update_state(data)

        self.client_socket.close()