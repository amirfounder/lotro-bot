import pyautogui
import pydirectinput

from bots.util_bots.logging_bot import LoggingBot


class InterceptionBot:
    log = LoggingBot()

    def __init__(self):
        self.log.log_interception('initialized', 'INTERCEPTION_BOT built and deployed...')

    def get_mouse_position(self):
        pos = pyautogui.position()
        self.log.log_interception('success', f'returned the current mouse position ({pos[0]}, {pos[1]})')
        return pos

    def get_screen_size(self):
        size = pyautogui.size()
        self.log.log_interception('success', f'returned the size of the current screen ({size[0]}, {size[1]})')
        return size

    def screenshot(self, destination=None):
        ss = pyautogui.screenshot()
        if destination is None:
            self.log.log_interception('success', 'Captured a screenshot')
            return ss
        else:
            ss.save(destination)
            self.log.log_interception('success', f'Captured and saved a screenshot to {destination}')

    def move(self, x_offset=0, y_offset=0, duration=0.0):
        pyautogui.move(
            xOffset=x_offset,
            yOffset=y_offset,
            duration=duration
        )
        self.log.log_interception('success',
                                      f'moved mouse an offset of ({x_offset}, {y_offset}) over duration of {duration} seconds')

    def move_to(self, coords, duration=0):
        pyautogui.moveTo(
            x=coords[0],
            y=coords[1],
            duration=duration
        )
        self.log.log_interception('success',
                                      f'moved mouse to ({coords[0]}, {coords[1]}) over a duration of {duration} seconds')

    def click(self, coords=None):
        message = f'Performed left-click'
        if coords is None:
            pydirectinput.click()
        else:
            pydirectinput.click(coords[0], coords[1])
            message += f' on ({coords[0]}, {coords[1]})'
        self.log.log_interception('success', message)

    def right_click(self, coords=None):
        message = f'Performed right-click'
        if coords is None:
            pydirectinput.click(button='right')
        else:
            pydirectinput.click(coords[0], coords[1], button='right')
            message += f'on ({coords[0]}, {coords[1]})'
        self.log.log_interception('success', message)

    def mouse_down(self):
        pydirectinput.mouseDown()
        self.log.log_interception('success', 'Pressed the mouse down')

    def mouse_up(self):
        pydirectinput.mouseUp()
        self.log.log_interception('success', 'Released the mouse')

    def scroll(self, direction_param, count=1):
        if direction_param.lower() == 'in':
            direction = 1
        elif direction_param.lower() == 'out':
            direction = -1
        else:
            self.log.log_interception('error',
                                          f'Value in \'direction_param\' parameter: \'{direction_param}\' is invalid')
            return
        for i in range(count):
            pyautogui.scroll(direction)
        self.log.log_interception('success', f'Scrolled {direction_param} {count} scroll-clicks')

    def drag(self, x_offset=None, y_offset=None, duration=0.0):
        pyautogui.drag(x_offset, y_offset, duration)
        self.log.log_interception('success',
                                      f'Dragged mouse an offset of ({x_offset}, {y_offset}) over a duration of {duration} seconds')

    def find_image(self, path, filename, confidence=0.8, grayscale=False):
        box = pyautogui.locateOnScreen(f'{path}\\{filename}', confidence=confidence, grayscale=grayscale,)
        if box is None:
            self.log.log_interception('error', f'Could not find \'{filename}\' on screen')
            return box
        else:
            self.log.log_interception('success', f'Located \'{filename}\' image')
            return box

    def press(self, key):
        pydirectinput.press(key)
        self.log.log_interception('success', f'Pressed the \'{key}\' character on the keyboard')

    def key_down(self, key):
        pydirectinput.keyDown(key)
        self.log.log_interception('success', f'Pressed the \'{key}\' key down')

    def key_up(self, key):
        pydirectinput.keyUp(key)
        self.log.log_interception('success', f'released the {key} key')
