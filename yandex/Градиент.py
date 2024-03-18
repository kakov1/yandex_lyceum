from PIL import Image, ImageDraw


def gradient(color):
    image = Image.new('RGB', (512, 200), (0, 0, 0))
    drawer = ImageDraw.Draw(image)
    for i in range(256):
        if color.upper() == 'R':
            drawer.line((i + i, 0, i + i, 200), fill=(i, 0, 0), width=2)
        elif color.upper() == 'G':
            drawer.line((i + i, 0, i + i, 200), fill=(0, i, 0), width=2)
        elif color.upper() == 'B':
            drawer.line((i + i, 0, i + i, 200), fill=(0, 0, i), width=2)
    image.save('res.png')
