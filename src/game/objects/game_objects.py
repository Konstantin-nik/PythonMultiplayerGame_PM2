from src.game.objects.game_object import GameObject


class GameObjects:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__init__(cls)
        return cls._instance

    def __init__(self):
        self.objects = []

    def draw(self):
        for obj in self.objects:
            obj.draw()

    def add_object(self, obj: GameObject):
        self.objects.append(obj)
