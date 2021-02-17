from fastapi import FastAPI, Response
from handler.main import handler
from dotenv import load_dotenv
from base64 import b64decode as dec64

from yandex_types import YandexEvent

load_dotenv()

app = FastAPI()


@app.post("/upload")
def upload_image():
    return {"Hello": "World"}


@app.get("/handle")
def handle_image(key):
    event: YandexEvent = {
        "httpMethod": "GET",
        "headers": {},
        "queryStringParameters": {
            "key": key
        },
        "body": "",
        "isBase64Encoded": True
    }
    result = handler(event)

    return Response(content=dec64(result['body']), media_type="image/jpeg")
