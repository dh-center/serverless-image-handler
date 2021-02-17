import os


def get_file_format(filename: str) -> str:
    """
    Returns file format for Pillow lib from filename
    :param filename: name for getting file format
    :return: Pillow image format
    """
    filename, file_extension_with_dot = os.path.splitext(filename)
    file_extension = file_extension_with_dot[1:]

    if file_extension == 'jpg':
        file_extension = 'jpeg'

    return file_extension
