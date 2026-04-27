from collections.abc import Iterator
from sys import maxsize

from reactivex import Observable, abc
from reactivex.disposable import MultipleAssignmentDisposable
from reactivex.scheduler import CurrentThreadScheduler


def range_(
    start: int,
    stop: int | None = None,
    step: int | None = None,
    scheduler: abc.SchedulerBase | None = None,
) -> Observable[int]:
    """Generates an observable sequence of integral numbers within a
    specified range, using the specified scheduler to send out observer
    messages.

    Examples:
        >>> res = range(10)
        >>> res = range(0, 10)
        >>> res = range(0, 10, 1)

    Args:
        start: The value of the first integer in the sequence.
        stop: [Optional] Generate number up to (exclusive) the stop
            value. Default is `sys.maxsize`.
        step: [Optional] The step to be used (default is 1).
        scheduler: The scheduler to schedule the values on.

    Returns:
        An observable sequence that contains a range of sequential
        integral numbers.
    """
    pass


__all__ = ["range_"]
