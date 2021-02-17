from PIL import Image, ImageFilter, ImageOps


def blur(image, params):
    """
    Blur filter
    :param image: image to transform
    :param params: params for transformation
    :return: transformed image
    """
    blur_radius = int(params)
    image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return image


def pixelate(image, params):
    """
    Pixelate filter
    :param image: image to transform
    :param params: params for transformation
    :return: transformed image
    """
    pixel_size = int(params)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    return image


def grayscale(image, params):
    return ImageOps.grayscale(image)


def scale(image, params):
    factor = int(params)
    return ImageOps.scale(image, factor)


def flip(image, params):
    return ImageOps.flip(image)


def invert(image, params):
    return ImageOps.invert(image)


def mirror(image, params):
    return ImageOps.mirror(image)


def posterize(image, params):
    bits = int(params)
    return ImageOps.posterize(image, bits)


def solarize(image, params):
    threshold = int(params)
    return ImageOps.solarize(image, threshold)


filters = {
    'blur': blur,
    'pixelate': pixelate,
    'grayscale': grayscale,
    'scale': scale,
    'flip': flip,
    'invert': invert,
    'mirror': mirror,
    'posterize': posterize,
    'solarize': solarize,
}
