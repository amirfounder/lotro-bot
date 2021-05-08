import datetime
from config import LOGS_PATH


def add_spacing(message, gap_size, symbol=' '):
    while len(message) < gap_size:
        message += symbol
    return message


def write_to_file(message):
    now = datetime.datetime.now()
    today = now.strftime('%Y_%m_%d')
    file_path = f'{LOGS_PATH}log_{today}.log'
    f = open(file_path, mode='a')
    f.write(f'{message}\n')


def log(log_level='NONE', log_type='NONE', log_message='NONE'):
    now = datetime.datetime.now()
    message = f'TIME: {now.strftime("%Y-%m-%d %H:%M:%S:%f")}'

    message = add_spacing(message, 20, '.')
    message += log_level

    message = add_spacing(message, 40, '.')
    message += log_type

    message = add_spacing(message, 10, '.')
    message += log_message

    write_to_file(message)
    print(message)
