from bots.util_bots.configuration_bot import ConfigurationBot

config = ConfigurationBot()
config.generate_config_py()

from bots.reset_bot import ResetBot
from bots.game_bots.boss_bots.hobbiton_boss_one import HobbitonBossBot

reset = ResetBot()
boss = HobbitonBossBot()

reset.count_down(5)

# boss.do_something_here()

config.destroy_config_py()
# config.destroy_main_py()
