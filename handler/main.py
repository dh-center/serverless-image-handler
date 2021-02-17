# Function gets image from S3 by key
# Process image with filters
# And return image in response

from base64 import b64encode
import boto3
import os
import io
from yandex_types import YandexEvent
from PIL import Image, ImageFilter

from typing import TypedDict, Dict


class HandlerResponse(TypedDict):
    statusCode: int
    headers: Dict[str, str]
    body: str
    isBase64Encoded: bool


def handler(event: YandexEvent, context) -> HandlerResponse:
    """Gets image properties from request, load image from bucket, transforms it and returns

    :param event: Yandex Cloud Function event
    :param context: Yandex Cloud Function context

    :returns: HTTP response transformed image
    """
    params = event['queryStringParameters']
    image_key = params["key"]

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
    image = Image.open(io.BytesIO(image_from_bucket))

    if 'blur' in params:
        blur_radius = int(params['blur'])
        image = image.filter(ImageFilter.GaussianBlur(blur_radius))

    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = b64encode(buffered.getvalue())

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'image/jpeg'
        },
        'body': img_str.decode('utf-8'),
        'isBase64Encoded': True
    }
