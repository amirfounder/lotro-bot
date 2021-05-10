import math

import config
from bots.game_bots.interaction_bot import InteractionBot
from bots.util_bots.generator_bot import GeneratorBot
from bots.util_bots.image_bot import ImageBot
from bots.util_bots.interceptor_bot import InterceptorBot
from bots.util_bots.logger_bot import LoggerBot
from bots.game_bots.npc_bot import NpcBot


class CrafterBot:
    gen_bot = GeneratorBot()
    image_bot = ImageBot()
    int_bot = InterceptorBot()
    log_bot = LoggerBot()
    interact = InteractionBot()
    npc = NpcBot()

    def __init__(self):
        self.log_bot.log_crafter('initialized', 'crafter_bot built and deployed...')

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

    def navigate_to_recipe(self, trade, tier, category, recipe):
        # TODO make a call to a database with just a recipe and it should return trade, tier, and category
        self.toggle_crafting_panel()
        self.toggle_trade(trade)
        self.toggle_tier(tier)
        self.toggle_category(category)
        self.click_recipe(recipe)

    def bulk_craft(self, trade, tier, category, recipe, total, batch_count, induction_speed):
        self.navigate_to_recipe(trade, tier, category, recipe)
        for i in range(math.ceil(total / batch_count)):
            self.interact.click_button('make_all')
            self.gen_bot.generate_delay(induction_speed * batch_count + 1000, 1500)
            self.int_bot.press('space')
            self.gen_bot.generate_delay()
            self.npc.repair_all()
            self.gen_bot.generate_delay()
            self.log_bot.log_crafter('success', f'planted and harvest {i + 1} time(s)')

