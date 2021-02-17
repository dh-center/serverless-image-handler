import os
import re
import boto3
import uuid


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


def get_field_name(content_disposition: str) -> str:
    """
    Gets field name from Content-Disposition HTTP Header
    :param content_disposition: Header for parsing
    :returns: Value of name field from header
    """
    parts = content_disposition.split(';')
    for part in parts:
        part_stripped = part.strip()
        search_result = re.search("^name=\"(.*)\"$", part_stripped)
        if search_result:
            return search_result.group(1)


def get_field_filename(content_disposition: str) -> str:
    """
    Gets field filename from Content-Disposition HTTP Header
    :param content_disposition: Header for parsing
    :returns: Value of filename field from header
    """
    parts = content_disposition.split(';')
    for part in parts:
        part_stripped = part.strip()
        search_result = re.search("^filename=\"(.*)\"$", part_stripped)
        if search_result:
            return search_result.group(1)


def get_file_extension(file_name):
    """
    Gets file extension from filename.
    If can't get file extension returns None.

    :param file_name: File name
    :type file_name: str

    :returns: File extension (example: '.jpg')
    :rtype: str
    """
    file_extension = re.search('.[0-9a-z]+$', file_name, re.IGNORECASE).group(0)
    return file_extension or None


def save_to_bucket(image: str, file_extension: str) -> str:
    """
    Connects to S3 bucket and saves image to them
    :param image: Image for saving
    :param file_extension: Extension of saving file
    :returns: Key of image in bucket
    """
    s3_client = boto3.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    )

    image_key = str(uuid.uuid4()) + file_extension
    s3_client.put_object(
        Bucket=os.environ['BUCKET_ID'],
        Key=image_key,
        Body=image,
        StorageClass='STANDARD'
    )
    return image_key
