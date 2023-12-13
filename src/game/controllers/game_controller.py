import pygame

from src.game.constants.constants import START_WINDOW_WIDTH, START_WINDOW_HEIGHT
from src.game.objects.game_objects import GameObjects


class GameController:
    def __init__(self, size=(START_WINDOW_WIDTH, START_WINDOW_HEIGHT), ticks=60):
        super().__init__()
        pygame.init()

        self.width = size[0]
        self.height = size[1]
        self.center = pygame.Vector2(self.width//2, self.height//2)

        # pygame setting
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Rotating Circle")
        self.clock = pygame.time.Clock()
        self.running = True
        self.ticks = ticks

    def run(self):
        while self.running:

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # clean screen
            self.screen.fill('black')

            # draw scene background
            self.draw_map()

            # draw everything
            self.draw_objects()

            # apply filter on final screen
            self.apply_screen_filter()

            pygame.display.flip()
            self.clock.tick(self.ticks)

        pygame.quit()

    def draw_map(self):
        """
        Draws background.
        :return:
        """
        pass

    def draw_objects(self):
        """
        Draws all objects.
        :return:
        """
        game_objects = GameObjects()
        game_objects.draw()

    def apply_screen_filter(self):
        """
        Applies filter on the screen.
        :return:
        """
        pass

