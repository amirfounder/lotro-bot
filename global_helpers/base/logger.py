import datetime
from config import LOGS_DIRECTORY_PATH
from global_helpers.base.generators import generate_date_time


def add_spacing(message, gap_size, symbol=' '):
    while len(message) < gap_size:
        message += symbol
    return message


def write_to_file(message):
    now = datetime.datetime.now()
    today = now.strftime('%Y_%m_%d')
    file_path = LOGS_DIRECTORY_PATH + r'\log_' + today + '.log'
    f = open(file_path, mode='a')
    f.write(f'{message}\n')


def log(log_level='NONE', log_type='NONE', log_message='NONE'):
    message = generate_date_time()
    message = add_spacing(message, 30, ' ')

    message += log_level
    message = add_spacing(message, 50, ' ')

    message += log_type
    message = add_spacing(message, 65, ' ')

    message += log_message
    write_to_file(message)
    print(message)

log()