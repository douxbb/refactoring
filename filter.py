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


arr = image_to_pixelart('img2.jpg', 10, 50)

res = Image.fromarray(arr)
res.save('res.jpg')
