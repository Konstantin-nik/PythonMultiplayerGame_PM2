START_WINDOW_WIDTH = 1200
START_WINDOW_HEIGHT = 800

PORT = 12340

TICKS = 60

IMAGE_PATH = 'src/assets/3x/'

COLORS = [
    (221, 36, 39),  # red
    (66, 90, 168),  # d_blue
    (209, 89, 161),  # magenta
    (255, 202, 28),  # yellow
    (113, 191, 68),  # green
    (115, 204, 214),  # l_blue
]

SCALE_PARAM = 0.6

FONT_SIZE = max(int(36*SCALE_PARAM), 22)
FONT_NAME = 'Verdana'
FONT_COLOR = (66, 90, 198)
FONT_ALPHA = 180    # from 0 to 255


def scale(t):
    return tuple(value * SCALE_PARAM for value in t)


SHAPES = {
    'eyes': scale((50, 16)),
    'head': scale((100, 111)),
    'hood': scale((100, 111)),
    'body': scale((150, 140)),
    'legs': scale((120, 37)),
    'shadow': scale((175, 37)),
    'bullet': scale((25, 10))
}

# states timers
WALK_TIME = 0.3
WALK_STATES = 3
WALK_FRAMES_NUM = TICKS * WALK_TIME // WALK_STATES

WALK_STEP_LENGTH = 20

# states
STATES = {
    'walk': 100,
    'jump': 200
}
