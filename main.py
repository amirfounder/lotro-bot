from bots.crafter_bot import CrafterBot
from bots.generator_bot import GeneratorBot
from bots.interceptor_bot import InterceptorBot
from bots.reset_bot import ResetBot

reset_bot = ResetBot()
crafter_bot = CrafterBot()
int_bot = InterceptorBot()
gen_bot = GeneratorBot()

reset_bot.count_down(3)
# reset_bot.reset_camera_position()
# reset_bot.reset_camera_scroll()
# crafter_bot.plant_and_harvest_field('apprentice', 'grains', 'spring_barley_field', 50)
crafter_bot.process_crops('apprentice', 'grains', 'bundle_of_spring_barley', 1792, 100)