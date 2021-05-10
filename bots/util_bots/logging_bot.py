import datetime

import config


class LoggingBot:
    log_file = f'{config.LOGS_DIRECTORY_PATH}\\{datetime.datetime.now().strftime(f"%Y_%m_%d")}'

    def __init__(self):
        self.log_message('logger_bot', 'initialized', 'LOGGER_BOT built and deployed...')

    @staticmethod
    def generate_log_padding(message, spacing, symbol=' '):
        """
        Generates padding for message for logging alignment
        :param message: The message to add padding to
        :param spacing: The amount of spacing to add after the message
        :param symbol: The symbol to use for the padding
        :return: Padded message
        """
        while len(message) <= spacing:
            message += symbol
        return message

    def write_to_log_file(self, message):
        """
        Writes a message to a log file
        :param message: The message to log
        :return: Void
        """
        if config.LIVE:
            f = open(f'{self.log_file}.log', mode='a')
        else:
            f = open(f'{self.log_file}_test.log', mode='a')
        f.write(f'{message}\n')
        f.close()

    def log_message(self, l_level=r'N\A', l_type=r'N\A', l_message=r'N\A'):
        """
        General method to print a log message and save to file
        :param l_level: level of the logging message(generator_bot, image_bot, etc.)
        :param l_type: type of message (success, failed, init, warning)
        :param l_message: message to write to the log
        :return: Void
        """
        message = datetime.datetime.now().strftime(f"%Y_%m_%d %H:%M:%S:%f")
        message = self.generate_log_padding(message, 30)
        message += f'LEVEL:{l_level.upper()}'
        message = self.generate_log_padding(message, 60)
        message += f'TYPE:{l_type.upper()}'
        message = self.generate_log_padding(message, 80)
        message += f'MESSAGE:{l_message}'
        print(message)
        self.write_to_log_file(message)

    def log_crafting(self, l_type, l_message):
        """
        Log a crafting message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('crafting_bot', l_type, l_message)

    def log_generation(self, l_type, l_message):
        """
        Log a generation message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('generation_bot', l_type, l_message)

    def log_interception(self, l_type, l_message):
        """
        Log an interception message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('interception_bot', l_type, l_message)

    def log_movement(self, l_type, l_message):
        """
        Log a movement message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('movement_bot', l_type, l_message)

    def log_reset(self, l_type, l_message):
        """
        Log a reset message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('reset_bot', l_type, l_message)

    def log_imaging(self, l_type, l_message):
        """
        Log an imaging message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('imaging_bot', l_type, l_message)

    def log_farming(self, l_type, l_message):
        """
        Log a farming message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('farming_bot', l_type, l_message)

    def log_cooking(self, l_type, l_message):
        """
        Log a cooking message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('cooking_bot', l_type, l_message)

    def log_interaction(self, l_type, l_message):
        """
        Log an interaction message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('interaction_bot', l_type, l_message)

    def log_npc_handling(self, l_type, l_message):
        """
        Log an NPC handling message
        :param l_type: Success, Info, Warning, or Failure
        :param l_message: The message to log
        :return: Void
        """
        self.log_message('npc_handling_bot', l_type, l_message)