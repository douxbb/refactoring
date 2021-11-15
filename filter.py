from PIL import Image
import numpy as np


def convert_img_to_pixel(image, size=10, gradation_step=5):
    arr_img = np.array(image)
    height = len(arr_img)
    width = len(arr_img[1])
    gradation = size * gradation_step
    for i in range(0, height - 1, size):
        for j in range(0, width - 1, size):
            grey = get_grey(arr_img, i, j, size)
            for x in range(i, i + size):
                for y in range(j, j + size):
                    grey_pixel = int(grey // gradation) * gradation / 3
                    arr_img[x][y][0] = grey_pixel
                    arr_img[x][y][1] = grey_pixel
                    arr_img[x][y][2] = grey_pixel
    return arr_img


def get_grey(arr, i, j, size):
    grey = 0
    for x in range(i, i + size):
        for y in range(j, j + size):
            red = int(arr[x][y][0])
            green = int(arr[x][y][1])
            blue = int(arr[x][y][2])
            grey += red + green + blue
    return int(grey // (size * size))


img = Image.open("img2.jpg")
res = Image.fromarray(convert_img_to_pixel(img))
res.save('res.jpg')
