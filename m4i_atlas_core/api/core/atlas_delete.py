from typing import Any, Awaitable, Dict, Optional

from aiohttp import ClientResponse, ClientSession

from ...config import ConfigStore
from .handle_request import R, ResponseParser, handle_request

HEADERS = {
    'Content-Type': 'application/json'
}

config = ConfigStore.get_instance()


def atlas_delete(
    path: str,
    headers: Dict[str, str] = HEADERS,
    params: Dict[str, Any] = None,
    parser: ResponseParser[R] = ClientResponse.text,
    access_token: Optional[str] = None
) -> Awaitable[R]:

    def request_factory(url: str, session: ClientSession):
        return session.delete(
            url=url,
            headers=headers,
            params=params,
            verify_ssl=False
        )
    # END request_factory

    return handle_request(
        path=path,
        request_factory=request_factory,
        response_parser=parser,
        access_token=access_token
    )
# END atlas_delete
