import pydirectinput as pdi

from global_helpers.base.api_interface import find_image
from global_helpers.base.generators import generate_coords as gc


def click_recipe(recipe):
    c = find_image(f'recipes\\{recipe}', confidence=0.9)
    if c is None:
        print('IMAGE CAPTURE FAILED')
        return
    else:
        coords = gc(c[0], c[1], c[2], c[3])
        pdi.leftClick(coords[0], coords[1])
        print(f'selected {recipe}')


def click_button(button):
    c = find_image(f'buttons\\{button}', confidence=0.95)
    if c is None:
        print('IMAGE CAPTURE FAILED')
        return
    else:
        coords = gc(c[0], c[1], c[2], c[3])
        pdi.leftClick(coords[0], coords[1])
        print(f'began planting')