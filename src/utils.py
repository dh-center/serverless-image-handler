import os
import re
import boto3
import uuid
from requests_toolbelt.multipart import decoder
import base64
from typing import Tuple


def get_file_format(filename: str) -> str:
    """
    Returns file format for Pillow lib from filename
    :param filename: name for getting file format
    :return: Pillow image format
    """
    file_extension_with_dot = get_file_extension(filename)
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


def get_file_extension(file_name: str) -> str:
    """
    Gets file extension from filename.
    If can't get file extension returns None.
    :param file_name: File name
    :returns: File extension (example: '.jpg')
    """
    _, file_extension = os.path.splitext(file_name)
    return file_extension


def save_to_bucket(image: bytes, file_extension: str) -> str:
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


def get_image_from_body(body: bytes, content_type: str) -> Tuple[bytes, str]:
    """
    Parses request body and returns image data from it
    :param body: body to parse
    :param content_type: content type to correctly parse body
    :return: image data
    """
    decoded_request_body = base64.b64decode(body)
    image = None
    file_extension = None

    for part in decoder.MultipartDecoder(decoded_request_body, content_type).parts:
        content_disposition = part.headers[b'Content-Disposition'].decode('utf-8')
        field_name = get_field_name(content_disposition)
        if field_name == 'image':
            image = part.content
        filename = get_field_filename(content_disposition)
        file_extension = get_file_extension(filename)

    return image, file_extension
