from PIL import Image
import numpy as np


def convert_to_pixelart(image, chunk_size=10, grey_gradation=5):
    arr = np.array(image)
    gradient = chunk_size * grey_gradation
    width = len(arr)
    height = len(arr[1])
    for i in range(0, width - chunk_size + 1, chunk_size):
        for j in range(0, height - chunk_size + 1, chunk_size):
            grey = count_grey(arr, chunk_size, i, j)
            for x in range(i, i + chunk_size):
                for y in range(j, j + chunk_size):
                    local_grey = int(grey // gradient) * gradient
                    arr[x][y][0] = local_grey
                    arr[x][y][1] = local_grey
                    arr[x][y][2] = local_grey
    return arr


def count_grey(arr, chunk_size, i, j):
    grey = 0
    for x in range(i, i + chunk_size):
        for y in range(j, j + chunk_size):
            red = int(arr[x][y][0])
            green = int(arr[x][y][1])
            blue = int(arr[x][y][2])
            grey += (red + green + blue) / 3
    return int(grey // chunk_size ** 2)


img = Image.open("img2.jpg")
res = Image.fromarray(convert_to_pixelart(img))
res.save('res.jpg')
