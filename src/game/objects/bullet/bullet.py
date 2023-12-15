import json

import pygame

from src.game.constants.constants import SHAPES, IMAGE_PATH
from src.game.objects.game_object import GameObject

class Bullet(GameObject):
    def __init__(self, x: float, y: float, target_pos: (float, float), z: float = 2, should_render: bool = True):
        super().__init__(x, y, 2)

        self.bullet_img = pygame.image.load(IMAGE_PATH + 'bullet.png').convert_alpha()
        self.bullet_img = pygame.transform.scale(self.bullet_img, SHAPES['bullet'])

    def draw(self, screen):
        screen.blit(self.bullet_img, (self.x, self.y))

    def __dict__(self):
        return {
            'class_name': 'bullet',
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'target_pos': self.target_pos,
        }

    @classmethod
    def from_json(cls, dictionary):
        return cls(x=dictionary['x'], y=dictionary['y'], z=dictionary['z'],
                   target_pos=dictionary['target_pos'])
