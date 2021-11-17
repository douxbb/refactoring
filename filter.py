from PIL import Image
import numpy as np


def get_greyscaled_pixels(step_width, mosaic_size, step_height, graid, img_arr, greyscale):

    for x in range(step_width, step_width + mosaic_size):
        for y in range(step_height, step_height + mosaic_size):
            for z in range(0,3):
                img_arr[x][y][z] = int(greyscale // graid) * graid

    return img_arr


def get_pixels_greyscale(step_width, mosaic_size, step_height, img_arr):

    img_segment = img_arr[step_width:step_width + mosaic_size,
                  step_height:step_height + mosaic_size]

    result = np.sum(img_segment)

    return int(result // (3 * (mosaic_size ** 2)))


def get_mosaic(graid, img_width, img_height, mosaic_size, img_arr):

    step_width = 0

    while step_width < img_width:

        step_height = 0

        while step_height < img_height:

            greyscale = get_pixels_greyscale(step_width, mosaic_size, step_height, img_arr)

            img_arr = get_greyscaled_pixels(step_width, mosaic_size, step_height, graid, img_arr, greyscale)

            step_height += mosaic_size
        step_width += mosaic_size

    return img_arr


def main():
    img_input = "img2.jpg"
    img_output = '1112sdad.jpg'
    img = Image.open(img_input)
    img_arr = np.array(img, dtype=np.uint32)
    img_width = len(img_arr)
    img_height = len(img_arr[1])
    mosaic_size = 10
    step_gray = 5
    graid = 255 / step_gray

    mosaic = get_mosaic(graid, img_width, img_height, mosaic_size, img_arr)
    res = Image.fromarray(mosaic.astype(np.uint8))
    res.save(img_output)


main()