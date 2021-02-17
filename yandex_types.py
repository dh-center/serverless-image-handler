from typing import TypedDict, Dict, Union, Mapping


class YandexEvent(TypedDict):
    httpMethod: str
    headers: Mapping[str, str]
    body: Union[str, bytes]
    queryStringParameters: Dict[str, str]
    isBase64Encoded: bool
