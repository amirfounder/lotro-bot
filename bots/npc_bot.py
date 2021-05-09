import config
from bots.Interactor import InteractorBot


class NpcBot:

    interact = InteractorBot()

    def __init__(self, name="NpcBot"):
        self.name = name

    def toggle_repair_tab(self):
        self.interact.toggle(
            path=f'{config.IMAGES_DIRECTORY_PATH}\\interaction_panels\\tabs',
            target='repair',
            t_type='trade',
            image_confidence=0.9
        )

    def repair_all(self):
        self.interact.click_button('repair_all')

