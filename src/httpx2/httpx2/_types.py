"""
Type definitions for type checking purposes.
"""

import typing
from http.cookiejar import CookieJar
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    AsyncIterable,
    AsyncIterator,
    Callable,
    Iterable,
    Iterator,
    Mapping,
    Sequence,
)

if TYPE_CHECKING:
    from ._auth import Auth  # noqa: F401
    from ._config import Proxy, Timeout  # noqa: F401
    from ._models import Cookies, Headers, Request  # noqa: F401
    from ._urls import URL, QueryParams  # noqa: F401


PrimitiveData = typing.Union[str, int, float, bool, None]

URLTypes = typing.Union["URL", str]

QueryParamTypes = typing.Union[
    "QueryParams",
    Mapping[str, typing.Union[PrimitiveData, Sequence[PrimitiveData]]],
    typing.List[typing.Tuple[str, PrimitiveData]],
    typing.Tuple[typing.Tuple[str, PrimitiveData], ...],
    str,
    bytes,
]

HeaderTypes = typing.Union[
    "Headers",
    Mapping[str, str],
    Mapping[bytes, bytes],
    Sequence[typing.Tuple[str, str]],
    Sequence[typing.Tuple[bytes, bytes]],
]

CookieTypes = typing.Union["Cookies", CookieJar, typing.Dict[str, str], typing.List[typing.Tuple[str, str]]]

TimeoutTypes = typing.Union[
    typing.Optional[float],
    typing.Tuple[typing.Optional[float], typing.Optional[float], typing.Optional[float], typing.Optional[float]],
    "Timeout",
]
ProxyTypes = typing.Union["URL", str, "Proxy"]
CertTypes = typing.Union[str, typing.Tuple[str, str], typing.Tuple[str, str, str]]

AuthTypes = typing.Union[
    typing.Tuple[typing.Union[str, bytes], typing.Union[str, bytes]],
    Callable[["Request"], "Request"],
    "Auth",
]

RequestContent = typing.Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]
ResponseContent = typing.Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]
ResponseExtensions = Mapping[str, Any]

RequestData = Mapping[str, Any]

FileContent = typing.Union[IO[bytes], bytes, str]
FileTypes = typing.Union[
    # file (or bytes)
    FileContent,
    # (filename, file (or bytes))
    typing.Tuple[typing.Optional[str], FileContent],
    # (filename, file (or bytes), content_type)
    typing.Tuple[typing.Optional[str], FileContent, typing.Optional[str]],
    # (filename, file (or bytes), content_type, headers)
    typing.Tuple[typing.Optional[str], FileContent, typing.Optional[str], Mapping[str, str]],
]
RequestFiles = typing.Union[Mapping[str, FileTypes], Sequence[typing.Tuple[str, FileTypes]]]

RequestExtensions = Mapping[str, Any]

__all__ = ["AsyncByteStream", "SyncByteStream"]


class SyncByteStream:
    def __iter__(self) -> Iterator[bytes]:
        raise NotImplementedError("The '__iter__' method must be implemented.")  # pragma: no cover
        yield b""  # pragma: no cover

    def close(self) -> None:
        """
        Subclasses can override this method to release any network resources
        after a request/response cycle is complete.
        """


class AsyncByteStream:
    async def __aiter__(self) -> AsyncIterator[bytes]:
        raise NotImplementedError("The '__aiter__' method must be implemented.")  # pragma: no cover
        yield b""  # pragma: no cover

    async def aclose(self) -> None:
        pass
