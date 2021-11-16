from PIL import Image
import numpy as np


def image_to_pixelart(filename, pixel_size, gradation_step):
    img = Image.open(filename)
    arr = np.array(img)
    height = len(arr)
    width = len(arr[1])

    for x in range(0, width, pixel_size):
        for y in range(0, height, pixel_size):
            sum_pixels_color = sum(map(lambda n: int(n) / 3, arr[y:y + pixel_size, x:x + pixel_size].flatten()))
            monochrome_color = int(sum_pixels_color / pixel_size ** 2 // gradation_step) * gradation_step
            arr[y:y + pixel_size, x:x + pixel_size] = monochrome_color
    return arr


filename = input('Image filename: ')
result_filename = input('Result image filename: ')
pixel_size = input("Pixel size (by default: 10): ")
pixel_size = int(pixel_size) if pixel_size else 10
gradation_step = input("Gradation step (by default 50): ")
gradation_step = int(gradation_step) if gradation_step else 50

arr = image_to_pixelart(filename, pixel_size, gradation_step)

res = Image.fromarray(arr)
res.save(result_filename)
