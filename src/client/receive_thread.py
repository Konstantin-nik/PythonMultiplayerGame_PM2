from socket import socket
from threading import Lock, Thread

from src.common.tools.data_sharing_tool import DataSharingTool
from src.game.objects.game_objects import GameObjects


class ReceiveThread(Thread):
    def __init__(self, client_socket: socket, game_objects_lock: Lock):
        super().__init__()
        self.client_socket = client_socket
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
                game_objects = GameObjects()

                with self.game_objects_lock:
                    game_objects.update_objects(obj)

        self.client_socket.close()
