from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 1:
    j = 0
    while j < a1 - 1:
        s = 0
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                n1 = arr[x][y][0] / 3
                n2 = arr[x][y][1] / 3
                n3 = arr[x][y][2] / 3
                M = n1 + n2 + n3
                s += M
        s = int(s // 100)
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                arr[x][y][0] = int(s // 50) * 50
                arr[x][y][1] = int(s // 50) * 50
                arr[x][y][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
