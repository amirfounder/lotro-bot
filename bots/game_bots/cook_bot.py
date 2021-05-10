from bots.game_bots.crafter_bot import CrafterBot


class CookBot:

    craft_bot = CrafterBot()

    def __init__(self, name="CookBot"):
        self.name = name

    def cook_food(self, tier, category, recipe, total, batch_count):
        self.craft_bot.bulk_craft('cooking', tier, category, recipe, total, batch_count, 3000)