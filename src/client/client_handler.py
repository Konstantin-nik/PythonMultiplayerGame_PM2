from socket import socket

from src.common.actions import Action
from src.common.tools.data_sharing_tool import DataSharingTool


class ClientHandler:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, client_socket: socket = None):
        if not self._initialized:
            self.client_socket = client_socket
            self._initialized = True

    def send(self, action: Action):
        self.client_socket.send(DataSharingTool.to_json(action).encode())

    def close(self):
        self.client_socket.close()
