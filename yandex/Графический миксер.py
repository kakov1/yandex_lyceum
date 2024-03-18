from PIL import Image


def twist_image(input_file_name, output_file_name):
    image = Image.open(input_file_name)
    pixels = image.load()
    x, y = image.size
    pixels_1 = image.crop((0, 0, x // 2, y)).load()
    pixels_2 = image.crop((x // 2, 0, x, y)).load()
    for i in range(x // 2):
        for j in range(y):
            r, g, b = pixels_2[i, j]
            pixels[i, j] = r, g, b
    for i in range(x // 2):
        for j in range(y):
            r, g, b = pixels_1[i, j]
            pixels[i + x // 2, j] = r, g, b
    image.save(output_file_name)
