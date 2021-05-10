import os

import config
from bots.util_bots.generator_bot import GeneratorBot
from bots.util_bots.interceptor_bot import InterceptorBot
from bots.util_bots.logger_bot import LoggerBot


class InteractionBot:

    int_bot = InterceptorBot()
    log_bot = LoggerBot()
    gen_bot = GeneratorBot()

    def __init__(self):
        print(f'started the InteractionBot in directory: {os.getcwd()}')

    def move_click(self, box, button='left'):
        coords = self.gen_bot.generate_coords(box[0], box[1], box[2], box[3], 3, 3)
        self.int_bot.move_to(coords, self.gen_bot.generate_duration())
        if button == 'left':
            self.int_bot.click()
        elif button == 'right':
            self.int_bot.right_click()
        else:
            self.log_bot.log_crafter('error',
                                     f'invalid button parameter {button}. please use values, \'left\' or \'right\'')

    def click_button(self, button):
        path = f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\buttons'
        filename = f'{button}.png'

        box = self.int_bot.find_image(path, filename, 0.9)
        if box is None:
            self.log_bot.log_crafter('error', f'unable to find the button, {button}')
            return
        self.log_bot.log_crafter('success', f'clicked the {button} button')
        self.move_click(box)

    def toggle(self, path, target, t_type, image_confidence):
        filename = f'{target}.png'
        filename_toggled = f'{target}_toggled.png'

        box = self.int_bot.find_image(path, filename_toggled, image_confidence)
        if box is not None:
            self.log_bot.log_crafter('info', f'{target} {t_type} already toggled')
            return
        box = self.int_bot.find_image(path, filename, image_confidence)
        if box is None:
            self.log_bot.log_crafter('error', f'unable to find {target} {t_type}')
            return

        self.log_bot.log_crafter('success', f'successfully located {target} {t_type}')
        self.move_click(box)
