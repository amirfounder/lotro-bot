import os
import random
import time

import config
from bots.generator_bot import GeneratorBot
from bots.interceptor_bot import InterceptorBot
from bots.logger_bot import LoggerBot


class ResetBot:

    log_bot = LoggerBot()
    gen_bot = GeneratorBot()
    int_bot = InterceptorBot()

    def __init__(self, name="ResetBot"):
        self.name = name

    def count_down(self, start_count=5):
        self.log_bot.log_reset(
            'initialize',
            f'Initialized countdown...'
        )
        for i in range(0, start_count):
            self.log_bot.log_reset(
                'progress',
                f'Counting down: {start_count - i}'
            )
            time.sleep(1)
        self.log_bot.log_reset(
            'success',
            f'Success! Bots deployed!'
        )

    def reset_project_pathname(self):
        cwd = os.getcwd()
        index = cwd.index(r'lotro-bot')
        config.PROJECT_DIRECTORY = ''
        for i in range(len(cwd)):
            if i < index + 9:
                config.PROJECT_DIRECTORY += cwd[i]
            else:
                break
        print(config.PROJECT_DIRECTORY)
        self.log_bot.log_reset(
            'success',
            f'Successfully reset project directory to \'{config.PROJECT_DIRECTORY}\''
        )

    def reset_camera_position(self):
        screen_size = self.int_bot.get_screen_size()
        coords = self.gen_bot.generate_coords(
            left=0,
            top=0,
            width=screen_size[0],
            height=screen_size[1],
            x_padding=screen_size[0]*.4,
            y_padding=screen_size[1]*.4
        )
        self.int_bot.move_to(coords, self.gen_bot.generate_duration())
        self.int_bot.right_click()
        self.gen_bot.generate_delay(1000)
        self.int_bot.mouse_down()
        coords = (
            coords[0],
            coords[1] + random.randint(600, 800)
        )
        self.int_bot.move_to(coords)
        self.int_bot.mouse_up()
        coords = (
            coords[0] + random.randint(-50, 50),
            coords[0] - random.randint(600, 800)
        )
        self.int_bot.move_to(coords, self.gen_bot.generate_duration())
        self.int_bot.mouse_down()
        coords = (
            coords[0],
            coords[1] + random.randint(600, 800)
        )
        self.int_bot.move_to(coords)
        self.int_bot.mouse_up()

    def reset_camera_scroll(self):
        self.int_bot.scroll('out', 21)
        self.int_bot.scroll('in', 5)

