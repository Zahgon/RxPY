from collections.abc import Callable, Iterable
from typing import TypeVar

import reactivex
from reactivex import Observable, abc, typing
from reactivex.disposable import CompositeDisposable
from reactivex.internal import default_comparer

_T = TypeVar("_T")


def sequence_equal_(
    second: Observable[_T] | Iterable[_T],
    comparer: typing.Comparer[_T] | None = None,
) -> Callable[[Observable[_T]], Observable[bool]]:
    comparer_ = comparer or default_comparer
    second_ = (
        reactivex.from_iterable(second) if isinstance(second, Iterable) else second
    )

    def sequence_equal(source: Observable[_T]) -> Observable[bool]:
        """Determines whether two sequences are equal by comparing the
        elements pairwise using a specified equality comparer.

        Examples:
            >>> res = sequence_equal([1,2,3])
            >>> res = sequence_equal([{ "value": 42 }], lambda x, y: x.value == y.value)
            >>> res = sequence_equal(reactivex.return_value(42))
            >>> res = sequence_equal(
                reactivex.return_value({ "value": 42 }),
                lambda x, y: x.value == y.value
            )

        Args:
            source: Source observable to compare.

        Returns:
            An observable sequence that contains a single element which
        indicates whether both sequences are of equal length and their
        corresponding elements are equal according to the specified
        equality comparer.
        """
        first = source

        def subscribe(
            observer: abc.ObserverBase[bool],
            scheduler: abc.SchedulerBase | None = None,
        ) -> abc.DisposableBase:
            donel = [False]
            doner = [False]
            ql: list[_T] = []
            qr: list[_T] = []

            def on_next1(x: _T) -> None:
                pass

            def on_completed1() -> None:
                pass

            def on_next2(x: _T):
                pass

            def on_completed2():
                pass

            subscription1 = first.subscribe(
                on_next1, observer.on_error, on_completed1, scheduler=scheduler
            )
            subscription2 = second_.subscribe(
                on_next2, observer.on_error, on_completed2, scheduler=scheduler
            )
            return CompositeDisposable(subscription1, subscription2)

        return Observable(subscribe)

    return sequence_equal


__all__ = ["sequence_equal_"]
