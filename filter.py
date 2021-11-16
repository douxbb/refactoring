from PIL import Image
import numpy as np


def get_average_shade_gray(arr, i, j, pixel_size):
    s = 0
    for x in range(i, i + pixel_size):
        for y in range(j, j + pixel_size):
            n1 = arr[x][y][0] / 3
            n2 = arr[x][y][1] / 3
            n3 = arr[x][y][2] / 3
            M = n1 + n2 + n3
            s += M
    return s


def set_color(arr, i, j, s, pixel_size, gradation_step):
    for x in range(i, i + pixel_size):
        for y in range(j, j + pixel_size):
            arr[x][y][0] = int(s // gradation_step) * gradation_step
            arr[x][y][1] = int(s // gradation_step) * gradation_step
            arr[x][y][2] = int(s // gradation_step) * gradation_step


def image_to_pixelart(filename, pixel_size, gradation_step):
    img = Image.open(filename)
    arr = np.array(img)
    height = len(arr)
    width = len(arr[1])
    i = 0
    while i < height - 1:
        j = 0
        while j < width - 1:
            s = get_average_shade_gray(arr, i, j, pixel_size)
            s = int(s // pixel_size ** 2)
            set_color(arr, i, j, s, pixel_size, gradation_step)
            j = j + pixel_size
        i = i + pixel_size
    return arr


arr = image_to_pixelart('img2.jpg', 10, 50)

res = Image.fromarray(arr)
res.save('res.jpg')
