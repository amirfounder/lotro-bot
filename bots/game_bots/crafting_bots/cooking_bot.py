from bots.game_bots.crafting_bots.crafting_bot import CraftingBot


class CookingBot:
    craft = CraftingBot()

    def __init__(self, name="CookBot"):
        self.name = name

    def cook_food(self, tier, category, recipe, total, batch_count):
        self.craft.bulk_craft('cooking', tier, category, recipe, total, batch_count, 3000)
