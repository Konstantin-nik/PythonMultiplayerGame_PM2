from socket import socket

import yaml

from src.game.objects.game_object import GameObject


class Player(GameObject):
    def __init__(self, client_socket: socket, name: str, colors, x: float, y: float, z: int):
        super().__init__(x, y, z)
        self.client_socket = client_socket
        self.name = name
        self.colors = colors

    def __eq__(self, other):
        return (self.name == other.name) and (self.coords == other.coords) and (self.colors == other.colors)


player_1 = Player(name='Petya', coords=(10, 9), colors=(1, 0, 3))

yaml_string = yaml.dump(player_1.__dict__)
print(yaml_string)

yaml_data = yaml.full_load(yaml_string)
player_2 = Player(**yaml_data)
print(player_1 == player_2)
