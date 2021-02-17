from fastapi import FastAPI, Response, Request
from handler.main import handler
from uploader.main import handler as uploader
from dotenv import load_dotenv
import base64

from yandex_types import YandexEvent

load_dotenv()

app = FastAPI()


@app.post("/upload")
async def upload_image(request: Request):
    event: YandexEvent = {
        "httpMethod": "POST",
        "headers": request.headers,
        "queryStringParameters": {},
        "body": base64.b64encode(await request.body()),
        "isBase64Encoded": True
    }
    result = uploader(event, {})
    return result


@app.get("/handle")
def handle_image(request: Request):
    event: YandexEvent = {
        "httpMethod": "GET",
        "headers": {},
        "queryStringParameters": dict(request.query_params),
        "body": "",
        "isBase64Encoded": False
    }
    result = handler(event, {})

    return Response(content=base64.b64decode(result['body']), media_type=result['headers']['Content-Type'])
