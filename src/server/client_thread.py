from socket import socket
from threading import Thread, Lock

from src.common.actions import is_action
from src.common.tools.data_sharing_tool import DataSharingTool
from src.game.objects.game_objects import GameObjects


class ClientThread(Thread):
    def __init__(self, client_socket: socket, client_list: list[socket], client_list_lock: Lock,
                 game_objects_lock: Lock):
        super().__init__()
        self.client_socket = client_socket
        self.client_list = client_list
        self.client_list_lock = client_list_lock
        self.game_objects_lock = game_objects_lock

    def run(self):
        data_sharing_tool = DataSharingTool()
        while True:
            data = self.client_socket.recv(2048)
            if not data:
                break

            data_sharing_tool.add_data(data=data.decode())

            for ans in data_sharing_tool:
                if ans is None:
                    continue

                name, obj = ans
                if is_action(name):
                    with self.game_objects_lock:
                        game_objects = GameObjects()
                        game_objects.update_game(self.client_socket, obj)

            json_objects = DataSharingTool.to_json(game_objects)

            self.send_to_clients(json_objects)
            # t1 = Thread(target=self.send_to_clients, args=[json_objects])
            # t1.start()

    def send_to_clients(self, data):
        with self.client_list_lock:
            for client in self.client_list:
                client.send(data.encode())
