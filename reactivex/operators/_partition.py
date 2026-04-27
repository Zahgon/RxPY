from typing import TypeVar

from reactivex import Observable
from reactivex import operators as ops
from reactivex.internal import curry_flip
from reactivex.typing import Predicate, PredicateIndexed

_T = TypeVar("_T")


@curry_flip
def partition_(
    source: Observable[_T],
    predicate: Predicate[_T],
) -> list[Observable[_T]]:
    """Returns two observables which partition the observations of the
    source by the given function.

    The first will trigger observations for those values for which the
    predicate returns true. The second will trigger observations for
    those values where the predicate returns false. The predicate is
    executed once for each subscribed observer. Both also propagate all
    error observations arising from the source and each completes
    when the source completes.

    Examples:
        >>> res = source.pipe(partition(lambda x: x > 5))
        >>> res = partition(lambda x: x > 5)(source)

    Args:
        source: Source observable to partition.
        predicate: Function to test each element.

    Returns:
        A list of observables. The first triggers when the
        predicate returns True, and the second triggers when the
        predicate returns False.
    """
    pass


@curry_flip
def partition_indexed_(
    source: Observable[_T],
    predicate_indexed: PredicateIndexed[_T],
) -> list[Observable[_T]]:
    """Returns two observables which partition the observations of the
    source by the given indexed function.

    The first will trigger observations for those values for which the
    predicate returns true. The second will trigger observations for
    those values where the predicate returns false. The predicate is
    executed once for each subscribed observer. Both also propagate all
    error observations arising from the source and each completes
    when the source completes.

    Examples:
        >>> res = source.pipe(partition_indexed(lambda x, i: i % 2 == 0))
        >>> res = partition_indexed(lambda x, i: i % 2 == 0)(source)

    Args:
        source: Source observable to partition.
        predicate_indexed: Function to test each element with its index.

    Returns:
        A list of observables. The first triggers when the
        predicate returns True, and the second triggers when the
        predicate returns False.
    """
    pass


__all__ = ["partition_", "partition_indexed_"]
