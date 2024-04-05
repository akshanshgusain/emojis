from PIL import Image
from colr import Colr

image = Image.open('img.png')
pixel_values = image.getdata()

width, height = image.size
for index, character in enumerate(pixel_values):
    if not isinstance(character, (tuple, list)):
        continue
    r, g, b = character[:-1]
    if index % width == 0:
        print("")
    print(Colr().rgb(r, g, b, "\u2584"), end="")


q =  get_a_record("User")
q2 =  get_a_record("User")
q3 =  get_a_record("User")

import requests
r = requests.get("")

q3 =  get_a_record("User")