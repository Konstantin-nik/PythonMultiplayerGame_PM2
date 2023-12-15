import pygame

from src.game.constants.constants import IMAGE_PATH, COLORS, SHAPES, FONT_SIZE, FONT_COLOR, FONT_ALPHA, FONT_NAME

TO_SRC_PATH = ''


class PlayerModel:
    def __init__(self, name, colors):
        font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)  # Font and font size (None for default font)
        self.name = font.render(name, True, FONT_COLOR)
        self.name.set_alpha(FONT_ALPHA)
        self.eyes = pygame.image.load(TO_SRC_PATH + IMAGE_PATH + 'eyes.png').convert_alpha()
        self.head = pygame.image.load(TO_SRC_PATH + IMAGE_PATH + 'head.png').convert_alpha()
        self.hood = pygame.image.load(TO_SRC_PATH + IMAGE_PATH + 'hood.png').convert_alpha()
        self.body = pygame.image.load(TO_SRC_PATH + IMAGE_PATH + 'body.png').convert_alpha()
        self.leg_1 = pygame.image.load(TO_SRC_PATH + IMAGE_PATH + 'leg_1.png').convert_alpha()
        self.leg_2 = pygame.image.load(TO_SRC_PATH + IMAGE_PATH + 'leg_2.png').convert_alpha()
        self.shadow = pygame.image.load(TO_SRC_PATH + IMAGE_PATH + 'shadow.png').convert_alpha()
        self.state_func_dict = {
            0: self.set_0_state,
            100: self.set_100_state,
            101: self.set_101_state,
            102: self.set_102_state,
            103: self.set_103_state,
            200: self.set_200_state,
            201: self.set_201_state,
            202: self.set_202_state,
            203: self.set_203_state,
        }

        self.pos = self.ModelPos()

        self.head_color = colors[0]
        self.body_color = colors[1]
        self.legs_color = colors[2]
        self.reshape()
        self.apply_filters()

    class ModelPos:
        def __init__(self):
            self.shadow_pos = (0, 0)
            self.leg_1_pos = (0, 0)
            self.leg_2_pos = (0, 0)
            self.body_pos = (0, 0)
            self.head_pos = (0, 0)
            self.hood_pos = (0, 0)
            self.eyes_pos = (0, 0)
            self.name_pos = (0, 0)

    def reshape(self):
        self.eyes = pygame.transform.scale(self.eyes, SHAPES['eyes'])
        self.head = pygame.transform.scale(self.head, SHAPES['head'])
        self.hood = pygame.transform.scale(self.hood, SHAPES['hood'])
        self.body = pygame.transform.scale(self.body, SHAPES['body'])
        self.leg_1 = pygame.transform.scale(self.leg_1, SHAPES['legs'])
        self.leg_2 = pygame.transform.scale(self.leg_2, SHAPES['legs'])
        self.shadow = pygame.transform.scale(self.shadow, SHAPES['shadow'])

    def apply_filters(self):
        self.head = self.apply_filter(self.head, self.head_color)
        self.hood = self.apply_filter(self.hood, self.head_color, spec=(-30, -30, -30))
        self.body = self.apply_filter(self.body, self.body_color)
        self.leg_1 = self.apply_filter(self.leg_1, self.legs_color)
        self.leg_2 = self.apply_filter(self.leg_2, self.legs_color)

    def apply_filter(self, image, new_color, *, spec=None):
        new_image = image.copy()
        for x in range(new_image.get_width()):
            for y in range(new_image.get_height()):
                color = self.get_color(new_color, new_image.get_at((x, y))[3])
                if spec is not None:
                    color = (max(min(color[0] + spec[0], 255), 0),
                             max(min(color[1] + spec[1], 255), 0),
                             max(min(color[2] + spec[2], 255), 0),
                             color[3])
                new_image.set_at((x, y), color)
        return new_image

    def draw(self, screen, state, x, y):
        if state == 100:
            self.set_100_state(x, y)
        elif state == 101:
            self.set_101_state(x, y)
        elif state == 102:
            self.set_102_state(x, y)
        else:
            self.set_0_state(x, y)

        screen.blit(self.shadow, self.pos.shadow_pos)
        screen.blit(self.leg_1, self.pos.leg_1_pos)
        screen.blit(self.leg_2, self.pos.leg_2_pos)
        screen.blit(self.body, self.pos.body_pos)
        screen.blit(self.hood, self.pos.hood_pos)
        screen.blit(self.head, self.pos.head_pos)
        screen.blit(self.eyes, self.pos.eyes_pos)
        screen.blit(self.name, self.pos.name_pos)
        pygame.draw.circle(screen, 'black', (x, y), 2)

    def get_color(self, color_num, transparency):
        color = COLORS[color_num]
        return color[0], color[1], color[2], transparency

    def set_0_state(self, x, y):
        self.pos.shadow_pos = (x - SHAPES['shadow'][0]/2, y - SHAPES['shadow'][1]/2)
        self.pos.leg_1_pos = (x - SHAPES['legs'][0]/2, y - SHAPES['legs'][1])
        self.pos.leg_2_pos = self.pos.leg_1_pos
        self.pos.body_pos = (x - SHAPES['body'][0]/2, y - SHAPES['body'][1] - SHAPES['legs'][1]*0.8)
        self.pos.head_pos = (self.pos.body_pos[0] - SHAPES['head'][0]*0.4, self.pos.body_pos[1] - SHAPES['head'][1]*0.36)
        self.pos.hood_pos = self.pos.head_pos
        self.pos.eyes_pos = (self.pos.head_pos[0] + SHAPES['head'][0]*0.1, self.pos.head_pos[1] + SHAPES['head'][1]*0.25)

        name_size = self.name.get_size()
        self.pos.name_pos = (x - name_size[0]/2*1.1, y - name_size[1] - SHAPES['body'][1] - SHAPES['head'][1]*0.9)

    def set_100_state(self, x, y):
        self.set_0_state(x, y)
        self.pos.leg_1_pos = (self.pos.leg_1_pos[0], self.pos.leg_1_pos[1] - SHAPES['legs'][1]*0.3)

    def set_101_state(self, x, y):
        self.set_0_state(x, y)

    def set_102_state(self, x, y):
        self.set_0_state(x, y)
        self.pos.leg_2_pos = (self.pos.leg_2_pos[0], self.pos.leg_2_pos[1] - SHAPES['legs'][1]*0.3)

    def set_103_state(self, x, y):
        self.set_0_state(x, y)
        self.pos.leg_2_pos = (self.pos.leg_2_pos[0], self.pos.leg_2_pos[1] - SHAPES['legs'][1]*0.3)

    def set_200_state(self, x, y):
        pass

    def set_201_state(self, x, y):
        pass

    def set_202_state(self, x, y):
        pass

    def set_203_state(self, x, y):
        pass
