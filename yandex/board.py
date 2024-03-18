from PIL import Image, ImageDraw

im = Image.new("RGB", (400, 400))
drawer = ImageDraw.Draw(im)
for i in range(8):
    for j in range(8):
        if i % 2:
            if not j % 2:
                drawer.rectangle(((j * 50, i * 50), ((j + 1) * 50, (i + 1) * 50)), '#b57335')
            else:
                drawer.rectangle(((j * 50, i * 50), ((j + 1) * 50, (i + 1) * 50)), '#ffcc99')
        else:
            if j % 2:
                drawer.rectangle(((j * 50, i * 50), ((j + 1) * 50, (i + 1) * 50)), '#b57335')
            else:
                drawer.rectangle(((j * 50, i * 50), ((j + 1) * 50, (i + 1) * 50)), '#ffcc99')
im.save('board.png')
