import pydirectinput as pdi

from global_helpers.base.api_interface import find_image
from global_helpers.base.generators import generate_coords as gc


def toggle_crafting_panel():
    cp = find_image('crafting_panel_header', confidence=0.8)
    if cp is None:
        pdi.press('t')
    return


def toggle_tab(tab):
    t = find_image(f'tabs\\{tab}_tab', confidence=0.85)
    t_toggled = find_image(f'tabs\\{tab}_tab_toggled', confidence=0.85)
    if t is not None:
        coords = gc(t[0], t[1], t[2], t[3])
        pdi.leftClick(coords[0], coords[1])
        print(f'toggled {tab} category')
    elif t_toggled is not None:
        print(f'{tab} craft already toggled!')
        return
    else:
        print('IMAGE CAPTURE FAILED')
        return


def toggle_tier(tier):
    t = find_image(f'tiers\\{tier}_tier', confidence=0.95)
    t_toggled = find_image(f'tiers\\{tier}_tier_toggled', confidence=0.95)
    if t is not None:
        coords = gc(t[0], t[1], t[2], t[3])
        pdi.leftClick(coords[0], coords[1])
        print(f'toggled {tier} category')
    elif t_toggled is not None:
        print(f'{tier} category already toggled!')
        return
    else:
        print('IMAGE CAPTURE FAILED')
        return


def toggle_category(category):
    c = find_image(f'categories\\{category}', confidence=0.95)
    c_toggled = find_image(f'categories\\{category}_toggled', confidence=0.95)
    if c is not None:
        coords = gc(c[0], c[1], c[2], c[3])
        pdi.leftClick(coords[0], coords[1])
        print(f'toggled {category} category')
    elif c_toggled is not None:
        print(f'{category} category already toggled!')
        return
    else:
        print('IMAGE CAPTURE FAILED')
        return