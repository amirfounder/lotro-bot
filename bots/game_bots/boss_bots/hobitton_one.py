from bots.game_bots.farmer_bot import FarmerBot
from bots.game_bots.interaction_bot import InteractionBot
from bots.game_bots.movement_bot import MovementBot
from bots.reset_bot import ResetBot
from bots.util_bots.generator_bot import GeneratorBot


class HobbitonBossBot:
    reset_bot = ResetBot()
    movement_bot = MovementBot()
    farmer_bot = FarmerBot()
    interaction_bot = InteractionBot()
    generator_bot = GeneratorBot()

    def __init__(self):
        print('level 1 boss bot appeared at hobbiton...')

    def run(self):
        self.reset_bot.reset_camera_position()
        self.reset_bot.reset_camera_scroll()
        self.movement_bot.strafe_right(3000)
        self.farmer_bot.plant_and_harvest_fields_bulk(
            'journeyman',
            'vegetables',
            'blueberry_field',
            1,
            1
        )
        self.movement_bot.strafe_left(3000)
        self.generator_bot.generate_delay(3200)
        self.interaction_bot.repair_tools('hobbiton', 'porto_brownlock')
