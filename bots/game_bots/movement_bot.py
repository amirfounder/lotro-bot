from bots.util_bots.generator_bot import GeneratorBot
from bots.util_bots.interceptor_bot import InterceptorBot
from bots.util_bots.logger_bot import LoggerBot


class MovementBot:

    log_bot = LoggerBot()
    int_bot = InterceptorBot()
    gen_bot = GeneratorBot()

    def __init__(self):
        self.log_bot.log_movement('initialized', 'movement_bot built and deployed...')

    def move(self, direction, duration):
        self.int_bot.key_down(direction)
        self.gen_bot.generate_delay(duration, 50)
        self.int_bot.key_up(direction)

    def rotate(self, direction, deg):
        self.int_bot.key_down(direction)
        self.gen_bot.generate_delay(int(deg * 6.21), 50)
        self.int_bot.key_up(direction)

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
        self.int_bot.press('space')
