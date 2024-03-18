from PIL import Image


def transparency(filename1, filename2):
    image_1 = Image.open(filename1)
    pixels = image_1.load()
    pixels_1 = image_1.load()
    pixels_2 = Image.open(filename2).load()
    x, y = image_1.size
    for i in range(x):
        for j in range(y):
            r1, g1, b1 = pixels_1[i, j]
            r2, g2, b2 = pixels_2[i, j]
            r, g, b = int(0.5 * r1 + 0.5 * r2), int(0.5 * g1 + 0.5 * g2), int(0.5 * b1 + 0.5 * b2)
            pixels[i, j] = r, g, b
    image_1.save('res.jpg')
