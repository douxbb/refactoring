from PIL import Image
import numpy as np


def convert_img_to_pixel(image, size=10, gradation_step=5):
    arr_img = np.array(image)
    height = len(arr_img)
    width = len(arr_img[1])
    gradation = size * gradation_step
    for x in range(0, height, size):
        for y in range(0, width, size):
            sum_pixel = sum(arr_img[y:y + size, x:x + size].flatten())
            arr_img[y:y + size, x:x + size] = int(sum_pixel // (size * size) // gradation) * gradation / 3
    return arr_img


img = Image.open("img2.jpg")
res = Image.fromarray(convert_img_to_pixel(img))
res.save('res.jpg')
