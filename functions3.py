import math

import pydirectinput as pdi

from functions import generate_delay as delay
from functions2 import click_button, \
    harvest_field


def plant_and_harvest_crops():

    for i in range(45):
        click_button('make')
        delay(250)
        pdi.press('t')
        delay(4000, 500)

        harvest_field('spring_barley')
        delay(7000, 500)
        pdi.press('t')
        delay(250)


def make_bulk_recipe(total, batch_count):
    """
    DESCRIPTION:

    This function will run a for loop to bulk make a pre-selected recipe, and repair itself after batch_count param
    limit is reached.

    GUI ASSUMPTIONS:

    1. NPC interaction panel is open.
    2. Crafting panel is navigated to the desired recipe.
    3. Tools fully repaired

    :param total: total amount of crops.
    :param batch_count:
    :return: void
    """

    make_per_batch = math.floor(total / batch_count)

    for i in range(make_per_batch):
        click_button('make_all')
        delay(5000 * make_per_batch + 1000, 1000)

        pdi.press('space')

        click_button('repair_all')
        delay(1500, 500)
