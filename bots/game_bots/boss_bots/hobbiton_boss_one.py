from bots.game_bots.crafting_bots.cooking_bot import CookingBot
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
    cook = CookingBot()

    def __init__(self):
        print('level 1 boss bot appeared at hobbiton...')

    def bulk_farm(self):
        self.reset.reset_camera_position()
        self.reset.reset_camera_scroll()
        self.farm.plant_and_harvest_fields_bulk(
            'journeyman',
            'vegetables',
            'blueberry_field',
            160,
            45,
            'hobbiton',
            'porto_brownlock'
        )

    def bulk_process(self):
        self.farm.process_crops(
            'journeyman',
            'vegetables',
            'bunch_of_blueberries',
            480,
            80
        )

    def bulk_cook(self):
        self.cook.cook_food('journeyman', 'ingredients', 'blueberry_pie_filling', 210, 70)