#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# form-data parser
def get_field_name(content_disposition):
    parts = content_disposition.split(';')
    for part in parts:
        part_stripped = part.strip()
        search_result = re.search("^name=\"(.*)\"$", part_stripped)

        if search_result:
            return search_result.group(1)


# decodes bytes function
def encode_file(image_file):
    return base64.b64encode(image_file)


# image-handler function
def handler(event, context):
    # data from HTTP request
    body = event['body']
    content_type = event['headers']['Content-Type']
    decoded_body = base64.b64decode(body)

    # separate the image in binary format from the data we don't need
    for part in decoder.MultipartDecoder(decoded_body, content_type).parts:
        content_disposition = part.headers[b'Content-Disposition'].decode('utf-8');
        field_name = get_field_name(content_disposition)
        image_file = part.content

    # create a variable 'image', which contains the image encoded into a byte string
    image = encode_file(image_file)

    # create a session and specify environment variables
    session = boto3.session.Session()

    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],

    )

    # upload the file to the bucket
    s3.put_object(Bucket='image-handler-bucket', Key='sample2.png', Body=image_file, StorageClass='STANDARD',
                  ContentType='image/png')

    return {
        'statusCode': 200,
        'headers': {
            'content-type': 'image/png'
        },
        'body': image.decode('utf-8'),
        'isBase64Encoded': True
    }

