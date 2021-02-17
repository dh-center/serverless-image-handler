# Function gets image from S3 by key
# Process image with filters
# And return image in response

from base64 import b64encode
import boto3
import os
from yandex_types import YandexEvent
from PIL import Image, ImageFilter

from typing import TypedDict, Dict


class HandlerResponse(TypedDict):
    statusCode: int
    headers: Dict[str, str]
    body: str
    isBase64Encoded: bool


# Функция, которая декодирует байты
def encode_file(image_file):
    return b64encode(image_file)


# Функция image-handler
def handler(event: YandexEvent) -> HandlerResponse:
    body = event['queryStringParameters']
    image_key = body["key"]

    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    )

    get_object_response = s3.get_object(
        Bucket=os.environ['BUCKET_ID'],
        Key=image_key
    )
    image_from_bucket = get_object_response['Body'].read()
    decoded_image = encode_file(image_from_bucket)

    return {
        'statusCode': 200,
        'headers': {
            'content-type': 'image/png'
        },
        'body': decoded_image.decode('utf-8'),
        'isBase64Encoded': True
    }
