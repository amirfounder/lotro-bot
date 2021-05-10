from bots.util_bots.config_bot import ConfigBot

config = ConfigBot()
config.generate_config_py()

from bots.reset_bot import ResetBot

reset = ResetBot()

reset.count_down(5)

# Remove this comment and start scripting

config.destroy_config_py()
# config.destroy_main_py()
