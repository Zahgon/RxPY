from asyncio import Future
from collections.abc import Callable
from typing import TypeVar

from reactivex import Observable, from_future, throw

_T = TypeVar("_T")


def start_async_(function_async: Callable[[], "Future[_T]"]) -> Observable[_T]:
    pass


__all__ = ["start_async_"]
