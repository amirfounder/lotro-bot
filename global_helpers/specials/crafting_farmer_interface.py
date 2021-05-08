from random import randint
import pydirectinput as pdi

from global_helpers.base.api_interface import find_image
from global_helpers.base.generators import generate_coords as gc, generate_delay as delay
from global_helpers.base.logger import log
from global_helpers.gui.gui_clicks import click_button
from global_helpers.specials.general import navigate_to_recipe, make_all


def plant_field(tier, category, field):
    """
    Plant a field
    :param tier: recipe tier
    :param category: recipe category
    :param field: filed file name
    :return: void
    """
    # TODO: Create database linking field to tier, category and craft to remove unnecessary paramaters
    navigate_to_recipe('farming', tier, category, field)
    click_button('make')
    log('Farmer Interface', 'S', f'began planting \'{field}\'')
    delay(3750, 250)
    log('Farmer Interface', 'success', f'successfully planted \'{field}\'')


def harvest_field(field):
    """
    Harvest the field
    :param field: field file name
    :return: void
    """
    # TODO: Capture the image of the induction to confirm player is performing skill
    i = 1
    c = find_image(f'fields\\{field}', confidence=0.3)
    while c is None and i < 2:
        log('Farmer Interface', 'WARNING', f'Failed to find image \'{field}\' (try: 1)')
        c = find_image(f'fields\\{field}', confidence=0.3)
        i += 1
    if c is None:
        log('Farmer Interface', 'ERROR', f'Failed to find image \'{field}\'')
        return
    for i in range(randint(1,2)):
        coords = gc(c[0], c[1], c[2], c[3])
        pdi.rightClick(coords[0], coords[1])
        delay(500, 800)
    log('Farmer Interface', 'UNKNOWN', f'Right-clicked on the generated coordinates of the field \'{field}\'')


def plant_and_harvest_field(tier, category, field):
    """
    Interface to run plant and harvest field
    :param tier: recipe tier
    :param category: recipe category
    :param field: field file name
    :return: void
    """
    plant_field(tier, category, field)
    harvest_field(field)


def work_all_crops(total_count, make_per_batch, tier, category, recipe):
    make_all(total_count, make_per_batch, 5000, 'crafting', tier, category, recipe)
    log('Farmer Interface', 'BEGUN', 'Began working all crops')
