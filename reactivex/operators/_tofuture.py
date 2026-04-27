import asyncio
from asyncio import Future
from collections.abc import Callable
from typing import TypeVar, cast

from reactivex import Observable, abc
from reactivex.internal.exceptions import SequenceContainsNoElementsError

_T = TypeVar("_T")


def to_future_(
    future_ctor: Callable[[], Future[_T]] | None = None,
    scheduler: abc.SchedulerBase | None = None,
) -> Callable[[Observable[_T]], Future[_T]]:
    pass


__all__ = ["to_future_"]
