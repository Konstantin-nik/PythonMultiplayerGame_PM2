import random
from socket import socket
from threading import Thread, Lock

import json

from src.client.actions import Action
from src.game.objects.game_objects import GameObjects
from src.game.objects.player.player import Player


class ClientThread(Thread):
    def __init__(self, client_socket: socket, client_list: list[socket], client_list_lock: Lock,
                 game_objects_lock: Lock):
        super().__init__()
        self.client_socket = client_socket
        self.client_list = client_list
        self.client_list_lock = client_list_lock
        self.game_objects_lock = game_objects_lock

    def run(self):
        while True:
            data = self.client_socket.recv(2048)
            if not data:
                break

            action = Action.from_json(data)
            with self.game_objects_lock:
                game_objects = GameObjects()
                game_objects.update_game(self.client_socket, action)

            json_objects = game_objects.to_json()
            print(json_objects)
            t1 = Thread(target=self.send_to_clients, args=[json_objects])
            t1.start()

    def send_to_clients(self, data):
        with self.client_list_lock:
            for client in self.client_list:
                client.send(data.encode())
