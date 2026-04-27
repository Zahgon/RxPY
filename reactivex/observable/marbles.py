import re
import threading
from collections.abc import Mapping
from datetime import datetime, timedelta
from typing import Any

from reactivex import Notification, Observable, abc, notification, typing
from reactivex.disposable import CompositeDisposable, Disposable
from reactivex.scheduler import NewThreadScheduler

new_thread_scheduler = NewThreadScheduler()

# tokens will be searched in the order below using pipe
# group of elements: match any characters surrounded by ()
pattern_group = r"(\(.*?\))"
# timespan: match one or multiple hyphens
pattern_ticks = r"(-+)"
# comma err: match any comma which is not in a group
pattern_comma_error = r"(,)"
# element: match | or # or one or more characters which are not - | # ( ) ,
pattern_element = r"(#|\||[^-,()#\|]+)"

pattern = r"|".join(
    [
        pattern_group,
        pattern_ticks,
        pattern_comma_error,
        pattern_element,
    ]
)
tokens = re.compile(pattern)


def hot(
    string: str,
    timespan: typing.RelativeTime = 0.1,
    duetime: typing.AbsoluteOrRelativeTime = 0.0,
    lookup: Mapping[str | float, Any] | None = None,
    error: Exception | None = None,
    scheduler: abc.SchedulerBase | None = None,
) -> Observable[Any]:
    pass


def from_marbles(
    string: str,
    timespan: typing.RelativeTime = 0.1,
    lookup: Mapping[str | float, Any] | None = None,
    error: Exception | None = None,
    scheduler: abc.SchedulerBase | None = None,
) -> Observable[Any]:
    pass


def parse(
    string: str,
    timespan: typing.RelativeTime = 1.0,
    time_shift: typing.RelativeTime = 0.0,
    lookup: Mapping[str | float, Any] | None = None,
    error: Exception | None = None,
    raise_stopped: bool = False,
) -> list[tuple[typing.RelativeTime, notification.Notification[Any]]]:
    """Convert a marble diagram string to a list of messages.

    Each character in the string will advance time by timespan
    (exept for space). Characters that are not special (see the table below)
    will be interpreted as a value to be emitted. numbers will be cast
    to int or float.

    Special characters:
        +--------+--------------------------------------------------------+
        |  `-`   | advance time by timespan                               |
        +--------+--------------------------------------------------------+
        |  `#`   | on_error()                                             |
        +--------+--------------------------------------------------------+
        |  `|`   | on_completed()                                         |
        +--------+--------------------------------------------------------+
        |  `(`   | open a group of elements sharing the same timestamp    |
        +--------+--------------------------------------------------------+
        |  `)`   | close a group of elements                              |
        +--------+--------------------------------------------------------+
        |  `,`   | separate elements in a group                           |
        +--------+--------------------------------------------------------+
        | space  | used to align multiple diagrams, does not advance time |
        +--------+--------------------------------------------------------+

    In a group of elements, the position of the initial `(` determines the
    timestamp at which grouped elements will be emitted. E.g. `--(12,3,4)--`
    will emit 12, 3, 4 at 2 * timespan and then advance virtual time
    by 8 * timespan.

    Examples:
        >>> parse("--1--(2,3)-4--|")
        >>> parse("a--b--c-", lookup={'a': 1, 'b': 2, 'c': 3})
        >>> parse("a--b---#", error=ValueError("foo"))

    Args:
        string: String with marble diagram

        timespan: [Optional] duration of each character in second.
            If not specified, defaults to 0.1s.

        lookup: [Optional] dict used to convert an element into a specified
            value. If not specified, defaults to {}.

        time_shift: [Optional] time used to delay every elements.
            If not specified, defaults to 0.0s.

        error: [Optional] exception that will be use in place of the # symbol.
            If not specified, defaults to Exception('error').

        raise_finished: [optional] raise ValueError if elements are
            declared after on_completed or on_error symbol.

    Returns:
        A list of messages defined as a tuple of (timespan, notification).

    """
    pass
