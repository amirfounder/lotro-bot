from bots.config_bot import ConfigBot

config_bot = ConfigBot()
config_bot.generate_config_py()

from bots.reset_bot import ResetBot
from bots.crafter_bot import CrafterBot

reset_bot = ResetBot()
crafter_bot = CrafterBot()

reset_bot.count_down(5)
# reset_bot.reset_camera_position()
# reset_bot.reset_camera_scroll()
# crafter_bot.plant_and_harvest_field('apprentice', 'grains', 'spring_barley_field', 50)
crafter_bot.cook_food('apprentice', 'ingredients', 'cup_of_spring_barley_flour', 3782, 50)

config_bot.destroy_config_py()
