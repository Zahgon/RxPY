from collections import OrderedDict
from collections.abc import Callable
from typing import Any, TypeVar

from reactivex import Observable, abc
from reactivex.disposable import CompositeDisposable, SingleAssignmentDisposable
from reactivex.internal import noop
from reactivex.operators import take

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")


def join_(
    right: Observable[_T2],
    left_duration_mapper: Callable[[Any], Observable[Any]],
    right_duration_mapper: Callable[[Any], Observable[Any]],
) -> Callable[[Observable[_T1]], Observable[tuple[_T1, _T2]]]:
    def join(source: Observable[_T1]) -> Observable[tuple[_T1, _T2]]:
        """Correlates the elements of two sequences based on
        overlapping durations.

        Args:
            source: Source observable.

        Return:
            An observable sequence that contains elements
            combined into a tuple from source elements that have an overlapping
            duration.
        """

        left = source

        def subscribe(
            observer: abc.ObserverBase[tuple[_T1, _T2]],
            scheduler: abc.SchedulerBase | None = None,
        ) -> abc.DisposableBase:
            group = CompositeDisposable()
            left_done = False
            left_map: OrderedDict[int, _T1] = OrderedDict()
            left_id = 0
            right_done = False
            right_map: OrderedDict[int, _T2] = OrderedDict()
            right_id = 0

            def on_next_left(value: _T1):
                pass

            def on_completed_left() -> None:
                pass

            group.add(
                left.subscribe(
                    on_next_left,
                    observer.on_error,
                    on_completed_left,
                    scheduler=scheduler,
                )
            )

            def on_next_right(value: _T2):
                pass

            def on_completed_right():
                pass

            group.add(
                right.subscribe(
                    on_next_right,
                    observer.on_error,
                    on_completed_right,
                    scheduler=scheduler,
                )
            )
            return group

        return Observable(subscribe)

    return join


__all__ = ["join_"]
