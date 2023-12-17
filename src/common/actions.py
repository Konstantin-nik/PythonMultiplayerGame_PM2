from enum import Enum

import json


def is_action(name):
    global actions_list
    return name in actions_list


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
    NAME = 'Action'

    @classmethod
    def from_json(cls, json_str: str):
        return json.loads(json_str, object_hook=cls.from_dict)

    @classmethod
    def from_dict(cls, dictionary: dict):
        raise NotImplementedError("This method should be implemented in subclasses.")

    def to_json(self):
        return json.dumps({'name': self.NAME} | self.__dict__)


class MoveAction(Action):
    NAME = 'MoveAction'

    def __init__(self, direction: Direction):
        super().__init__()
        self.direction = direction

    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(
            direction=Direction.from_json_repr(dictionary['direction'])
        )

    def to_json(self):
        return json.dumps({'name': self.NAME, 'direction': self.direction.to_json_rep()})


class ShootAction(Action):
    NAME = 'ShootAction'

    def __init__(self, angle: float):
        self.angle = angle

    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(
            angle=dictionary['angle']
        )


class TalkAction(Action):
    NAME = 'TalkAction'

    def __init__(self, npc_id: str, message: str):
        self.npc_id = npc_id
        self.message = message

    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(
            npc_id=dictionary['npc_id'],
            message=dictionary['message']
        )


class SpawnAction(Action):
    NAME = 'SpawnAction'

    def __init__(self, character_name: str, x, y, colors):
        self.character_name = character_name
        self.x = x
        self.y = y
        self.colors = colors

    @classmethod
    def from_dict(cls, dictionary):
        return cls(
            character_name=dictionary['character_name'],
            x=dictionary['x'],
            y=dictionary['y'],
            colors=dictionary['colors']
        )

    def to_json(self):
        return json.dumps({'name': self.NAME} | self.__dict__)


class JumpAction(Action):
    NAME = 'JumpAction'

    @classmethod
    def from_dict(cls, dictionary):
        return cls()

    def to_json(self):
        return json.dumps({'name': self.NAME})


actions_list = [
    Action.NAME, MoveAction.NAME, ShootAction.NAME, SpawnAction.NAME, JumpAction.NAME, TalkAction.NAME,
]
