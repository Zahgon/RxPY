import logging
from collections import OrderedDict
from collections.abc import Callable
from typing import Any, TypeVar

from reactivex import Observable, abc
from reactivex import operators as ops
from reactivex.disposable import (
    CompositeDisposable,
    RefCountDisposable,
    SingleAssignmentDisposable,
)
from reactivex.internal import add_ref
from reactivex.subject import Subject

_TLeft = TypeVar("_TLeft")
_TRight = TypeVar("_TRight")

log = logging.getLogger("Rx")


def group_join_(
    right: Observable[_TRight],
    left_duration_mapper: Callable[[_TLeft], Observable[Any]],
    right_duration_mapper: Callable[[_TRight], Observable[Any]],
) -> Callable[[Observable[_TLeft]], Observable[tuple[_TLeft, Observable[_TRight]]]]:
    """Correlates the elements of two sequences based on overlapping
    durations, and groups the results.

    Args:
        right: The right observable sequence to join elements for.
        left_duration_mapper: A function to select the duration (expressed
            as an observable sequence) of each element of the left observable
            sequence, used to determine overlap.
        right_duration_mapper: A function to select the duration (expressed
            as an observable sequence) of each element of the right observable
            sequence, used to determine overlap.

    Returns:
        An observable sequence that contains elements combined into a tuple
    from source elements that have an overlapping duration.
    """

    def nothing(_: Any) -> None:
        pass

    def group_join(
        left: Observable[_TLeft],
    ) -> Observable[tuple[_TLeft, Observable[_TRight]]]:
        def subscribe(
            observer: abc.ObserverBase[tuple[_TLeft, Observable[_TRight]]],
            scheduler: abc.SchedulerBase | None = None,
        ) -> abc.DisposableBase:
            group = CompositeDisposable()
            rcd = RefCountDisposable(group)
            left_map: OrderedDict[int, Subject[_TRight]] = OrderedDict()
            right_map: OrderedDict[int, _TRight] = OrderedDict()
            left_id = [0]
            right_id = [0]

            def on_next_left(value: _TLeft) -> None:
                pass

            def on_error_left(error: Exception) -> None:
                pass

            group.add(
                left.subscribe(
                    on_next_left,
                    on_error_left,
                    observer.on_completed,
                    scheduler=scheduler,
                )
            )

            def send_right(value: _TRight) -> None:
                pass

            def on_error_right(error: Exception) -> None:
                pass

            group.add(right.subscribe(send_right, on_error_right, scheduler=scheduler))
            return rcd

        return Observable(subscribe)

    return group_join


__all__ = ["group_join_"]
