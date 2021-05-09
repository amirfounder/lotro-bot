import math
import random

import config
from bots.Interactor import InteractorBot
from bots.generator_bot import GeneratorBot
from bots.image_bot import ImageBot
from bots.interceptor_bot import InterceptorBot
from bots.logger_bot import LoggerBot
from bots.npc_bot import NpcBot


class CrafterBot:
    gen_bot = GeneratorBot()
    image_bot = ImageBot()
    int_bot = InterceptorBot()
    log_bot = LoggerBot()
    interact = InteractorBot()
    npc = NpcBot()

    def __init__(self, name="CrafterBot"):
        self.name = name

    def toggle_crafting_panel(self):
        path = f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\crafting_panel'
        filename = 'crafting_panel_header.png'
        box = self.int_bot.find_image(path, filename)

        if box is not None:
            self.log_bot.log_crafter('info', 'crafting panel already toggled on')
            return
        self.int_bot.press('t')
        box = self.int_bot.find_image(path, filename)
        if box is None:
            self.log_bot.log_crafter('error', f'there was a problem opening the crafting panel')
        self.log_bot.log_crafter('success', f'successfully toggled the crafting panel on')

    def toggle_trade(self, trade):
        self.interact.toggle(
            path=f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\tabs',
            target=trade,
            t_type='trade',
            image_confidence=0.95
        )

    def toggle_tier(self, tier):
        self.interact.toggle(
            path=f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\crafting_panel\\tiers',
            target=tier,
            t_type='tier',
            image_confidence=0.99
        )

    def toggle_category(self, category):
        self.interact.toggle(
            path=f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\crafting_panel\\categories',
            target=category,
            t_type='tier',
            image_confidence=0.93
        )

    def click_recipe(self, recipe):
        path = f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\crafting_panel\\recipes'
        filename = f'{recipe}.png'

        box = self.int_bot.find_image(path, filename, 0.95)
        if box is None:
            self.log_bot.log_crafter('error', f'unable to find the recipe, {recipe}')
            return
        self.log_bot.log_crafter('success', f'clicked the {recipe} recipe')
        self.interact.move_click(box)

    def navigate_to_recipe(self, tier, category, recipe):
        # TODO make a call to a database with just a recipe and it should return trade, tier, and category
        self.toggle_crafting_panel()
        self.toggle_trade('farming')
        self.toggle_tier(tier)
        self.toggle_category(category)
        self.click_recipe(recipe)

    def harvest_field(self, field):
        box = self.image_bot.find_images_from_directory(
            path=f'{config.IMAGES_DIRECTORY_PATH}\\world\\field_floaty_names\\{field}',
            confidence=0.6,
            grayscale=False
        )
        for i in range(random.randint(1, 2)):
            self.interact.move_click(box, button='right')

    def plant_and_harvest_fields(self, tier, category, recipe, count):
        for i in range(count):
            self.interact.click_button('make')
            self.gen_bot.generate_delay()
            self.int_bot.press('t')
            self.gen_bot.generate_delay()
            # self.int_bot.screenshot( f'{config.ML_DATA_DIRECTORY_PATH}\\screenshots\\{
            # self.gen_bot.generate_date_time("", "", "_", ms=False)}.png')
            self.gen_bot.generate_delay(3000, 500)
            self.harvest_field('spring_barley_field')
            # self.int_bot.screenshot( f'{config.ML_DATA_DIRECTORY_PATH}\\screenshots\\{
            # self.gen_bot.generate_date_time("", "", "_", ms=False)}.png')
            self.gen_bot.generate_delay()
            self.int_bot.press('t')
            self.gen_bot.generate_delay(7000, 1000)

    def plant_and_harvest_fields_bulk(self, tier, category, recipe, seed_count, batch_count=80):
        self.navigate_to_recipe(tier, category, recipe)
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
        self.navigate_to_recipe(tier, category, recipe)
        for i in range(math.ceil(total / batch_count)):
            self.interact.click_button('make_all')
            self.gen_bot.generate_delay(5000 * batch_count + 1000, 1500)
            self.int_bot.press('space')
            self.gen_bot.generate_delay()
            self.npc.repair_all()
            self.gen_bot.generate_delay()
            self.log_bot.log_crafter('success', f'planted and harvest {i + 1} time(s)')