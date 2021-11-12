from PIL import Image
import numpy as np


def convert_image_to_pixelart(image, chunk_size=10, grey_gradation=5):
    arr = np.array(image)
    gradient = chunk_size * grey_gradation

    for x in range(0, arr.shape[0], chunk_size):
        for y in range(0, arr.shape[1], chunk_size):
            grey = sum(map(lambda n: int(n)/3, arr[x:x+chunk_size, y:y+chunk_size].flatten()))
            grey = int(grey / chunk_size ** 2 // gradient) * gradient

            arr[x:x+chunk_size, y:y+chunk_size] = grey

    return arr


img = Image.open("img2.jpg")
res = Image.fromarray(convert_image_to_pixelart(img))
res.save('res.jpg')
