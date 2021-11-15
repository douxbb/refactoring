import numpy as np
from PIL import Image

img = Image.open("img2.jpg")
arr = np.array(img)
height = len(arr)
width = len(arr[1])
mosaic_size = 10;
grayscale = 50;

i = 0
while i < height:
    j = 0
    while j < width:
        pixel = arr[i: i + mosaic_size, j: j + mosaic_size]
        pixel_color = (pixel.sum() / 3) // (100 * grayscale) * grayscale
        new_pixel = np.full(300, pixel_color).reshape(10, 10, 3)
        arr[i: i + mosaic_size, j: j + mosaic_size] = new_pixel
        j = j + mosaic_size
    i = i + mosaic_size

res = Image.fromarray(arr)
res.save('res.jpg')
