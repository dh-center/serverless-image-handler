import base64
import os
import uuid

from requests_toolbelt.multipart import decoder
import re
import boto3


def get_field_name(content_disposition):
    """Gets field name from Content-Disposition HTTP Header

    :param content_disposition: Header for parsing
    :type content_disposition: str

    :returns: Value of name field from header
    :rtype: str
    """
    parts = content_disposition.split(';')
    for part in parts:
        part_stripped = part.strip()
        search_result = re.search("^name=\"(.*)\"$", part_stripped)
        if search_result:
            return search_result.group(1)


def get_field_filename(content_disposition):
    """Gets field filename from Content-Disposition HTTP Header

    :param content_disposition: Header for parsing
    :type content_disposition: str

    :returns: Value of filename field from header
    :rtype: str
    """
    parts = content_disposition.split(';')
    for part in parts:
        part_stripped = part.strip()
        search_result = re.search("^filename=\"(.*)\"$", part_stripped)
        if search_result:
            return search_result.group(1)


def get_file_extension(file_name):
    """Gets file extension from filename.
    If can't get file extension returns None.

    :param file_name: File name
    :type file_name: str

    :returns: File extension (example: '.jpg')
    :rtype: str
    """
    file_extension = re.search('.[0-9a-z]+$', file_name, re.IGNORECASE).group(0)
    return file_extension or None


def save_to_bucket(image, file_extension):
    """Connects to S3 bucket and saves image to them

    :param image: Image for saving
    :type image: str

    :param file_extension: Extension of saving file
    :type file_extension: str

    :returns: Key of image in bucket
    :rtype: str
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


def handler(event, context):
    """Gets image from POST event and saves it to S3 bucket

    :param event: Yandex Cloud Function event
    :param context: Yandex Cloud Function context

    :returns: HTTP response with key of image in S3 bucket
    """
    content_type = event['headers']['Content-Type']
    decoded_request_body = base64.b64decode(event['body'])

    image = None
    file_extension = None

    for part in decoder.MultipartDecoder(decoded_request_body, content_type).parts:
        content_disposition = part.headers[b'Content-Disposition'].decode('utf-8')
        field_name = get_field_name(content_disposition)
        if field_name == 'image':
            image = part.content
        filename = get_field_filename(content_disposition)
        file_extension = get_file_extension(filename)

    if not image:
        raise IOError('Can\'t read image from request message.')

    if not file_extension:
        raise IOError('Can\'t get extension of file.')

    image_key = save_to_bucket(image, file_extension)

    return {
        'statusCode': 200,
        'headers': {
            'content-type': 'application/json'
        },
        'body': {
            'image-key': image_key
        }
    }
