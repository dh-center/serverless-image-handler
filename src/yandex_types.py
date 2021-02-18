from typing import TypedDict, Dict, Union, Mapping, Callable, Any


class YandexEvent(TypedDict):
    httpMethod: str
    headers: Mapping[str, str]
    body: Union[str, bytes]
    queryStringParameters: Dict[str, str]
    isBase64Encoded: bool


class YandexResponse(TypedDict):
    statusCode: int
    headers: Dict[str, str]
    body: Union[dict, str]
    isBase64Encoded: bool


HandlerFunction = Callable[[YandexEvent, Any], YandexResponse]
