from socket import socket

from src.client.actions import Action


class ClientHandler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, client_socket: socket = None):
        self.client_socket = client_socket

    def send(self, action: Action):
        self.client_socket.send(action.to_yaml())

    def close(self):
        self.client_socket.close()