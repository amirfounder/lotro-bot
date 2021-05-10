import config
from bots.game_bots.interaction_bot import InteractionBot
from bots.util_bots.generation_bot import GenerationBot
from bots.util_bots.imaging_bot import ImagingBot
from bots.util_bots.interception_bot import InterceptionBot
from bots.util_bots.logging_bot import LoggingBot


class NpcHandlingBot:
    interact = InteractionBot()
    intercept = InterceptionBot()
    generate = GenerationBot()
    log = LoggingBot()
    image = ImagingBot()

    def __init__(self):
        self.log.log_npc_handling('initialized', 'NPC_HANDLING_BOT built and deployed...')

    def interact_with_npc(self, location, npc_name):
        pathname = f'{config.IMAGES_DIRECTORY_PATH}\\world\\npc_nameplates\\{location}\\{npc_name}'
        box = self.image.find_images_from_directory(pathname, 0.33)
        if box is not None:
            self.interact.move_mouse_and_click(box, 'right', x_padding=8, y_padding=8)
            return
        return None

    def toggle_repair_tab(self):
        self.interact.toggle(f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\tabs', 'repair', 'tab', 0.95)

    def interact_and_repair_all(self, location, npc_name):
        self.interact_with_npc(location, npc_name)
        box = self.intercept.find_image(f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\headers', 'shop.png')
        if box is None:
            box = self.intercept.find_image(f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\npc_interactions',
                                            'browse_the_shop.png')
            self.interact.move_mouse_and_click(box, x_padding=5, y_padding=5)
        self.generate.generate_delay(500)
        self.toggle_repair_tab()
        self.generate.generate_delay()
        self.interact.click_button('repair_all')
        self.generate.generate_delay()
        self.intercept.press('esc')
        self.intercept.press('esc')
