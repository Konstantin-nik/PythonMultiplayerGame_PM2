import threading
from socket import socket, AF_INET, SOCK_STREAM

from src.game.constants.constants import PORT
from src.game.controllers.game_controller import GameController
from src.server.client_thread import ClientThread


def main():
    server_address = ("0.0.0.0", PORT)
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(server_address)
    print("Server started")

    clients: list[socket] = []
    client_list_lock = threading.Lock()

    game_objects_lock = threading.Lock()

    threading.Thread(target=listening_for_clients, args=[server, clients, client_list_lock, game_objects_lock]).start()

    game = GameController(game_objects_lock=game_objects_lock, user='server')
    game.run()


def listening_for_clients(server, clients, client_list_lock, game_objects_lock):
    while True:
        server.listen(1)
        client_socket, client_address = server.accept()
        with client_list_lock:
            clients.append(client_socket)
        print(f"Client at {client_address} connected")
        client_thread = ClientThread(client_socket=client_socket, client_list=clients,
                                     client_list_lock=client_list_lock,
                                     game_objects_lock=game_objects_lock)
        client_thread.start()


if __name__ == '__main__':
    main()
