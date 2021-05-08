from global_helpers import generate_delay as delay, reset_camera
from global_helpers import countdown
import pyautogui

from functions2 import navigate_to_recipe
from functions3 import plant_and_harvest_crops, make_bulk_recipe


countdown()
delay(250)

reset_camera()
delay(250)

navigate_to_recipe('farming', 'apprentice', 'grains', 'spring_barley_field')
plant_and_harvest_crops(15)
# make_bulk_recipe(3742, 100)
