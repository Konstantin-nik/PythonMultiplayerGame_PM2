from enum import Enum

import json


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def to_json_rep(self) -> str:
        return self.value

    @classmethod
    def from_json_repr(cls, data: str) -> 'Direction':
        return cls(data)


class Action:
    name = ''

    @classmethod
    def from_json(cls, data: bytes) -> 'Action':
        json_data = json.loads(data)
        action_name = json_data.get('name')

        for subclass in cls.__subclasses__():
            if subclass.name == action_name:
                return subclass.from_json_data(json_data)

        raise ValueError(f"Unknown action: {action_name}")

    @classmethod
    def from_json_data(cls, data: dict):
        raise NotImplementedError("This method should be implemented in subclasses.")

    def to_json(self) -> bytes:
        return json.dumps({'name': self.name} | self.__dict__).encode()


class MoveAction(Action):
    name = 'Move'

    def __init__(self, direction: Direction):
        super().__init__()
        self.direction = direction

    @classmethod
    def from_json_data(cls, data: dict):
        return cls(direction=Direction.from_json_repr(data['direction']))

    def to_json(self) -> bytes:
        return json.dumps({'name': self.name, 'direction': self.direction.to_json_rep()}).encode()


class ShootAction(Action):
    name = 'Shoot'

    def __init__(self, angle: float):
        self.angle = angle

    @classmethod
    def from_json_data(cls, data: dict):
        return cls(angle=data['angle'])


class TalkAction(Action):
    name = 'Talk'

    def __init__(self, npc_id: str, message: str):
        self.npc_id = npc_id
        self.message = message

    @classmethod
    def from_json_data(cls, data: dict):
        return cls(npc_id=data['npc_id'], message=data['message'])


class SpawnAction(Action):
    name = 'Spawn'

    def __init__(self, character_name: str, x, y, colors):
        self.character_name = character_name
        self.x = x
        self.y = y
        self.colors = colors

    @classmethod
    def from_json_data(cls, data: dict):
        return cls(character_name=data['character_name'], x=data['x'], y=data['y'], colors=data['colors'])

    def to_json(self) -> bytes:
        return json.dumps({'name': self.name} | self.__dict__).encode()


class JumpAction(Action):
    name = 'Jump'

    @classmethod
    def from_json_data(cls, data: dict):
        return cls()

    def to_json(self):
        return json.dumps({'name': self.name}).encode()