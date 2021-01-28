import json
import base64
from requests_toolbelt.multipart import decoder
import re
from base64 import b64encode as enc64
from base64 import b64decode as dec64
import PIL
from PIL import Image
import io
import boto3
import os
import uuid



# Парсер для form-data
def get_field_name(content_disposition):
    parts = content_disposition.split(';')
    for part in parts:
        part_stripped = part.strip()
        search_result = re.search("^name=\"(.*)\"$", part_stripped)
        
        if search_result:
            return search_result.group(1)

# Функция, которая декодирует байты
def encode_file(image_file):
    return base64.b64encode(image_file)

# Функция image-handler
def handler(event, context):
    # передаем данные из HTTP запроса
    body = event['body']
    content_type = event['headers']['Content-Type']
    decoded_body = base64.b64decode(body)
        
    # отделяем изображение в бинарном формате от ненужных нам данных                           
    for part in decoder.MultipartDecoder(decoded_body, content_type).parts: 
        content_disposition = part.headers[b'Content-Disposition'].decode('utf-8');
        field_name = get_field_name(content_disposition)
        image_file = part.content
    # создаем переменную image, в которой находится изображение закодированное в байтовую строку 
    image = encode_file(image_file)
    # создаем сессию и указываем переменные среды
    session = boto3.session.Session()
    
    s3 = session.client(
            service_name='s3',
            endpoint_url='https://storage.yandexcloud.net',
            aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],
            

     ) 


    generate_key = uuid.uuid4()
    
    # загружаем файл в бакет
    s3.put_object(Bucket=os.environ['BUKET'], Key= str(generate_key), Body=image_file, StorageClass='STANDARD')
    
    
    # достаем файл из бакета
    get_object_response = s3.get_object(Bucket=os.environ['BUKET'],Key= str(generate_key))#в скобках имя бакета и имя файла, в бакете
    image_from_buket = get_object_response['Body'].read()
    decoded_image = encode_file(image_from_buket)
    
   
    
    return {
        'statusCode': 200,
        'headers': {
        'content-type': 'image/png'
        },
        'body': decoded_image.decode('utf-8'),
        'isBase64Encoded': True
        }