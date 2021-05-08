import time
from random import randint

import pyautogui

from config import LOCAL_PROJECT_PATH


def countdown():
    for i in range(5):
        print(5 - i)
        time.sleep(1)


def reset_camera(actual=False):
    pyautogui.mouseDown()
    generate_delay(200)
    pyautogui.move(0, 500)
    generate_delay(200)
    pyautogui.mouseUp()
    generate_delay(200)
    pyautogui.move(0, -500)
    generate_delay(500)
    pyautogui.mouseDown()
    generate_delay(200)
    pyautogui.move(0, 500)
    generate_delay(200)
    pyautogui.mouseUp()
    generate_delay(500)
    for i in range(21):
        pyautogui.scroll(-1)
    generate_delay(500)
    if actual:
        for i in range(9):
            pyautogui.scroll(1)
    generate_delay(500)


def generate_delay(delay_ms=1000, delay_range=100):
    random_delay = randint(int(delay_ms - delay_range / 2), int(delay_ms + delay_range / 2))
    time.sleep(random_delay / 1000)
    print(f'delayed {random_delay} ms...')


def generate_coords(left, top, width, height):
    x = randint(left + 2, left + width - 2)
    y = randint(top + 2, top + height - 2)
    coords = (x, y)
    return coords


def find_image(file_name, confidence=0.8, grayscale=False, haystackImage=None):
    if haystackImage is None:
        try:
            return pyautogui.locateOnScreen(
                f'{LOCAL_PROJECT_PATH}images\\{file_name}.png',
                confidence=confidence,
                grayscale=grayscale)
        except pyautogui.ImageNotFoundException:
            return None
    else:
        try:
            return pyautogui.locate(
                needleImage=f'{LOCAL_PROJECT_PATH}images\\{file_name}.png',
                haystackImage=haystackImage,
                confidence=confidence,
                grayscale=grayscale
            )
        except pyautogui.ImageNotFoundException:
            return None


def generate_haystack_image():
    center_x = (1152 / 2)
    center_y = (864 / 2)
    left = center_x * .40
    top = center_y * .40
    width = 1152 * .60
    height = 864 * .60
    pyautogui.screenshot('haystack.png', region=(left, top, width, height))
