import math
import random

import config
from bots.game_bots.interaction_bot import InteractionBot
from bots.game_bots.crafter_bot import CrafterBot
from bots.util_bots.generator_bot import GeneratorBot
from bots.util_bots.image_bot import ImageBot
from bots.util_bots.interceptor_bot import InterceptorBot
from bots.util_bots.logger_bot import LoggerBot


class FarmerBot:
    gen_bot = GeneratorBot()
    image_bot = ImageBot()
    craft_bot = CrafterBot()
    interact = InteractionBot()
    int_bot = InterceptorBot()
    log_bot = LoggerBot()

    def __init__(self):
        print("FarmerBot built and deployed...")

    def harvest_field(self, field):
        box = self.image_bot.find_images_from_directory(
            path=f'{config.IMAGES_DIRECTORY_PATH}\\world\\field_floaty_names\\{field}',
            confidence=0.6,
            grayscale=False
        )
        for i in range(random.randint(1, 2)):
            self.interact.move_click(box, button='right')

    def plant_and_harvest_fields(self, tier, category, recipe, count):
        self.craft_bot.navigate_to_recipe('farming', tier, category, recipe)
        for i in range(count):
            self.interact.click_button('make')
            self.gen_bot.generate_delay()
            self.int_bot.press('t')
            self.gen_bot.generate_delay()
            # self.int_bot.screenshot( f'{config.ML_DATA_DIRECTORY_PATH}\\screenshots\\{
            # self.gen_bot.generate_date_time("", "", "_", ms=False)}.png')
            self.gen_bot.generate_delay(3000, 500)
            self.harvest_field(recipe)
            # self.int_bot.screenshot( f'{config.ML_DATA_DIRECTORY_PATH}\\screenshots\\{
            # self.gen_bot.generate_date_time("", "", "_", ms=False)}.png')
            self.gen_bot.generate_delay()
            self.int_bot.press('t')
            self.gen_bot.generate_delay(7000, 1000)

    def plant_and_harvest_fields_bulk(self, tier, category, recipe, seed_count, batch_count=80):
        last_batch = seed_count % batch_count
        for i in range(math.floor(seed_count / batch_count)):
            self.plant_and_harvest_fields(tier, category, recipe, batch_count)
            self.log_bot.log_crafter('success', f'successfully planted {batch_count} crops')

            # Repair materials

        if last_batch != 0:
            self.plant_and_harvest_fields(tier, category, recipe, batch_count)
            self.log_bot.log_crafter('success', f'successfully planted the last {last_batch} crops')

            # Repair materials

        self.int_bot.press('t')

    def process_crops(self, tier, category, recipe, total, batch_count):
        self.bulk_craft('farming', tier, category, recipe, total, batch_count, 5000)