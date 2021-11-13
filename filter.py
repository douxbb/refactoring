from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 9:
    j = 0
    while j < a1 - 9:
        s = 0
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                n1 = int(arr[x][y][0])
                n2 = int(arr[x][y][1])
                n3 = int(arr[x][y][2])
                M = n1 + n2 + n3
                s += M / 3
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
