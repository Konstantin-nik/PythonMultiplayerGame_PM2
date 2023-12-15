from socket import socket
from threading import Lock, Thread

from src.game.objects.game_objects import GameObjects


class ReceiveThread(Thread):
    def __init__(self, client_socket: socket, game_objects_lock: Lock):
        super().__init__()
        self.client_socket = client_socket
        self.game_objects_lock = game_objects_lock

    def run(self):
        while True:
            data = self.client_socket.recv(40000)
            if not data:
                break

            game_objects = GameObjects()

            with self.game_objects_lock:
                game_objects.update_objects(data)

        self.client_socket.close()
