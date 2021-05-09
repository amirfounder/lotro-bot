import os.path
import pyautogui

from config import LOCAL_PROJECT_PATH, ML_DATA_SCREENSHOT_PATH
from global_helpers.base.generators import generate_date_time


def find_image(file_name, confidence=0.8, grayscale=False):
    """
    Custom image finder using PyAutoGui library.
    :param file_name: path to find image (not including \\image)
    :param confidence: confidence level (default=0.8)
    :param grayscale: grayscale active (default=False)
    :return: tuple (or None if exception thrown)
    """
    # TODO: Create AI model that locates reference_images on screen (transparency and resizing)
    try:
        return pyautogui.locateOnScreen(
            f'{LOCAL_PROJECT_PATH}images\\{file_name}.png',
            confidence=confidence,
            grayscale=grayscale)
    except pyautogui.ImageNotFoundException:
        return None


def take_screenshot(screenshot_name):
    """
    Takes a screenshot for ML training
    :param screenshot_name: name of the screenshot
    :return: void
    """
    time_stamp = f'{generate_date_time("date", ds="")}{generate_date_time("time", ts="")}'
    pyautogui.screenshot(f'{ML_DATA_SCREENSHOT_PATH}\\screenshot_{screenshot_name}_{time_stamp}.png')
