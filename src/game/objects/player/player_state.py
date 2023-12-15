from src.game.constants.constants import WALK_FRAMES_NUM, STATES


class PlayerState:
    def __init__(self, state: int = 0):
        self.state = state
        self.state_flow = {
            # basic state player stands still, start pos of all other flows
            0: (0, 0),

            # walk states
            100: self.State(WALK_FRAMES_NUM, 101),
            101: self.State(WALK_FRAMES_NUM, 102),
            102: self.State(WALK_FRAMES_NUM, 103),
            103: self.State(WALK_FRAMES_NUM, 0),

            # jump states
            200: self.State(0, 201),
            201: self.State(0, 202),
            202: self.State(0, 203),
            203: self.State(0, 0),
        }
        self.current_score = 0

    class State:
        def __init__(self, frames, next_state):
            self.frames = frames
            self.next_state = next_state

    def __iter__(self):
        return self

    def __next__(self):
        if self.state == 0:
            return self.state

        if self.current_score == self.state_flow[self.state].frames:
            self.current_score = 0
            self.state = self.state_flow[self.state].next_state
        else:
            self.current_score += 1

        return self.state

    def __eq__(self, other):
        return self.state == other

    def set_state(self, state_name):
        if self.state != 0:
            return

        self.state = STATES.get(state_name)
