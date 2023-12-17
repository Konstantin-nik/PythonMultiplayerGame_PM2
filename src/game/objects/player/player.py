import json

from src.game.objects.game_object import GameObject
from src.game.objects.player.player_model import PlayerModel
from src.game.objects.player.player_state import PlayerState


class Player(GameObject):
    def __init__(self, name: str, colors: tuple[int, int, int], x: float, y: float, z: int = 2,
                 should_render: bool = True, state: int = 0):
        super().__init__(x, y, z)
        self.name = name
        self.colors = colors
        if should_render:
            path = ''
        else:
            path = '../../'
        self.player_model = PlayerModel(name, colors, path)
        self.state = PlayerState(state)

    def __eq__(self, other):
        return (self.name == other.name) and (self.coords == other.coords) and (self.colors == other.colors)

    def draw(self, screen):
        self.player_model.draw(screen, self.state, self.x, self.y)
        self.state.__next__()

    def jump(self):
        self.state.set_state('jump')

    def set_state(self, state_name):
        self.state.set_state(state_name)

    def __dict__(self):
        return {
            'class_name': 'player',
            'name': self.name,
            'colors': self.colors,
            'state': self.state.state,
            'x': self.x,
            'y': self.y,
            'z': self.z,
        }

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y
        self.state.set_state('walk')

    @classmethod
    def from_json(cls, dictionary):
        return cls(name=dictionary['name'], colors=dictionary['colors'], x=dictionary['x'], y=dictionary['y'],
                   z=dictionary['z'], state=dictionary['state'])