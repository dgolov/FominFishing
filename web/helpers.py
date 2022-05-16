from PIL import Image, ImageEnhance


def auto_make_watermark(filepath):
    """ Наложение водяного знака на изображения
    :param filepath: путь к изображению
    """
    image = Image.open(filepath)
    watermark = Image.open('static/img/logo.png')

    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(0.1)
    watermark.putalpha(alpha)
    layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
    for y in range(0, image.size[1], int(watermark.size[1] / 2)):
        for x in range(0, image.size[0], int(watermark.size[0] / 2)):
            layer.paste(watermark, (x, y))
    new_image = Image.composite(layer, image, layer)
    new_image.save(filepath)


if __name__ == '__main__':
    auto_make_watermark('/Users/dgolov/PycharmProjects/FominFishing/media/photos/photo_2022-04-10_17.13.19.jpeg')