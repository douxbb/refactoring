from PIL import Image
import numpy as np


def convert_to_pixelart(image, chunk_size=10, grey_gradation=5):
    arr = np.array(image)
    gradient = chunk_size * grey_gradation
    for x in range(0, arr.shape[0], chunk_size):
        for y in range(0, arr.shape[1], chunk_size):
            grey = sum(map(lambda n: int(n) / 3, arr[x:x + chunk_size, y:y + chunk_size].flatten()))
            grey = int(grey / chunk_size ** 2 // gradient) * gradient
            arr[x:x + chunk_size, y:y + chunk_size] = grey
    return arr


mage_name = input("Введите название файла изображения: ")

mosaic = input("Введите размер мозайки(или нажмите Ввод для значения по-умолчанию - 10): ")
mosaic = int(mosaic) if mosaic else 10

gradation = input("Введите шаг градации(или нажмите Ввод для значения по-умолчанию - 5): ")
gradation = int(gradation) if gradation else 5

img = Image.open(image_name)
res = Image.fromarray(convert_to_pixelart(img, mosaic, gradation))
res.save('res.jpg')
print("Результат сохранён как res.jpg")
