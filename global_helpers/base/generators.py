import datetime
import time
from random import randint


def generate_delay(delay_ms=1000, delay_range=100):
    random_delay = randint(int(delay_ms - delay_range / 2), int(delay_ms + delay_range / 2))
    time.sleep(random_delay / 1000)
    print(f'delayed {random_delay} ms...')


def generate_coords(left, top, width, height):
    x = randint(left + 2, left + width - 2)
    y = randint(top + 2, top + height - 2)
    coords = (x, y)
    return coords


def generate_date_time(dt_format='date_time', ds='-', ts=':'):
    if dt_format.lower() == 'date_time':
        return datetime.datetime.now().strftime(f'%Y{ds}%m{ds}%d %H{ts}%M{ts}%S{ts}%f')
    elif dt_format.lower() == 'date':
        return datetime.datetime.now().strftime(f'%Y{ds}%m{ds}%d')
    elif dt_format.lower() == 'time':
        return datetime.datetime.now().strftime(f'%M{ts}%S{ts}%f')