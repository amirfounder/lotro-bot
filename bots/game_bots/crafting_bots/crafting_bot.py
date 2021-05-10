import math

import config
from bots.game_bots.interaction_bot import InteractionBot
from bots.game_bots.npc_handling_bot import NpcHandlingBot
from bots.util_bots.generation_bot import GenerationBot
from bots.util_bots.imaging_bot import ImagingBot
from bots.util_bots.interception_bot import InterceptionBot
from bots.util_bots.logging_bot import LoggingBot


class CraftingBot:
    generate = GenerationBot()
    image = ImagingBot()
    intercept = InterceptionBot()
    log = LoggingBot()
    interact = InteractionBot()
    handle_npc = NpcHandlingBot()

    def __init__(self):
        self.log.log_crafting('initialized', 'crafter_bot built and deployed...')

    def toggle_crafting_panel(self, specialization):
        path = f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\headers'
        filename = specialization
        box = self.intercept.find_image(path, filename)

        if box is not None:
            self.log.log_crafting('info', 'crafting panel already toggled on')
            return
        self.intercept.press('t')
        box = self.intercept.find_image(path, filename)
        if box is None:
            self.log.log_crafting('error', f'there was a problem opening the crafting panel')
        self.log.log_crafting('success', f'successfully toggled the crafting panel on')

    def toggle_trade(self, trade):
        self.interact.toggle(f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\tabs', trade, 'trade', 0.95)

    def toggle_tier(self, tier):
        self.interact.toggle(f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\crafting_panel\\tiers', tier, 'tier',
                             0.99)

    def toggle_category(self, category):
        self.interact.toggle(f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\crafting_panel\\categories',
                             category, 'tier', 0.97)

    def click_recipe(self, recipe):
        path = f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\crafting_panel\\recipes'
        filename = f'{recipe}.png'
        box = self.intercept.find_image(path, filename, 0.95)
        if box is None:
            self.log.log_crafting('error', f'unable to find the recipe, {recipe}')
            return
        self.log.log_crafting('success', f'clicked the {recipe} recipe')
        self.interact.move_mouse_and_click(box)

    def navigate_to_recipe(self, trade, tier, category, recipe):
        self.toggle_crafting_panel('yeoman.png')
        self.toggle_trade(trade)
        self.toggle_tier(tier)
        self.toggle_category(category)
        self.click_recipe(recipe)

    def bulk_craft(self, trade, tier, category, recipe, total, batch_count, induction_speed):
        self.navigate_to_recipe(trade, tier, category, recipe)
        for i in range(math.ceil(total / batch_count)):
            self.interact.click_button('make_all')
            self.generate.generate_delay(induction_speed * batch_count + 1000, 1500)
            self.intercept.press('space')
            self.generate.generate_delay()
            self.interact.move_mouse_and_click('repair_all')
            self.generate.generate_delay()
            self.log.log_crafting('success', f'planted and harvest {i + 1} time(s)')
