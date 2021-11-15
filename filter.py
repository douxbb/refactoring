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
        pixel = 0
        for n in range(i, i + mosaic_size):
            for n1 in range(j, j + mosaic_size):
                r = int(arr[n][n1][0])
                g = int(arr[n][n1][1])
                b = int(arr[n][n1][2])
                average = (r + g + b) / 3
                pixel += average
        pixel = pixel // (100 * grayscale) * grayscale
        for n in range(i, i + mosaic_size):
            for n1 in range(j, j + mosaic_size):
                arr[n][n1] = pixel
        j = j + mosaic_size
    i = i + mosaic_size

res = Image.fromarray(arr)
res.save('res.jpg')
