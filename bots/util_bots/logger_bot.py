import datetime

import config


class LoggerBot:
    default_log_spacing_symbol = ' '

    def __init__(self, name="LoggerBot"):
        self.name = name
        self.log_directory = config.LOGS_DIRECTORY_PATH
        self.log_file = f'{self.log_directory}\\{datetime.datetime.now().strftime(f"%Y_%m_%d")}.log'

    @staticmethod
    def generate_log_padding(message, spacing, symbol=default_log_spacing_symbol):
        while len(message) <= spacing:
            message += symbol
        return message

    def write_to_log_file(self, message):
        f = open(self.log_file, mode='a')
        f.write(f'{message}\n')

    def log_message(self, l_level=r'N\A', l_type=r'N\A', l_message=r'N\A', persist=config.LIVE, capitalize_message=True):
        """
        General method to print a log message and save to file
        :param l_level: level of the logging message(generator_bot, image_bot, etc.)
        :param l_type: type of message (success, failed, init, warning)
        :param l_message: message to write to the log
        :param persist: whether to persist the log to the file
        :param capitalize_message:
        :return: void
        """
        message = datetime.datetime.now().strftime(f"%Y_%m_%d %H:%M:%S:%f")
        message = self.generate_log_padding(message, 30)

        message += f'LEVEL:{l_level.upper()}'
        message = self.generate_log_padding(message, 54)

        message += f'TYPE:{l_type.upper()}'
        message = self.generate_log_padding(message, 72)

        if capitalize_message:
            message += f'MESSAGE:{l_message.capitalize()}'
        else:
            message += f'MESSAGE:{l_message}'
        print(message)

        if persist:
            self.write_to_log_file(message)

    def log_interceptor(self, l_type, l_message):
        self.log_message(
            'interceptor_bot',
            l_type,
            l_message
        )

    def log_generator(self, l_type, l_message):
        self.log_message(
            'generator_bot',
            l_type,
            l_message
        )

    def log_reset(self, l_type, l_message):
        self.log_message(
            'reset_bot',
            l_type,
            l_message,
            capitalize_message=False
        )

    def log_crafter(self, l_type, l_message):
        self.log_message(
            'crafter_bot',
            l_type,
            l_message
        )

    def log_movement(self, l_type, l_message):
        self.log_message(
            'movement_bot',
            l_type,
            l_message
        )
