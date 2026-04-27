from typing import TypeVar

from reactivex import Observable, abc
from reactivex.internal import curry_flip, noop

_T = TypeVar("_T")


@curry_flip
def ignore_elements_(source: Observable[_T]) -> Observable[_T]:
    """Ignores all elements in an observable sequence leaving only the
    termination messages.

    Examples:
        >>> res = source.pipe(ignore_elements())
        >>> res = ignore_elements()(source)

    Args:
        source: The source observable sequence.

    Returns:
        An empty observable sequence that signals
        termination, successful or exceptional, of the source sequence.
    """
    pass


__all__ = ["ignore_elements_"]
