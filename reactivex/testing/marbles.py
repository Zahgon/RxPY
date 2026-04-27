from collections.abc import Generator
from contextlib import contextmanager
from typing import Any, NamedTuple, cast
from warnings import warn

import reactivex
from reactivex import Observable, typing
from reactivex.notification import Notification, OnError, OnNext
from reactivex.observable.marbles import parse
from reactivex.scheduler import NewThreadScheduler
from reactivex.typing import Callable, RelativeTime

from .reactivetest import ReactiveTest
from .recorded import Recorded
from .testscheduler import TestScheduler

new_thread_scheduler = NewThreadScheduler()


class MarblesContext(NamedTuple):
    start: Callable[
        [Observable[Any] | Callable[[], Observable[Any]]], list[Recorded[Any]]
    ]
    cold: Callable[
        [str, dict[str | float, Any] | None, Exception | None],
        Observable[Any],
    ]
    hot: Callable[
        [str, dict[str | float, Any] | None, Exception | None],
        Observable[Any],
    ]
    exp: Callable[
        [str, dict[str | float, Any] | None, Exception | None],
        list[Recorded[Any]],
    ]


@contextmanager
def marbles_testing(
    timespan: RelativeTime = 1.0,
) -> Generator[MarblesContext, None, None]:
    """
    Initialize a :class:`rx.testing.TestScheduler` and return a namedtuple
    containing the following functions that wrap its methods.

    :func:`cold()`:
    Parse a marbles string and return a cold observable

    :func:`hot()`:
    Parse a marbles string and return a hot observable

    :func:`start()`:
    Start the test scheduler, invoke the create function,
    subscribe to the resulting sequence, dispose the subscription and
    return the resulting records

    :func:`exp()`:
    Parse a marbles string and return a list of records

    Examples:
        >>> with marbles_testing() as (start, cold, hot, exp):
        ...     obs = hot("-a-----b---c-|")
        ...     ex = exp( "-a-----b---c-|")
        ...     results = start(obs)
        ...     assert results == ex

    The underlying test scheduler is initialized with the following
    parameters:
        - created time = 100.0s
        - subscribed = 200.0s
        - disposed = 1000.0s

    **IMPORTANT**: regarding :func:`hot()`, a marble declared as the
    first character will be skipped by the test scheduler.
    E.g. hot("a--b--") will only emit b.
    """
    pass


def messages_to_records(
    messages: list[tuple[typing.RelativeTime, Notification[Any]]],
) -> list[Recorded[Any]]:
    """
    Helper function to convert messages returned by parse() to a list of
    Recorded.
    """
    pass
