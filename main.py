from bots.config_bot import ConfigBot

config_bot = ConfigBot()
config_bot.generate_config_py()

from bots.crafter_bot import CrafterBot
from bots.generator_bot import GeneratorBot
from bots.interceptor_bot import InterceptorBot
from bots.reset_bot import ResetBot

reset_bot = ResetBot()
crafter_bot = CrafterBot()
int_bot = InterceptorBot()
gen_bot = GeneratorBot()

# TODO : Run this program if this is the first time running the bot on your laptop
config_bot.generate_config_py()

reset_bot.count_down(3)
reset_bot.reset_camera_position()
reset_bot.reset_camera_scroll()
crafter_bot.plant_and_harvest_fields('expert', 'vegetables', 'green_onion_field', 1)
# crafter_bot.process_crops('apprentice', 'grains', 'bundle_of_spring_barley', 1792, 100)

config_bot.destroy_config_py()
