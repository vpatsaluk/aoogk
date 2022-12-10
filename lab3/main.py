import math

from PIL import Image, ImageDraw

image = Image.new('RGBA', (960, 960), (255, 255, 255))

draw = ImageDraw.Draw(image)

angle = math.radians(10 * (2 + 1))

draw_img = lambda coordArray: draw.line((coordArray[0] + 480, coordArray[1] + 480, coordArray[0] + 481, coordArray[1] + 481), fill=(15, 10, 222))

with open('DS2.txt', 'r', encoding='utf-8') as file:
    file_lines = list(map(lambda el: el.strip(), file.readlines()))
    for el in file_lines:
        coord_list = el.split()
        coord_0 = int(coord_list[0]) - 480
        coord_1 = int(coord_list[1]) - 480
        x = math.cos(angle) * coord_0 - math.sin(angle) * coord_1
        y = math.sin(angle) * coord_0 + math.cos(angle) * coord_1
        draw_img([x, y])

image.show()
image.save('DS2.png', "PNG")