import pyautogui
from config import LOCAL_PROJECT_PATH


def find_image(file_name, confidence=0.8, grayscale=False):
    """
    Custom image finder using PyAutoGui library.
    :param file_name: path to find image (not including \\image)
    :param confidence: confidence level (default=0.8)
    :param grayscale: grayscale active (default=False)
    :return: tuple (or None if exception thrown)
    """
    # TODO: Create AI model that locates images on screen (transparency and resizing)
    try:
        return pyautogui.locateOnScreen(
            f'{LOCAL_PROJECT_PATH}images\\{file_name}.png',
            confidence=confidence,
            grayscale=grayscale)
    except pyautogui.ImageNotFoundException:
        return None
