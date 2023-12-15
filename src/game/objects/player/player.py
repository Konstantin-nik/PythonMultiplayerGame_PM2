import random

from src.game.controllers.game_controller import GameController
from src.game.objects.game_object import GameObject
from src.game.objects.game_objects import GameObjects
from src.game.objects.player.player_model import PlayerModel
from src.game.objects.player.player_state import PlayerState


class Player(GameObject):
    def __init__(self, name: str, colors: tuple[int, int, int], x: float, y: float, z: int = 2):
        super().__init__(x, y, z)
        self.name = name
        self.colors = colors
        self.player_model = PlayerModel(name, colors)
        self.state = PlayerState()

    def __eq__(self, other):
        return (self.name == other.name) and (self.coords == other.coords) and (self.colors == other.colors)

    def draw(self, screen):
        self.player_model.draw(screen, self.state, self.x, self.y)



if __name__ == '__main__':
    game = GameController()
    game_objects = GameObjects()
    game_objects.init()
    player_1 = Player(name='Super_Stepa', x=game.center.x, y=game.center.y,
                      colors=(random.sample(range(6), 3)))

    game_objects.add_object(player_1)

    game.run()
