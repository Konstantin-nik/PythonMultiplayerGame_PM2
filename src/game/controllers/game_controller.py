import random
from threading import Thread, Lock

import pygame

from src.common.actions import MoveAction, Direction, SpawnAction, ShootAction, JumpAction
from src.client.client_handler import ClientHandler
from src.game.constants.constants import START_WINDOW_WIDTH, START_WINDOW_HEIGHT, TICKS
from src.game.objects.game_objects import GameObjects


class GameController(Thread):
    def __init__(self, *, game_objects_lock: Lock, size=(START_WINDOW_WIDTH, START_WINDOW_HEIGHT), ticks=TICKS,
                 user='client'):
        super().__init__()
        pygame.init()

        self.user = user

        self.game_objects_lock = game_objects_lock

        self.width = size[0]
        self.height = size[1]
        self.center = pygame.Vector2(self.width // 2, self.height // 2)

        # pygame setting
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Multiplayer Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.ticks = ticks

        # spawn a player

        if user == 'client':
            client_handler = ClientHandler()
            player_name = input("Enter your name: ")
            client_handler.send(SpawnAction(character_name=player_name, x=random.randint(100, 500), y=self.center.y,
                                            colors=(random.sample(range(6), 3))))

    def run(self):
        while self.running:
            if self.user == 'client':
                client_handler = ClientHandler()
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if self.user == 'client':
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                            client_handler.send(MoveAction(Direction.UP))
                        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            client_handler.send(MoveAction(Direction.LEFT))
                        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                            client_handler.send(MoveAction(Direction.DOWN))
                        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            client_handler.send(MoveAction(Direction.RIGHT))
                        elif event.key == pygame.K_SPACE:
                            client_handler.send(JumpAction())
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        click_position = pygame.mouse.get_pos()
                        client_handler.send(ShootAction(click_position))

            # clean screen
            self.screen.fill('white')

            # draw scene background
            self.draw_map()

            # draw everything
            self.draw_objects()

            # apply filter on final screen
            self.apply_screen_filter()

            pygame.display.flip()
            self.clock.tick(self.ticks)

        pygame.quit()
        client_handler = ClientHandler()
        client_handler.close()

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
        with self.game_objects_lock:
            game_objects = GameObjects()
            game_objects.draw(self.screen)
        # game_objects = GameObjects()
        # game_objects.draw(self.screen)

    def apply_screen_filter(self):
        """
        Applies filter on the screen.
        :return:
        """
        pass
