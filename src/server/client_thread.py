from socket import socket
from threading import Thread, Lock

from src.game.objects.game_objects import GameObjects


class ClientThread(Thread):
    def __init__(self, client_socket: socket, client_list: list[socket],
                 client_list_lock: Lock, game_objects_lock: Lock):
        Thread.__init__(self)
        self.client_socket = client_socket
        self.client_list = client_list
        self.client_list_lock = client_list_lock
        self.game_objects_lock = game_objects_lock

    def run(self):
        while True:
            data = self.client_socket.recv(2048)
            message = data.decode()
            if message == 'exit':
                break

            game_objects = GameObjects()
            self.game_state.update_state(message)

            t1 = Thread(target=self.send_to_clients, args=[data])
            t1.start()

        with self.client_list_lock:
            self.client_list.remove(self.client_socket)

    def send_to_clients(self, data):
        for client in self.client_list:
            if client != self.client_socket:
                client.send(data)