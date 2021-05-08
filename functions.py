import time
from random import randint

import pyautogui

from config import LOCAL_PROJECT_PATH


def countdown():
    for i in range(5):
        print(5 - i)
        time.sleep(1)


def reset_camera():
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


def generate_delay(delay_ms=1000, delay_range=100):
    random_delay = randint(int(delay_ms - delay_range / 2), int(delay_ms + delay_range / 2))
    time.sleep(random_delay / 1000)
    print(f'delayed {random_delay} ms...')


def generate_coords(left, top, width, height):
    x = randint(left + 2, left + width - 2)
    y = randint(top + 2, top + height - 2)
    coords = (x, y)
    return coords


def find_image(file_name, confidence=0.8):
    try:
        return pyautogui.locateOnScreen(
            f'{LOCAL_PROJECT_PATH}images\\{file_name}.png',
            confidence=confidence)
    except pyautogui.ImageNotFoundException:
        return None
