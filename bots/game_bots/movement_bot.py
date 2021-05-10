from bots.util_bots.generation_bot import GenerationBot
from bots.util_bots.interception_bot import InterceptionBot
from bots.util_bots.logging_bot import LoggingBot


class MovementBot:
    log = LoggingBot()
    intercept = InterceptionBot()
    generate = GenerationBot()

    def __init__(self):
        self.log.log_movement('initialized', 'MOVEMENT_BOT built and deployed...')

    def move(self, direction, duration):
        self.intercept.key_down(direction)
        self.generate.generate_delay(duration, 50)
        self.intercept.key_up(direction)

    def rotate(self, direction, deg):
        self.intercept.key_down(direction)
        self.generate.generate_delay(int(deg * 6.21), 50)
        self.intercept.key_up(direction)

    def move_forward(self, duration):
        self.move('e', duration)

    def move_backward(self, duration):
        self.move('d', duration)

    def strafe_left(self, duration):
        self.move('a', duration)

    def strafe_right(self, duration):
        self.move('g', duration)

    def rotate_left(self, deg):
        self.rotate('s', deg)

    def rotate_right(self, deg):
        self.rotate('f', deg)

    def jump(self):
        self.intercept.press('space')
