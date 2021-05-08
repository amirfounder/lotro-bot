from functions import generate_delay as delay, reset_camera
from functions import countdown

from functions2 import navigate_to_recipe
from functions3 import plant_and_harvest_crops, make_bulk_recipe

print('bot starting in...')

countdown()
delay(250)

# reset_camera()
# delay(250)

navigate_to_recipe('cooking', 'apprentice', 'ingredients', 'cup_of_spring_barley_flour')
make_bulk_recipe(3742, 100)
