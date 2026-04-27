from collections.abc import Callable
from threading import RLock, Thread
from typing import Any, TypeVar

from typing_extensions import ParamSpec

from reactivex.typing import StartableTarget

_T = TypeVar("_T")
_P = ParamSpec("_P")


def default_thread_factory(target: StartableTarget) -> Thread:
    pass


def synchronized(lock: RLock) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    """A decorator for synchronizing access to a given function."""

    def wrapper(fn: Callable[_P, _T]) -> Callable[_P, _T]:
        pass

    return wrapper
