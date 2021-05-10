import os

from bots.util_bots.generation_bot import GenerationBot
from bots.util_bots.interception_bot import InterceptionBot
from bots.util_bots.logging_bot import LoggingBot


class ImagingBot:
    intercept = InterceptionBot()
    generate = GenerationBot()
    log = LoggingBot()

    def __init__(self, name='ImageBot'):
        self.name = name

    def find_images_from_directory(self, path, confidence=0.9, grayscale=False):
        for filename in os.listdir(path):
            image = self.intercept.find_image(path, filename, confidence, grayscale)
            if image is not None:
                self.log.log_imaging('success', f'Located {filename} image on screen')
                return image
            else:
                self.log.log_imaging('warning', f'Could not locate {filename} image on screen yet...')
            self.generate.generate_delay()
        self.log.log_imaging('error', f'Could not locate {filename} image on screen')
        return None
