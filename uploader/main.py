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


def save_to_bucket(image):
    """Connects to S3 bucket and saves image to them

    :param image: Image for saving
    :type image: str

    :returns: Key of image in bucket
    :rtype: str
    """
    s3_client = boto3.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    )

    image_key = str(uuid.uuid4)
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

    for part in decoder.MultipartDecoder(decoded_request_body, content_type).parts:
        content_disposition = part.headers[b'Content-Disposition'].decode('utf-8')
        field_name = get_field_name(content_disposition)
        if field_name == 'image':
            image = part.content

    if not image:
        raise IOError('Can\'t read image from request message.')

    image_key = save_to_bucket(image)

    return {
        'statusCode': 200,
        'headers': {
            'content-type': 'application/json'
        },
        'body': {
            'image-key': image_key
        }
    }
