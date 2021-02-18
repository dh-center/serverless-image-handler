from base64 import b64encode
import boto3
import os
import io
from src.utils import get_file_format, handle_cors
from src.yandex_types import YandexEvent, YandexResponse
from PIL import Image
import mimetypes
from src.filters import filters
from typing import Any


@handle_cors
def handler(event: YandexEvent, context: Any) -> YandexResponse:
    """Gets image properties from request, load image from bucket, transforms it and returns

    :param event: Yandex Cloud Function event
    :param context: Yandex Cloud Function context

    :returns: HTTP response transformed image
    """

    params = event['queryStringParameters']
    image_key = params["key"]
    mimetype = mimetypes.guess_type(image_key)[0]
    file_format = get_file_format(image_key)

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

    for param_name, param_value in params.items():
        if param_name in filters:
            image = filters[param_name](image, param_value)

    buffered = io.BytesIO()
    image.save(buffered, format=file_format)
    img_str = b64encode(buffered.getvalue())

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': mimetype
        },
        'body': img_str.decode('utf-8'),
        'isBase64Encoded': True
    }
