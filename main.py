from bots.config_bot import ConfigBot

config_bot = ConfigBot()
config_bot.generate_config_py()

from bots.reset_bot import ResetBot
from bots.crafter_bot import CrafterBot

reset_bot = ResetBot()
crafter_bot = CrafterBot()

reset_bot.count_down(5)

# Write your code here!

config_bot.destroy_config_py()
