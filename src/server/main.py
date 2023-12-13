from socket import socket, AF_INET, SOCK_STREAM
import threading

from src.server.client_thread import ClientThread
from src.game.objects import GameObjects


clients: list[socket] = []
client_list_lock = threading.Lock()

def main():
    server_address = ("127.0.0.1", 12345)
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(server_address)
    print("Server started")

    game_objects_lock = threading.Lock()

    while True:
        server.listen(1)
        client_socket, client_address = server.accept()
        with client_list_lock:
            clients.append(client_socket)

        print("New connection added: ", client_address)
        client_thread = ClientThread(client_address, client_socket, clients, client_list_lock, game_objects_lock)
        client_thread.start()

if __name__ == '__main__':
    main()