from socket import socket

import json

from src.client.actions import Action, MoveAction, ShootAction, TalkAction, SpawnAction, JumpAction, Direction
from src.game.constants.constants import WALK_STEP_LENGTH
from src.game.objects.game_object import GameObject
from src.game.objects.player.player import Player


class GameObjects:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if not self._initialized:
            self.objects: list[GameObject] = []
            self.players = {}
            self._initialized = True

    def add_object(self, obj: GameObject):
        self.objects.append(obj)

    def draw(self, screen):
        self.objects = sorted(self.objects)
        for obj in self.objects:
            obj.draw(screen)

    def to_json(self):
        arr = []
        for obj in self.objects:
            arr.append(obj.__dict__())
        return json.dumps(arr)

    def update_objects(self, data: bytes):
        json_data = json.loads(data)

        arr = []
        for d in json_data:
            match d['class_name']:
                case 'player':
                    arr.append(Player.from_json(d))

        self.objects = arr

    def update_game(self, client_socket: socket, action: Action):
        match action:
            case MoveAction():
                match action.direction:
                    case Direction.UP:
                        self.players[client_socket].move(0, -WALK_STEP_LENGTH)
                    case Direction.DOWN:
                        self.players[client_socket].move(0, WALK_STEP_LENGTH)
                    case Direction.LEFT:
                        self.players[client_socket].move(-WALK_STEP_LENGTH, 0)
                    case Direction.RIGHT:
                        self.players[client_socket].move(WALK_STEP_LENGTH, 0)
            case ShootAction():
                pass
                # self.objects.append()
            case TalkAction():
                pass
            case JumpAction():
                self.players[client_socket].jump()
            case SpawnAction():
                pl = Player(name=action.character_name, x=action.x, y=action.y,
                            colors=action.colors, should_render=False)
                self.players[client_socket] = pl
                self.objects.append(pl)
