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
            'minas_ithil',
            'vegetables',
            'minas_ithil_field',
            100,
            3,
            'hobbiton',
            'porto_brownlock'
        )

    def bulk_process(self):
        self.farm.process_crops(
            'minas_ithil',
            'vegetables',
            'vegetable_treble',
            887,
            150
        )

    def bulk_cook(self):
        self.cook.cook_food('minas_ithil', 'ingredients', 'bunch_of_par_cooked_vegetables', 7000, 200)
