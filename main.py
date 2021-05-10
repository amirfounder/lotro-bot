from bots.game_bots.boss_bots.hobitton_one import HobbitonBossBot
from bots.game_bots.interaction_bot import InteractionBot
from bots.util_bots.config_bot import ConfigBot

config = ConfigBot()
config.generate_config_py()

from bots.reset_bot import ResetBot

reset = ResetBot()
interact = InteractionBot()
boss_bot = HobbitonBossBot()

reset.count_down(5)

boss_bot.run()

# config.destroy_config_py()
# config.destroy_main_py()
