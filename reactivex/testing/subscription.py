import sys
from typing import Any


class Subscription:
    def __init__(self, start: int, end: int | None = None):
        self.subscribe = start
        self.unsubscribe = end or sys.maxsize

    def equals(self, other: Any) -> bool:
        pass

    def __eq__(self, other: Any) -> bool:
        return self.equals(other)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        unsubscribe = (
            "Infinite" if self.unsubscribe == sys.maxsize else self.unsubscribe
        )
        return f"({self.subscribe}, {unsubscribe})"
