import datetime
import random
import time

from bots.logger_bot import LoggerBot


class GeneratorBot:

    log_bot = LoggerBot()

    default_ds = '-'
    default_ts = ':'
    default_s = ' '
    default_delay = 250
    default_delay_range = 200
    default_log_spacing_symbol = ' '
    default_duration_low_threshold_ms = 500
    default_duration_high_threshold_ms = 1000

    generated_times = []
    generated_dates = []
    generated_date_times = []
    generated_delays = []
    generated_coords = []

    def __init__(self, name='GeneratorBot'):
        self.name = name

    def generate_date(self, ds=default_ds):
        g_date = datetime.datetime.now().strftime(f'%Y{ds}%m{ds}%d')
        self.generated_dates.append(g_date)
        self.log_bot.log_generator('success', 'successfully generated current date')
        return g_date

    def generate_time(self, ts=default_ts, ms=True):
        if ms:
            g_time = datetime.datetime.now().strftime(f'%H{ts}%M{ts}%S{ts}%f')
        else:
            g_time = datetime.datetime.now().strftime(f'%H{ts}%M{ts}%S')
        self.generated_times.append(g_time)
        self.log_bot.log_generator('success', 'successfully generated current time')
        return g_time

    def generate_date_time(self, ds=default_ds, ts=default_ts, s=default_s, ms=True):
        g_date = self.generate_date(ds=ds)
        g_time = self.generate_time(ts=ts, ms=ms)
        g_date_time = f'{g_date}{s}{g_time}'
        self.generated_date_times.append(g_date_time)
        self.log_bot.log_generator('success', 'successfully generated current date_time')
        return g_date_time

    def generate_delay(self, gen_delay=default_delay, gen_range=default_delay_range):
        delay = random.randint(
            gen_delay - int(gen_range / 2),
            gen_delay + int(gen_range / 2)
        )
        time.sleep(delay / 1000)
        self.generated_delays.append(delay)
        self.log_bot.log_generator('success', f'successfully generated delay, {delay} ms ({delay / 1000}) sec')
        return

    def generate_coords(self, left, top, width, height, x_padding, y_padding):
        ran_x = random.randint(left + x_padding, (left + width) - x_padding)
        ran_y = random.randint(top + y_padding, (top + height) - y_padding)
        xy = (ran_x, ran_y)
        self.generated_coords.append(xy)
        self.log_bot.log_generator('success', f'successfully generated coords ({ran_x}, {ran_y})')
        return xy

    def generate_duration(
            self,
            low_threshold_ms=default_duration_low_threshold_ms,
            high_threshold_ms=default_duration_high_threshold_ms
    ):
        duration = random.randint(low_threshold_ms, high_threshold_ms) / 1000
        self.log_bot.log_generator('success', f'successfully generated a duration of {duration} seconds')
        return duration
