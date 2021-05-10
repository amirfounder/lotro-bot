import math
import random

import config
from bots.game_bots.crafting_bots.crafting_bot import CraftingBot
from bots.game_bots.interaction_bot import InteractionBot
from bots.game_bots.movement_bot import MovementBot
from bots.game_bots.npc_handling_bot import NpcHandlingBot
from bots.util_bots.generation_bot import GenerationBot
from bots.util_bots.imaging_bot import ImagingBot
from bots.util_bots.interception_bot import InterceptionBot
from bots.util_bots.logging_bot import LoggingBot


class FarmingBot:
    generate = GenerationBot()
    image = ImagingBot()
    craft = CraftingBot()
    interact = InteractionBot()
    intercept = InterceptionBot()
    log = LoggingBot()
    move = MovementBot()
    handle_npc = NpcHandlingBot()

    def __init__(self):
        self.log.log_farming('initialized', 'FARMER_BOT built and deployed...')

    def harvest_field(self, field):
        box = self.image.find_images_from_directory(
            f'{config.IMAGES_DIRECTORY_PATH}\\world\\field_floaty_names\\{field}', 0.55)
        for i in range(random.randint(1, 2)):
            self.interact.move_mouse_and_click(box, button='right')

    def plant_and_harvest_fields(self, tier, category, recipe, count):
        self.craft.navigate_to_recipe('farming', tier, category, recipe)
        for i in range(count):
            self.interact.click_button('make')
            self.generate.generate_delay()
            self.intercept.press('t')
            self.generate.generate_delay()
            self.generate.generate_delay(3000, 500)
            self.harvest_field(recipe)
            self.generate.generate_delay(7000, 1000)
            self.generate.generate_delay()
            self.intercept.press('t')
            self.generate.generate_delay()

    def plant_and_harvest_fields_bulk(self, tier, category, recipe, seed_count, batch_count, location, npc_name):
        last_batch = seed_count % batch_count
        for i in range(math.floor(seed_count / batch_count)):
            self.move.strafe_left(3000)
            self.plant_and_harvest_fields(tier, category, recipe, batch_count)
            self.log.log_farming('success', f'Planted {batch_count} crops')
            self.intercept.press('t')
            self.move.strafe_right(3000)
            self.handle_npc.interact_and_repair_all(location, npc_name)
        if last_batch != 0:
            self.move.strafe_left(3000)
            self.plant_and_harvest_fields(tier, category, recipe, last_batch)
            self.log.log_farming('success', f'Planted the last {last_batch} crop(s)')
            self.intercept.press('t')
            self.move.strafe_right(3000)
            self.handle_npc.interact_and_repair_all(location, npc_name)

    def process_crops(self, tier, category, recipe, total, batch_count):
        self.craft.bulk_craft('farming', tier, category, recipe, total, batch_count, 5000)
