from PIL import Image


def mirror():
    image = Image.open('image.jpg')
    pixels = image.load()
    image_new = Image.open('image.jpg')
    pixels_new = image_new.load()
    x, y = image.size
    for i in range(y):
        for j in range(x):
            r, g, b = pixels[x - j - 1, y - i - 1]
            pixels_new[i, j] = r, g, b
    image_new.save('res.jpg')
