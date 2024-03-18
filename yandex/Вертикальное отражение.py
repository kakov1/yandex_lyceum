from PIL import Image


def mirror():
    image = Image.open('image.jpg')
    pixels = image.load()
    image_new = Image.open('image.jpg')
    pixels_new = image_new.load()
    x, y = image.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels_new[abs(x - i - 1), j] = r, g, b
    image_new.save('res.jpg')
