import json
import base64
# import requests_toolbelt
# from requests_toolbelt.multipart import decoder
# import re
from base64 import b64encode as enc64
from base64 import b64decode as dec64
# import PIL
# from PIL import Image
# import io
import boto3
import os

# Функция, которая декодирует байты
def encode_file(image_file):
    return base64.b64encode(image_file)

# Функция image-handler
def handler(event, context):
    # передаем данные из HTTP запроса
    body = event['queryStringParameters']
    # content_type = event['headers']['Content-Type']
    # decoded_body = base64.b64decode(body)
    
    session = boto3.session.Session()
    
    s3 = session.client(
            service_name='s3',
            endpoint_url='https://storage.yandexcloud.net',
            aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],
           

      ) 

    image_key = body['key ']
    # достаем файл из бакета
    get_object_response = s3.get_object(Bucket= os.environ['BUKET'],Key= image_key )#в скобках имя бакета и имя файла, в бакете
    image_from_buket = get_object_response['Body'].read()
    decoded_image = encode_file(image_from_buket)
    
    
    return {
        'statusCode': 200,
        # 'headers': {
        # 'content-type': 'image/png'
        # },
        'body': decoded_image.decode('utf-8'),
        # 'body': image_key
        # 'isBase64Encoded': True
        }