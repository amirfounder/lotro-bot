import pydirectinput as pdi

from config import FARMING_TOOL_SPEED_BOOST
from global_helpers.base.api_interface import find_image
from global_helpers.base.generators import generate_coords as gc, generate_delay as delay
from global_helpers.gui.gui_clicks import click_recipe, click_button
from global_helpers.gui.gui_toggles import toggle_crafting_panel, toggle_tab, toggle_tier, toggle_category


def interact_with_npc(nameplate):
    c = find_image(f'nameplates\\{nameplate}')
    if c is None:
        print('IMAGE CAPTURE FAILED')
        return
    else:
        coords = gc(c[0], c[1], c[2], c[3])
        pdi.rightClick(coords[0], coords[1])
        print('interacted with npc')


def make_all(total_count, make_per_batch, induction_speed, trade, tier, category, recipe):

    # interact with npc
    # click repair tab
    # click repair all

    for i in range(int(total_count / make_per_batch)):

        navigate_to_recipe(trade, tier, category, recipe)

        click_button('make_all')
        delay(induction_speed * make_per_batch + 1000, 1800)

        pdi.press('space')

        click_button('repair_all')
        delay(1000, 1000)
        pdi.press('t')
        delay(1000, 1000)



def navigate_to_recipe(trade, tier, category, recipe):
    toggle_crafting_panel()
    delay(200)
    toggle_tab(trade)
    delay(200)
    toggle_tier(tier)
    delay(200)
    toggle_category(category)
    delay(200)
    click_recipe(recipe)
    delay(500)