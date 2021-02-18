from PIL import Image, ImageFilter, ImageOps


def blur(image: Image, params: str) -> Image:
    """
    Blur filter
    :param image: image to transform
    :param params: params for transformation
    :return: transformed image
    """
    blur_radius = int(params)
    image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return image


def pixelate(image: Image, params: str) -> Image:
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


def grayscale(image: Image, params: str) -> Image:
    """
    Convert the image to grayscale
    :param image: image to transform
    :param params: params for transformation
    :return: transformed image
    """
    return ImageOps.grayscale(image)


def scale(image: Image, params: str) -> Image:
    """
    Returns a rescaled image by a specific factor given in parameter
    :param image: image to transform
    :param params: Scale factor. Factor greater than 1 expands the image, between 0 and 1 contracts the image.
    :return: transformed image
    """
    factor = int(params)
    return ImageOps.scale(image, factor)


def flip(image: Image, params: str) -> Image:
    """
    Flip the image vertically (top to bottom).
    :param image: image to transform
    :param params: params for transformation
    :return: transformed image
    """
    return ImageOps.flip(image)


def invert(image: Image, params: str) -> Image:
    """
    Invert (negate) the image.
    :param image: image to transform
    :param params: params for transformation
    :return: transformed image
    """
    return ImageOps.invert(image)


def mirror(image: Image, params: str) -> Image:
    """
    Flip image horizontally (left to right).
    :param image: image to transform
    :param params: params for transformation
    :return: transformed image
    """
    return ImageOps.mirror(image)


def posterize(image: Image, params: str) -> Image:
    """
    Reduce the number of bits for each color channel.
    :param image: image to transform
    :param params: bits — The number of bits to keep for each channel (1-8)
    :return: transformed image
    """
    bits = int(params)
    return ImageOps.posterize(image, bits)


def solarize(image: Image, params: str) -> Image:
    """
    Invert all pixel values above a threshold.
    :param image: image to transform
    :param params: threshold – all pixels above this greyscale level are inverted
    :return: transformed image
    """
    threshold = int(params)
    return ImageOps.solarize(image, threshold)


def equalize(image: Image, params: str) -> Image:
    """
    Equalize the image histogram.
    This function applies a non-linear mapping to the input image,
    in order to create a uniform distribution of grayscale values in the output image.
    :param image: image to transform
    :param params: params for transformation
    :return: transformed image
    """
    return ImageOps.equalize(image)


def resize(image: Image, params: str) -> Image:
    """
    Returns resized image.
    :param image: image to transform
    :param params: width and height for resizing in form 200x300 or 200 (width=height)
    :return: transformed image
    """
    dimensions = params.split('x')
    if len(dimensions) == 2:
        width, height = map(int, dimensions)
    else:
        width = int(dimensions[0])
        height = width

    return image.resize((width, height))


def crop(image: Image, params: str) -> Image:
    """
    Returns a rectangular region from provided image
    :param image: image to transform
    :param params: params for transformation
    :return: transformed image
    """
    split_params = params.split('&')

    if len(split_params) == 2:
        dimensions, start_point = split_params
    else:
        dimensions = split_params[0]
        start_point = '0,0'

    split_dimensions = dimensions.split('x')

    if len(split_dimensions) == 2:
        width, height = map(int, split_dimensions)
    else:
        width = int(split_dimensions[0])
        height = width

    x, y = map(int, start_point.split(','))

    return image.crop((x, y, width + x, height + y))


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
    'equalize': equalize,
    'resize': resize,
    'crop': crop,
}
