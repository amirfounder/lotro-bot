import datetime
import random
import time

from bots.util_bots.logging_bot import LoggingBot


class GenerationBot:
    log = LoggingBot()

    def __init__(self):
        self.log.log_generation('initialized', 'GENERATION_BOT built and deployed...')

    def generate_date(self, ds='-'):
        g_date = datetime.datetime.now().strftime(f'%Y{ds}%m{ds}%d')
        self.log.log_generation('success', 'Generated current date')
        return g_date

    def generate_time(self, ts=':', ms=True):
        if ms:
            g_time = datetime.datetime.now().strftime(f'%H{ts}%M{ts}%S{ts}%f')
        else:
            g_time = datetime.datetime.now().strftime(f'%H{ts}%M{ts}%S')
        self.log.log_generation('success', 'Generated current time')
        return g_time

    def generate_date_time(self, ds='-', ts=':', s=' ', ms=True):
        g_date = self.generate_date(ds=ds)
        g_time = self.generate_time(ts=ts, ms=ms)
        g_date_time = f'{g_date}{s}{g_time}'
        self.log.log_generation('success', 'Generated current date_time')
        return g_date_time

    def generate_delay(self, delay=200, delay_range=360):
        ran_delay = random.randint(delay - int(delay_range / 2), delay + int(delay_range / 2))
        time.sleep(ran_delay / 1000)
        self.log.log_generation('success',
                                f'Generated random delay: {ran_delay} milliseconds ({ran_delay / 1000} seconds)')
        return

    def generate_coords(self, left, top, width, height, x_padding, y_padding):
        ran_x = random.randint(int(left + x_padding), int((left + width) - x_padding))
        ran_y = random.randint(int(top + y_padding), int((top + height) - y_padding))
        xy = (ran_x, ran_y)
        self.log.log_generation('success', f'Generated random coords: ({ran_x}, {ran_y})')
        return xy

    def generate_duration(self, lower_threshold_ms=250, upper_threshold_ms=500):
        duration = random.randint(lower_threshold_ms, upper_threshold_ms) / 1000
        self.log.log_generation('success', f'Generated a random duration of {duration} seconds')
        return duration
