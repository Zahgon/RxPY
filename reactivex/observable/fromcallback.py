from collections.abc import Callable
from typing import Any

from reactivex import Observable, abc, typing
from reactivex.disposable import Disposable


def from_callback_(
    func: Callable[..., Callable[..., None]],
    mapper: typing.Mapper[Any, Any] | None = None,
) -> Callable[..., Observable[Any]]:
    """Converts a callback function to an observable sequence.

    Args:
        func: Function with a callback as the last argument to
            convert to an Observable sequence.
        mapper: [Optional] A mapper which takes the arguments
            from the callback to produce a single item to yield on next.

    Returns:
        A function, when executed with the required arguments minus
        the callback, produces an Observable sequence with a single value of
        the arguments to the callback as a list.
    """
    pass


__all__ = ["from_callback_"]
