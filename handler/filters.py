from PIL import Image, ImageFilter


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


filters = {
    'blur': blur,
    'pixelate': pixelate
}
