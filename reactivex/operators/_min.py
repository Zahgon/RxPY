from collections.abc import Callable
from typing import TypeVar, cast

from reactivex import Observable
from reactivex import operators as ops
from reactivex.internal import curry_flip
from reactivex.internal.basic import identity
from reactivex.internal.exceptions import SequenceContainsNoElementsError
from reactivex.typing import Comparer

_T = TypeVar("_T")


def first_only(x: list[_T]) -> _T:
    pass


@curry_flip
def min_(
    source: Observable[_T],
    comparer: Comparer[_T] | None = None,
) -> Observable[_T]:
    """Returns the minimum element in an observable sequence.

    Returns the minimum element in an observable sequence according to
    the optional comparer else a default greater than less than check.

    Examples:
        >>> result = source.pipe(min())
        >>> result = min()(source)
        >>> result = source.pipe(min(lambda x, y: x.value - y.value))

    Args:
        source: The source observable.
        comparer: Optional comparer used to compare elements.

    Returns:
        An observable sequence containing a single element
        with the minimum element in the source sequence.
    """
    pass


__all__ = ["min_"]
