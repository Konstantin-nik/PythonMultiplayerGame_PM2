import json

from src.game.objects.game_object import GameObject

class Bullet(GameObject):
    def __init__(self, x: float, y: float, z: int = 2, should_render: bool = True):
        super().__init__(x, y, z)
        if should_render:
            self.bullet_model = BulletModel(name, colors)

    def __eq__(self, other):
        return (self.name == other.name) and (self.coords == other.coords) and (self.colors == other.colors)

    def draw(self, screen):
        self.player_model.draw(screen, self.state, self.x, self.y)
        self.state.__next__()

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

# if __name__ == '__main__':
# game = GameController()
# game_objects = GameObjects()
# player_1 = Player(name='Super_Stepa', x=game.center.x, y=game.center.y,
#                   colors=(random.sample(range(6), 3)))

# game_objects.add_object(player_1)

# game.run()
