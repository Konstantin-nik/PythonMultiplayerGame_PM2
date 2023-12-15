from socket import socket

import yaml

from src.client.actions import Action, MoveAction, ShootAction, TalkAction
from src.game.objects.game_object import GameObject


class GameObjects:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def init(self):
        self.objects: list[GameObject] = []

    def add_object(self, obj: GameObject):
        self.objects.append(obj)

    def draw(self, screen):
        self.objects = sorted(self.objects)
        for obj in self.objects:
            obj.draw(screen)

    def update_objects(self, data: bytes):
        yaml_data = yaml.safe_load(data)
        self.objects = [GameObject(**game_object) for game_object in yaml_data]

    def update_game(self, client_socket: socket, action: Action):
        player = filter(lambda obj: obj)
        match action:
            case MoveAction():
                pass
            case ShootAction():
                pass
            case TalkAction():
                pass
