from asyncio import Future
from typing import TypeVar, Union

import reactivex
from reactivex import Observable, abc
from reactivex.disposable import CompositeDisposable, SingleAssignmentDisposable
from reactivex.internal import curry_flip

_T = TypeVar("_T")


@curry_flip
def exclusive_(source: Observable[Observable[_T]]) -> Observable[_T]:
    """Performs a exclusive waiting for the first to finish before
    subscribing to another observable. Observables that come in between
    subscriptions will be dropped on the floor.

    Examples:
        >>> res = source.pipe(exclusive())
        >>> res = exclusive()(source)

    Args:
        source: Source observable of observables.

    Returns:
        An exclusive observable with only the results that
        happen when subscribed.
    """
    pass


__all__ = ["exclusive_"]
