from bots.game_bots.crafting_bots.farming_bot import FarmingBot
from bots.game_bots.interaction_bot import InteractionBot
from bots.game_bots.movement_bot import MovementBot
from bots.game_bots.npc_handling_bot import NpcHandlingBot
from bots.reset_bot import ResetBot
from bots.util_bots.generation_bot import GenerationBot


class HobbitonBossBot:
    reset = ResetBot()
    move = MovementBot()
    farm = FarmingBot()
    interact = InteractionBot()
    generate = GenerationBot()
    handle_npc = NpcHandlingBot()

    def __init__(self):
        print('level 1 boss bot appeared at hobbiton...')

    def run(self):
        self.reset.reset_camera_position()
        self.reset.reset_camera_scroll()
        self.move.strafe_right(2000)
        self.farm.plant_and_harvest_fields_bulk(
            'journeyman',
            'vegetables',
            'blueberry_field',
            10,
            7
        )
        self.move.strafe_left(2000)
        self.generate.generate_delay(1000)
        self.handle_npc.interact_and_repair_all('hobbiton', 'porto_brownlock')
