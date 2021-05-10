import random
import time

from bots.util_bots.generation_bot import GenerationBot
from bots.util_bots.interception_bot import InterceptionBot
from bots.util_bots.logging_bot import LoggingBot


class ResetBot:
    log = LoggingBot()
    generate = GenerationBot()
    intercept = InterceptionBot()

    def __init__(self):
        self.log.log_reset('initialized', 'RESET_BOT built and deployed...')

    def count_down(self, start_count=5):
        """
        Countdown to immense at the beginning of each script run
        :param start_count: The number from which to start (default=5)
        :return: Void
        """
        self.log.log_reset('initialize', f'Initialized countdown...')
        for i in range(0, start_count):
            self.log.log_reset('progress', f'Counting down: {start_count - i}')
            time.sleep(1)
        self.log.log_reset('success', f'Success! Bots deployed!')

    def reset_mouse_position(self):
        """
        Resets the mouse position to the center 10% of the target screen
        :return: Tuple (x, y)
        """
        screen_size = self.intercept.get_screen_size()
        coords = self.generate.generate_coords(
            left=0,
            top=0,
            width=screen_size[0],
            height=screen_size[1],
            x_padding=screen_size[0] * .4,
            y_padding=screen_size[1] * .4
        )
        self.intercept.move_to(coords, self.generate.generate_duration())
        self.intercept.right_click()
        self.generate.generate_delay(1000)
        self.log.log_reset('success', f'Reset mouse position to ({coords[0]}, {coords[1]})')
        return coords

    def reset_camera_position(self):
        """
        Resets the camera position to bird view
        :return: Void
        """
        coords = self.reset_mouse_position()
        self.intercept.mouse_down()
        coords = (coords[0], coords[1] + random.randint(600, 800))
        self.intercept.move_to(coords)
        self.intercept.mouse_up()
        coords = (coords[0] + random.randint(-50, 50), coords[0] - random.randint(600, 800))
        self.intercept.move_to(coords, self.generate.generate_duration())
        self.intercept.mouse_down()
        coords = (coords[0], coords[1] + random.randint(600, 800))
        self.intercept.move_to(coords)
        self.intercept.mouse_up()
        self.log.log_reset('success', 'Reset camera position to bird view')

    def reset_camera_scroll(self):
        """
        Resets the camera scroll
        :return: Void
        """
        self.intercept.scroll('out', 21)
        self.intercept.scroll('in', 5)
        self.log.log_reset('success', 'Reset camera scroll')
