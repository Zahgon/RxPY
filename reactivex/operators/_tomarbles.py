from typing import Any

from reactivex import Observable, abc
from reactivex.scheduler import NewThreadScheduler
from reactivex.typing import RelativeTime

new_thread_scheduler = NewThreadScheduler()


def to_marbles(
    timespan: RelativeTime = 0.1, scheduler: abc.SchedulerBase | None = None
):
    pass


def stringify(value: Any) -> str:
    """Utility for stringifying an event."""
    string = str(value)
    if len(string) > 1:
        string = f"({string})"

    return string


__all__ = ["stringify"]
