from PIL import Image
import numpy as np


def get_average_rgb(local_x, local_y):
    global img_matrix
    n1 = img_matrix[local_x][local_y][0]
    n2 = img_matrix[local_x][local_y][1]
    n3 = img_matrix[local_x][local_y][2]
    return (int(n1) + int(n2) + int(n3)) // 3


CELL_X_OFFSET = 10
CELL_Y_OFFSET = 10
GREY_GRADATION = 50
img = Image.open(
    "C:\\Users\Статик\Desktop\\refactoring\img2.jpg")  # по какой-то причине не работает относительный адрес к картинке
img_matrix = np.array(img)
len_x = len(img_matrix)
len_y = len(img_matrix[1])
cell_x = 0
while cell_x < len_x:
    cell_y = 0
    while cell_y < len_y:
        sum_RGB = 0
        for x in range(cell_x, cell_x + CELL_X_OFFSET):
            for y in range(cell_y, cell_y + CELL_Y_OFFSET):
                sum_RGB += get_average_rgb(x, y)
        sum_RGB = int(sum_RGB // 100)
        for x in range(cell_x, cell_x + CELL_X_OFFSET):
            for y in range(cell_y, cell_y + CELL_Y_OFFSET):
                img_matrix[x][y][0] = int(sum_RGB // GREY_GRADATION) * GREY_GRADATION
                img_matrix[x][y][1] = int(sum_RGB // GREY_GRADATION) * GREY_GRADATION
                img_matrix[x][y][2] = int(sum_RGB // GREY_GRADATION) * GREY_GRADATION
        cell_y = cell_y + CELL_Y_OFFSET
    cell_x = cell_x + CELL_X_OFFSET
res = Image.fromarray(img_matrix)
res.save('C:\\Users\Статик\Desktop\\refactoring\\res.jpg')  # то же самое что и в первом случае
