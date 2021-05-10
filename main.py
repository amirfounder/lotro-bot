from bots.util_bots.configuration_bot import ConfigBot

config = ConfigBot()
config.generate_config_py()

from bots.reset_bot import ResetBot
from bots.game_bots.boss_bots.hobbiton_boss_one import HobbitonBossBot

reset = ResetBot()
boss_bot = HobbitonBossBot()

reset.count_down(5)

boss_bot.bulk_cook()

config.destroy_config_py()
# config.destroy_main_py()
