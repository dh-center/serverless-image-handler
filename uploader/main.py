import base64
from requests_toolbelt.multipart import decoder
from utils import save_to_bucket, get_file_extension, get_field_filename, get_field_name
from yandex_types import YandexEvent


def handler(event: YandexEvent, context):
    """
    Gets image from POST event and saves it to S3 bucket

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
