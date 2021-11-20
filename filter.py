from PIL import Image
import numpy as np


def pixelizate(path_to_source, block_size=10, grey_value=5):
    arr = np.array(path_to_source)
    gradient = block_size * grey_value
    width = len(arr)
    height = len(arr[1])

    for i in range(0, width - block_size + 1, block_size):
        for j in range(0, height - block_size + 1, block_size):
            grey = 0

            for x in range(i, i + block_size):
                for y in range(j, j + block_size):
                    light = np.sum(arr[x][y])
                    grey += light / 3

            grey = int(grey // block_size ** 2)

            for x in range(i, i + block_size):
                for y in range(j, j + block_size):
                    block_grey = int(grey // gradient) * gradient
                    arr[x][y][0] = block_grey
                    arr[x][y][1] = block_grey
                    arr[x][y][2] = block_grey

    return arr


img_path = input('Введите путь до изображения:')
chunk_size = input('Введите размер блоков мозаики в пикселях (default 10):')
gray_scale = input('Введите шаг градации (default 5):')

img = Image.open(img_path)
res = Image.fromarray(pixelizate(img))
res.save('res.jpg')
print('Сохранено в файл res.jpg')
