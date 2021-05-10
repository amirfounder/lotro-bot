import pyautogui
import pydirectinput

from bots.util_bots.logger_bot import LoggerBot


# noinspection PyBroadException


class InterceptorBot:
    log_bot = LoggerBot()

    def __init__(self, name="InterceptorBot"):
        self.name = name

    # PyAutoGui Stuff

    # Utils

    def get_mouse_position(self):
        pos = pyautogui.position()
        self.log_bot.log_interceptor(
            'success',
            f'successfully returned the current mouse position ({pos[0]}, {pos[1]})'
        )
        return pos

    def get_screen_size(self):
        size = pyautogui.size()
        self.log_bot.log_interceptor(
            'success',
            f'successfully returned the size of the current screen ({size[0]}, {size[1]})'
        )
        return size

    def screenshot(self, destination=None):
        ss = pyautogui.screenshot()
        self.log_bot.log_interceptor(
            'success',
            f'successfully captured a screenshot'
        )
        if destination is None:
            return ss
        else:
            ss.save(destination)
            self.log_bot.log_interceptor('success', f'successfully saved the screenshot to {destination}')

    # Mouse stuff

    def move(self, x_offset=0, y_offset=0, duration=0.0):
        pyautogui.move(
            xOffset=x_offset,
            yOffset=y_offset,
            duration=duration
        )
        self.log_bot.log_interceptor(
            'success',
            f'successfully moved mouse an x offset of {x_offset} and y offset of {y_offset} and duration of {duration} seconds'
        )

    def move_to(self, coords, duration=0):
        pyautogui.moveTo(
            x=coords[0],
            y=coords[1],
            duration=duration
        )
        self.log_bot.log_interceptor(
            'success',
            f'successfully moved mouse to ({coords[0]}, {coords[1]}) over a duration of {duration} seconds'
        )

    def click(self, coords=None):
        """
        Performs a left click on the passed coordinates
        :param coords: a coordiante tuple (x=x, y=y)
        :return: void
        """
        message = f'successfully left-clicked'
        if coords is None:
            pyautogui.click()
        else:
            pyautogui.click(
                x=coords[0],
                y=coords[1]
            )
            message += f' on ({coords[0]}, {coords[1]})'
        self.log_bot.log_interceptor(
            'success',
            message
        )

    def right_click(self, coords=None):
        message = f'successfully right-clicked'
        if coords is None:
            pyautogui.click(
                button='right'
            )
        else:
            pyautogui.click(
                x=coords[0],
                y=coords[1],
                button='right'
            )
            message += f'on ({coords[0]}, {coords[1]})'
        self.log_bot.log_interceptor(
            'success',
            message
        )

    def mouse_down(self):
        pyautogui.mouseDown()
        self.log_bot.log_interceptor(
            'success',
            'successfully performed the mouse down operation'
        )

    def mouse_up(self):
        pyautogui.mouseUp()
        self.log_bot.log_interceptor(
            'success',
            'successfully performed the mouse up operation'
        )

    def scroll(self, direction_param, count=1):
        if direction_param.lower() == 'in':
            direction = 1
        elif direction_param.lower() == 'out':
            direction = -1
        else:
            self.log_bot.log_interceptor(
                'error',
                f'the scroll direction specified, \'{direction_param}\' is unavailable. please use \'in\' or \'out\' '
                f'for the direction parameter '
            )
            return
        for i in range(count):
            pyautogui.scroll(direction)
        self.log_bot.log_interceptor(
            'success',
            f'successfully scrolled {direction_param} {count} scroll-clicks'
        )

    def drag(self, x_offset=None, y_offset=None, duration=0.0):
        pyautogui.drag(
            x_offset=x_offset,
            y_offset=y_offset,
            duration=duration
        )
        self.log_bot.log_interceptor(
            'success',
            f'successfully dragged mouse an x offset of {x_offset} and y offset of {y_offset} for a duration of {duration} '
        )

    def find_image(self, path, filename, confidence=0.8, grayscale=False):
        box = pyautogui.locateOnScreen(
            f'{path}\\{filename}',
            confidence=confidence,
            grayscale=grayscale,
        )
        if box is None:
            self.log_bot.log_interceptor(
                'error',
                f'could not find \'{filename}\' on screen'
            )
            return box
        else:
            self.log_bot.log_interceptor(
                'success',
                f'successfully located the image {filename} on screen'
            )
            return box

    def press(self, key):
        pydirectinput.press(key)
        self.log_bot.log_interceptor(
            'success',
            f'successfully pressed the {key} character on the keyboard'
        )

    def key_down(self, key):
        pydirectinput.keyDown(key)
        self.log_bot.log_interceptor(
            'success',
            f'pressed the {key} key down'
        )

    def key_up(self, key):
        pydirectinput.keyUp(key)
        self.log_bot.log_interceptor(
            'success',
            f'released the {key} key'
        )
