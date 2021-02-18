from src.utils import save_to_bucket, get_image_from_body
from src.yandex_types import YandexEvent


def handler(event: YandexEvent, context):
    """
    Gets image from POST event and saves it to S3 bucket

    :param event: Yandex Cloud Function event
    :param context: Yandex Cloud Function context

    :returns: HTTP response with key of image in S3 bucket
    """
    content_type = event['headers']['Content-Type']

    image, file_extension = get_image_from_body(event['body'], content_type)

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
