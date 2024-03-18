from PIL import Image, ImageDraw


def board(num, size):
    image = Image.new('RGB', (num * size, num * size), (255, 255, 255))
    drawer = ImageDraw.Draw(image)
    for i in range(num):
        for j in range(num):
            if i % 2:
                if j % 2:
                    drawer.rectangle(((j * size, i * size), (j * size + size - 1, i * size + size - 1)), (0, 0, 0))
            else:
                if not j % 2:
                    drawer.rectangle(((j * size, i * size), (j * size + size - 1, i * size + size - 1)), (0, 0, 0))
    image.save('res.png')
