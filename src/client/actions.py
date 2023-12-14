from enum import Enum

import yaml


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def to_yaml_rep(self) -> str:
        return self.value

    @classmethod
    def from_yaml_repr(cls, data: str) -> 'Direction':
        return cls(data)


class Action:
    name = ''

    @classmethod
    def from_yaml(cls, data: bytes) -> 'Action':
        yaml_data = yaml.safe_load(data)
        action_name = yaml_data.get('name')

        for subclass in cls.__subclasses__():
            if subclass.name == action_name:
                return subclass.from_yaml_data(yaml_data)

        raise ValueError(f"Unknown action: {action_name}")

    @classmethod
    def from_yaml_data(cls, data: dict):
        raise NotImplementedError("This method should be implemented in subclasses.")

    def to_yaml(self) -> bytes:

        return yaml.dump({'name': self.name} | self.__dict__).encode()


class MoveAction(Action):
    name = 'Move'

    def __init__(self, direction: Direction):
        super().__init__()
        self.direction = direction

    @classmethod
    def from_yaml_data(cls, data: dict):
        return cls(direction=Direction.from_yaml_repr(data['direction']))

    def to_yaml(self) -> bytes:
        return yaml.dump({'name': self.name, 'direction': self.direction.to_yaml_rep()}).encode()


class ShootAction(Action):
    name = 'Shoot'

    def __init__(self, angle: float):
        self.angle = angle

    @classmethod
    def from_yaml_data(cls, data: dict):
        return cls(angle=data['angle'])


class TalkAction(Action):
    name = 'Talk'

    def __init__(self, npc_id: str, message: str):
        self.npc_id = npc_id
        self.message = message

    @classmethod
    def from_yaml_data(cls, data: dict):
        return cls(npc_id=data['npc_id'], message=data['message'])
