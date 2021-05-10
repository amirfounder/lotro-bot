import os

from bots.util_bots.interceptor_bot import InterceptorBot


class ImageBot:
    int_bot = InterceptorBot()

    def __init__(self, name='ImageBot'):
        self.name = name

    def find_images_from_directory(self, path, confidence=0.8, grayscale=False):
        for filename in os.listdir(path):
            image = self.int_bot.find_image(
                path=path,
                filename=filename,
                confidence=confidence,
                grayscale=grayscale
            )
            if image is not None:
                break
        return image
