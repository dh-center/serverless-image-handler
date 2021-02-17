from fastapi import FastAPI, Response
from handler.main import handler
from dotenv import load_dotenv
from base64 import b64decode as dec64

load_dotenv()

app = FastAPI()


@app.post("/upload")
def upload_image():
    return {"Hello": "World"}


@app.get("/handle")
def handle_image():
    event = {
        "httpMethod": "GET",
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Cache-Control": "no-cache",
            "Postman-Token": "7e7e5725-fae3-4461-a605-0e0447894dec",
            "User-Agent": "PostmanRuntime/7.26.8",
            "X-Real-Remote-Address": "[37.120.217.39]:55406",
            "X-Request-Id": "53a69cdc-7574-4fd8-b4f4-f6b510f1dd2a",
            "X-Trace-Id": "f00216e6-5593-4a00-bd5d-d4aca2e901b3"
        },
        "url": "",
        "params": {},
        "multiValueParams": {},
        "pathParams": {},
        "multiValueHeaders": {
            "Accept": [
                "*/*"
            ],
            "Accept-Encoding": [
                "gzip, deflate, br"
            ],
            "Cache-Control": [
                "no-cache"
            ],
            "Postman-Token": [
                "7e7e5725-fae3-4461-a605-0e0447894dec"
            ],
            "User-Agent": [
                "PostmanRuntime/7.26.8"
            ],
            "X-Real-Remote-Address": [
                "[37.120.217.39]:55406"
            ],
            "X-Request-Id": [
                "53a69cdc-7574-4fd8-b4f4-f6b510f1dd2a"
            ],
            "X-Trace-Id": [
                "f00216e6-5593-4a00-bd5d-d4aca2e901b3"
            ]
        },
        "queryStringParameters": {
            "key": "156e9336-01bb-4c9c-a405-36dc226f68bb.jpg"
        },
        "multiValueQueryStringParameters": {
            "key": [
                "156e9336-01bb-4c9c-a405-36dc226f68bb.jpg"
            ]
        },
        "requestContext": {
            "identity": {
                "sourceIp": "37.120.217.39",
                "userAgent": "PostmanRuntime/7.26.8"
            },
            "httpMethod": "GET",
            "requestId": "53a69cdc-7574-4fd8-b4f4-f6b510f1dd2a",
            "requestTime": "17/Feb/2021:12:32:42 +0000",
            "requestTimeEpoch": 1613565162
        },
        "body": "",
        "isBase64Encoded": True
    }
    result = handler(event)

    return Response(content=dec64(result['body']), media_type="image/jpeg")
