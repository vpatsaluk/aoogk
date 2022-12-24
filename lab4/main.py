
import numpy as np
from PIL import Image, ImageDraw

#-------------------------
# d can be changed
d = 20
#-------------------------

image = Image.new('L', (960, 540), 255)

draw = ImageDraw.Draw(image)

with open('DS2.txt', 'r', encoding='utf-8') as file_dataset, open('DS2New.txt', 'w', encoding='utf-8') as file_dataset_new :
    file_dataset_list = list(map(lambda el: el.strip(), file_dataset.readlines()))

    for coord_pair in file_dataset_list:
        exist_coords = [float(el) for el in coord_pair.split()]

        matrix_point = np.array([exist_coords[0], exist_coords[1], 100, 1])
        matrix = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 1/d],
                          [0, 0, 0, 0]])

        matrix_center = np.dot(matrix_point, matrix)

        matrix_center = list(map(lambda el: el/(100 / d), matrix_center))
        print(matrix_center[0], matrix_center[1], file = file_dataset_new)


draw_img = lambda coordArray: draw.line((float(coordArray[0]) + 480, float(coordArray[1]) + 480, float(coordArray[0]) + 481,
                                         float(coordArray[1]) + 481), fill=15)
with open('DS2New.txt', 'r', encoding='utf-8') as file_dataset:
    file_lines = list(map(lambda el: el.strip(), file_dataset.readlines()))
    for el in file_lines:
        draw_img(el.split())

image.show()
image.save("DS2.jpeg", "JPEG")
