from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75BBFD',
            snow_color='#FFFAFA', trunk_color='#A45A52', needls_color='#01796F',
            sun_color='#FFDB00'):
    image = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(image)

    drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)),
                     snow_color)
    drawer.ellipse((
        (int(0.8 * width), -int(0.2 * height)),
        (int(1.2 * width), int(0.2 * height))),
        sun_color)
    drawer.rectangle(((0.45 * width, 0.9 * height), (0.55 * width, 0.7 * height)), trunk_color)
    drawer.polygon(((0.3 * width, 0.7 * height),
                    (0.4 * width, 0.5 * height),
                    (0.35 * width, 0.5 * height),
                    (0.45 * width, 0.3 * height),
                    (0.4 * width, 0.3 * height),
                    (0.5 * width, 0.1 * height),
                    (0.6 * width, 0.3 * height),
                    (0.55 * width, 0.3 * height),
                    (0.65 * width, 0.5 * height),
                    (0.6 * width, 0.5 * height),
                    (0.7 * width, 0.7 * height),
                    (0.3 * width, 0.7 * height)), needls_color)
    image.save(file_name)
