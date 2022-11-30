from PIL import Image, ImageDraw

image = Image.new('L', (960, 540), 255)

draw = ImageDraw.Draw(image)

draw_img = lambda coordArray: draw.line((int(coordArray[1]), 540 - int(coordArray[0]), int(coordArray[1]) + 1, 540 - (int(coordArray[0]) + 1)))
with open("DS2.txt", 'r', encoding='utf-8') as file:
    file_lines = list(map(lambda el: el.strip(), file.readlines()))
    for el in file_lines:
        draw_img(el.split())

image.show()
image.save("DS2.jpeg", "JPEG")

