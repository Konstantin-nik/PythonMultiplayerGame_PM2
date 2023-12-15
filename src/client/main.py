import threading
from socket import socket, AF_INET, SOCK_STREAM

from receive_thread import ReceiveThread
from src.client.client_handler import ClientHandler
from src.game.controllers.game_controller import GameController
from src.game.objects.game_objects import GameObjects


def main():
    client_socket = socket(AF_INET, SOCK_STREAM)

    client_socket.connect(("127.0.0.1", 12345))

    _game_objects = GameObjects()
    game_objects_lock = threading.Lock()

    _client_handler = ClientHandler(client_socket=client_socket)

    receive_thread = ReceiveThread(client_socket=client_socket, game_objects_lock=game_objects_lock)
    receive_thread.start()

    game = GameController(game_objects_lock=game_objects_lock)
    game.run()


if __name__ == "__main__":
    main()
