import config
from bots.util_bots.generation_bot import GenerationBot
from bots.util_bots.imaging_bot import ImagingBot
from bots.util_bots.interception_bot import InterceptionBot
from bots.util_bots.logging_bot import LoggingBot


class InteractionBot:
    intercept = InterceptionBot()
    log = LoggingBot()
    generate = GenerationBot()
    image = ImagingBot()

    def __init__(self):
        self.log.log_interaction('initialized', 'INTERACTION_BOT built and deployed...')

    def move_mouse_and_click(self, box, button='left', x_padding=3, y_padding=3):
        coords = self.generate.generate_coords(box[0], box[1], box[2], box[3], x_padding, y_padding)
        self.intercept.move_to(coords, self.generate.generate_duration())
        if button == 'left':
            self.intercept.click()
        elif button == 'right':
            self.intercept.right_click()
        else:
            self.log.log_crafting('error',
                                  f'invalid button parameter {button}. please use values, \'left\' or \'right\'')

    def click_button(self, button):
        path = f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\buttons'
        filename = f'{button}.png'
        box = self.intercept.find_image(path, filename, 0.9)
        if box is None:
            self.log.log_crafting('error', f'unable to find the button, {button}')
            return
        self.log.log_crafting('success', f'clicked the {button} button')
        self.move_mouse_and_click(box)

    def toggle(self, path, target, t_type, image_confidence):
        filename = f'{target}.png'
        filename_toggled = f'{target}_toggled.png'
        box = self.intercept.find_image(path, filename_toggled, image_confidence)
        if box is not None:
            self.log.log_crafting('info', f'{target} {t_type} already toggled')
            return
        box = self.intercept.find_image(path, filename, image_confidence)
        if box is None:
            self.log.log_crafting('error', f'unable to find {target} {t_type}')
            return
        self.log.log_crafting('success', f'successfully located {target} {t_type}')
        self.move_mouse_and_click(box)
