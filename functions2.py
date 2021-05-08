from random import randint
import pydirectinput as pdi

from config import LOCAL_PROJECT_PATH
from functions import find_image, generate_delay as delay, generate_delay, generate_haystack_image
from functions import generate_coords as gc


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


def harvest_field(crop):
    generate_haystack_image()
    delay(1000)
    c = find_image(
        f'fields\\{crop}_field',
        confidence=0.3
        # haystackImage=f'{LOCAL_PROJECT_PATH}haystack.png'
    )
    if c is None:
        print(f'IMAGE CAPTURE FAILED: {crop}')
        return
    else:
        for i in range(randint(1,2)):
            coords = gc(c[0], c[1], c[2], c[3])
            pdi.rightClick(coords[0], coords[1])
            generate_delay(500, 200)
        print(f'began harvesting {crop}')


def interact_with_npc(nameplate):
    c = find_image(f'nameplates\\{nameplate}')
    if c is None:
        print('IMAGE CAPTURE FAILED')
        return
    else:
        coords = gc(c[0], c[1], c[2], c[3])
        pdi.rightClick(coords[0], coords[1])
        print('interacted with npc')


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
