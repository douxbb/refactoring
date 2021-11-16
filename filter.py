from PIL import Image
import numpy as np

correct_path = False
CELL_X_OFFSET = 10
CELL_Y_OFFSET = 10
GREY_GRADATION = 50
while not correct_path:
    img_path = input("Enter path to image for filtering: ")
    try:
        img = Image.open(img_path)
        correct_path = True
    except:
        print("Incorrect path/file format, please try again")
img_matrix = np.array(img)
len_x = len(img_matrix)
len_y = len(img_matrix[1])
cell_x = 0
while cell_x < len_x:
    cell_y = 0
    while cell_y < len_y:
        sum_RGB = 0
        sum_RGB += np.sum(img_matrix[cell_x:cell_x + CELL_X_OFFSET, cell_y:cell_y + CELL_Y_OFFSET]) // 3
        sum_RGB = int(sum_RGB // 100)
        grey_matrix = np.zeros((CELL_X_OFFSET, CELL_Y_OFFSET, 3))
        grey_matrix[:] = int(sum_RGB // GREY_GRADATION) * GREY_GRADATION
        img_matrix[cell_x:cell_x + CELL_X_OFFSET, cell_y:cell_y + CELL_Y_OFFSET] = grey_matrix
        cell_y = cell_y + CELL_Y_OFFSET
    cell_x = cell_x + CELL_X_OFFSET
res = Image.fromarray(img_matrix)
correct_path = False
while not correct_path:
    res_path = input("Enter path to resulting image: ")
    try:
        res.save(res_path)
        correct_path = True
    except:
        print("Incorrect path/file format, please try again")
