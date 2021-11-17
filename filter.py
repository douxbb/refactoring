from PIL import Image
import numpy as np
img_input = "img2.jpg"
img_output = 'res.jpg'
img = Image.open(img_input)
img_arr = np.array(img, dtype=np.uint32)
img_width = len(img_arr)
img_height = len(img_arr[1])
i = 0
while i < img_width:
    j = 0
    while j < img_height:
        s = 0
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                n1 = img_arr[x][y][0]
                n2 = img_arr[x][y][1]
                n3 = img_arr[x][y][2]
                M = (n1 + n2 + n3) // 3
                s += M
        s = int(s // 100)
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                img_arr[x][y][0] = int(s // 50) * 50
                img_arr[x][y][1] = int(s // 50) * 50
                img_arr[x][y][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(img_arr.astype(np.uint8))
res.save(img_output)
