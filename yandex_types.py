from typing import TypedDict, Dict


class YandexEvent(TypedDict):
    httpMethod: str
    headers: Dict[str, str]
    body: str
    queryStringParameters: Dict[str, str]
    isBase64Encoded: bool
